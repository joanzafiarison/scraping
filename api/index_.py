
from flask import Flask , send_from_directory , jsonify , request 
from werkzeug.utils import secure_filename
from markupsafe import escape
import os

from model.schema import User , Struct , ResultJob, Job, Category
from model.db import db

from services.executor import execute_command, run_scraper

from middlewares.auth_middleware import token_required
import jwt

from queue import Queue, Empty
from threading import Thread
from time import sleep

import json


UPLOAD_FOLDER= os.path.join(os.getcwd(),"server/files")
ALLOWED_EXTENSIONS = {'txt','csv','json'}
app = Flask(__name__, static_folder='../front/dist/assets')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


with app.app_context():
    db.create_all()

commands = Queue()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def process_loop():
    while True:
        try: 
            command = commands.get_nowait()
            print("command",command)
            if command["test"] == "success":
                print("success of ",command["job_id"])
            elif command["test"] == "cancel" :
                print("cancel of ",command["job_id"])
            else :
                print("run crawler ",command["action"])
                #print("command ", command)
                run_scraper(command)
        except Empty :
            pass
        sleep(5)

#start process in another loop
t1 = Thread(target=process_loop, daemon = True)
t1.start()


#Ajout d'une clé secrete pour signer JWT
SECRET_KEY = os.environ.get("SECRET_KEY")

app.config["SECRET_KEY"] = SECRET_KEY

@app.route("/")
def hello_world():
    return send_from_directory("../front/dist",'index.html')


''' Job id , user id, '''
@app.route("/perform", methods=["POST"])
def perform():
    url = request.form["url"]
    sitemap_id = request.form["sitemap_id"]
    model = request.form["model"]

    if sitemap_id != "":
        #get sitemap
        #load model? deja dans le sitemap
        data = {
            'url' : url,
            'sitemap_id' : sitemap_id,
            'model' : model
        }
        commands.put_nowait({'action' : 'scraping', 'struct' :842, 'data' : data, 'test' : False})
        #print("known content",sitemap_id)
    else : 
        data = {
            'url' : url,
            'sitemap_id' : sitemap_id,
            'model' : model
        }
        commands.put_nowait({'action' : 'scan', 'data' : data, 'test' : False})
        #print("using model",model)
    return "performing"

@app.route("/perform/<int:job_id>", methods=["POST"])
def perform_job(job_id):
    #si le job_id est associé a l'user id
    #lancer le scraping
    email = request.form["email"]
    user_id = request.form["user_id"]
    isTest= request.form["test"]

    users = db.session.execute(db.select(User).where(User.email == email)).scalars().all()
    if len(users) == 1 :
        try :
            #asynchrone
            #execute_command()
            #run_crawler()
            commands.put_nowait({'action' : 'scraping', 'struct' :842, 'job_id' :job_id , "test": isTest })
            return f"perform job id {escape(job_id)} for user {users[0].username}"
        except :
            return "Server unavailable"
    else :
        return "unauthentified user"
    

#Results   results/<ID-category>?date=""&ORD="asc"
@app.route("/results/category/<int:category_id>") #/date=<datetime>&ord=<order>"
@token_required
def get_results(category_id):
    return f"Result for : {escape(category_id)} in XX order for XX"

@app.route("/results/job/<int:job_id>") #/date=<datetime>&ord=<order>"
@token_required
def get_job_result(job_id):
    return f"Result for job {escape(job_id)} in XX order for XX"

#JOB  jobs/<ID-category>?date""
@app.route("/jobs/category/<int:category_id>")
@token_required
def get_jobs(category_id):
    return f"Get Job for  {escape(category_id)} after XX"


@app.route("/job", methods=["POST"])
@token_required
def create_job(job_id):
    due_date = request.form["due_date"]
    file_data = request.files["file"]
    jobs = db.session.execute(db.select(Job).where(Job.due_date == due_date)).scalars().all()
    if len(jobs) == 0 :
        job = Job (
            due_date = due_date,
            filepath = file_data
        )
        db.session.add(job)
        db.session.commit()
        return f"Create job id {escape(job_id)} due to {due_date}"
    else :
        return f'Error creating a JOb'

    

@app.route("/job/<int:job_id>", methods=["GET"])
@token_required
def get_job(job_id):
    return f"Get job id {escape(job_id)} after XX"

@app.route("/jobs/<int:job_id>", methods=["UPDATE"])
@token_required
def update_job(job_id):
    return f"Update Jobs  {escape(job_id)} after XX"

@app.route("/jobs/<int:job_id>", methods=["DELETE"])
@token_required
def delete_job(job_id):
    return f"Delete Job {escape(job_id)} after XX"


@app.route("/categories", methods=["GET"])
def get_categories():
    categories = db.session.execute(db.select(Category)).scalars().all()
    if len(categories) > 1 :
        return " ".join([category.name for category in categories])
    else :
        return "no categories"
    
@app.route("/categories/<int:category_id>", methods=["GET"])
def get_category_by_id(category_id):
    categories = db.session.execute(db.select(Category).where(Category.id == category_id)).scalars().all()
    if len(categories) == 1 :
        return jsonify(
            name = categories[0].name,
            filepath = categories[0].filepath
        )
    else :
        return "no categories"


@app.route("/categories/<int:category_id>", methods=["DELETE"])
def delete_category():
    name = request.form["name"]
    try :
        db.session.delete(db.select(Category).where(Category.name == name))
    except Exception as e :
        return "db error"
    return f"category {name} deleted"

    
