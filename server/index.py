
from flask import Flask , send_from_directory , current_app, request, abort
from markupsafe import escape
import os

from model.schema import User
from model.db import db

from middlewares.auth_middleware import token_required

app = Flask(__name__, static_folder='../front/dist/assets')

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


with app.app_context():
    db.create_all()

#Ajout d'une clé secrete pour signer JWT
SECRET_KEY = os.environ.get("SECRET_KEY")

app.config["SECRET_KEY"] = SECRET_KEY

@app.route("/")
def hello_world():
    return send_from_directory("../front/dist",'index.html')

#Results   results/<ID-category>?date=""&ORD="asc"
@app.route("/results/<int:category_id>") #/date=<datetime>&ord=<order>"
@token_required
def get_results(category_id):
    return f"Result for : {escape(category_id)} in XX order for XX"

#JOB  jobs/<ID-category>?date""
@app.route("/jobs/<int:category_id>")
@token_required
def get_jobs(category_id):
    return f"Jobs for {escape(category_id)} after XX"

@app.route("/struct/<int:map_id>")
@token_required
def get_html_struct(map_id):
    print("res", map_id)
    return f"Structure id {escape(map_id)}"

@app.route("/test/<name>")
def get_test(name):
    print("res", name)
    return f"name {escape(name)}"
#Structure  struc/<ID-Map> 

#Auth 
@app.route("/auth")
def auth():
    return "Auth endpoint"

#Login
@app.route("/login", methods=["POST"])
def login():
    users = db.session.execute(db.select(User).where(User.email == request.form["email"]).where(User.password == request.form["password"])).scalars().all()
    if len(users) == 1 :
        return "Login endpoint "+users[0].username
    else : 
        return "User not found"

#Login
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
@app.route("/profil")
@token_required
def profil():
    return "Profil end point"