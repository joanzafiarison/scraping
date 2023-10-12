
from flask import Flask , send_from_directory , current_app, request, abort
from markupsafe import escape
import os

app = Flask(__name__, static_folder='../front/dist/assets')

#Ajout d'une clé secrete pour signer JWT
SECRET_KEY = os.environ.get("SECRET_KEY")
print(SECRET_KEY)

app.config["SECRET_KEY"] = SECRET_KEY

@app.route("/")
def hello_world():
    return send_from_directory("../front/dist",'index.html')

#Results   results/<ID-category>?date=""&ORD="asc"
@app.route("/results/<int:category_id>") #/date=<datetime>&ord=<order>"
def get_results(category_id):
    return f"Result for : {escape(category_id)} in XX order for XX"

#JOB  jobs/<ID-category>?date""
@app.route("/jobs/<int:category_id>")
def get_jobs(category_id):
    return f"Jobs for {escape(category_id)} after XX"

@app.route("/struct/<int:map_id>")
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
@app.route("/login")
def login():
    return "Login endpoint"

#Profil
@app.route("/profil")
def profil():
    return "Profil end point"