@app.route("/categories/create", methods=["POST"])
def create_category():
    print("attempt category creation")
    name = request.form["name"]
    keys = request.form["keys"]

    #recupérer id category 
    #Et créer les clés
    category = Category (
        name = name,
    )
    try :
        db.session.add(category)
        db.session.commit()
    except Exception as e: 
        return "Error creating category"
    return f'category {name} created'

#>>Add blueprint

@app.route("/structs", methods=["GET"])
def get_html_structs():
    structs = db.session.execute(db.select(Struct)).scalars().all()
    if len(structs) > 1 :
        #return  f'fichiers structures créés {", ".join([struct.name for struct in structs])}'
        return jsonify(
         struct = structs
        )
    else : 
        return "no struct found"

    
#Structure  struc/<ID-Map> 
@app.route("/struct/<int:map_id>", methods=["GET"])
#@token_required
def get_html_struct(map_id):
    structs = db.session.execute(db.select(Struct).where(Struct.id == map_id)).scalars().all()
    if len(structs) == 1 :
        f = open(structs[0].filepath,"r")
        data = json.load(f)
        return jsonify(
            id = structs[0].id,
            name = structs[0].name,
            data= data
        )
    return f'Id {map_id} not found'

@app.route("/struct/", methods=["POST"])
def create_html_struct_by_data():
    name = request.form["name"]
    category = request.form["category"]
    meta = request.form["meta"]

    metadata = json.loads(meta)
    #struct_file = open("")
    try :
        #convert to string
        sitemap_data = json.dumps(metadata, indent=4)
        #writing to file
    except Exception as e :
        return "JSON error"
    
    try : 
        filepath = f"{app.config['UPLOAD_FOLDER']}/structs/{name}.json"
        with open(filepath , "w") as struct_file :
            struct_file.write(sitemap_data)
    except Exception as e :
        return "File error"

    print(metadata)
    #check if category name exists
    #get sitemap meta + single 

    struct = Struct (
        name = name,
        filepath = filepath,
        category = 1
    )

    try :
        db.session.add(struct)
        db.session.commit()
    except Exception as e: 
        return "Error creating Struct"
    
    
    return f'Struct {name} created'

#create
@app.route("/struct/upload", methods=["POST"])
#@token_required
def create_html_struct_by_file():
    name = request.form["name"]
    category=request.form["category"]
    


    #check if we have a file
    #ImmutableMultiDict([('files', <FileStorage: 'airpod.png' ('image/png')>)])
    if "file" in request.files :
        file_data = request.files["file"]
        print("f data ",file_data)
        structs = db.session.execute(db.select(Struct).where(Struct.name == name)).scalars().all()
        if len(structs) == 0 :
            filename = secure_filename(file_data.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"structs/{filename}")
            struct = Struct(
                name= name,
                category = category,
                filepath = filepath
            )
            #save file in upload folder
            try :
                file_data.save(filepath)
            except Exception as e :
                print('File error', e)
            db.session.add(struct)
            db.session.commit()
            return f" struct {name} created"
        else :
            return f'error creating struct {name}'
    else : 
        return f'no file provided'

  

#delete
@app.route("/struct/<int:map_id>", methods=["DELETE"])
#@token_required
def delete_html_struct(map_id):
    struct = db.session.execute(db.select(Struct).where(Struct.id == map_id)).scalars().all()
    if len(struct) == 1 : 
        db.session.delete(struct[0])
        db.session.commit()
    return f"delete Structure id {escape(map_id)}"

#update
@app.route("/struct/<int:map_id>", methods=["PUT"])
def update_html_struct(map_id):
    name = request.form["name"]
    #get keys
    struct = db.session.execute(db.select(Struct).where(Struct.id == map_id)).scalars().all()
    db.session.commit()
    if len(struct) == 1 :
        struct[0].name = name 
        #db.session.update(struct[0]).values(name=name)
        db.session.commit()
    return f"update Structure id {escape(map_id)}"



#>>>
#Login
@app.route("/login", methods=["POST"])
def login():
    users = db.session.execute(db.select(User).where(User.email == request.form["email"]).where(User.password == request.form["password"])).scalars().all()
    if len(users) == 1 :
        #return token
        #if role = user return know as "user", "admin"
       
        return "Login endpoint "+users[0].username
    else : 
        return "User not found"

#Register
@app.route("/register", methods = ["POST"])
def register():
    try : 
        users = db.session.execute(db.select(User).where(User.email == request.form["email"])).scalars().all()
        if len(users) == 0 :
            user = User(
                username=request.form["username"],
                email=request.form["email"],
                password = request.form["password"],
                role = request.form["role"]
            )
            db.session.add(user)
            db.session.commit()
            return "User registered"
        else :
            return "user already in"
    except Exception as e : 
        return "erreur de données"


#Profil
@app.route("/profil", methods=["GET"])
@token_required
def profil():
    users = db.session.execute(db.select(User).where(User.email == request.form["email"])).scalars().all()
    if len(users) == 1 :
        return {
            "username" : users[0].username,
            "email" :users[0].email,
            "role" :users[0].role
        }
    else :
        return "erreur DB"
    
@app.route("/profil", methods=["UPDATE"])
@token_required
def udpate_profil():
    try : 
        users = db.session.execute(db.update(User).where(User.email == request.form["email"]))
        
    except :
        return  "erreur serveur"

@app.route("/profil", methods=["DELETE"])
@token_required
def delete_profil():
    try : 
        deletion = db.session.delete(User).where(User.email == request.form["email"])
        print("prints deletion ", deletion)
    except Exception as e : 
        return "DB problem"
    return "profil deleted"