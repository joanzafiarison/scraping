
from flask import Flask , render_template 
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! </p>"

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