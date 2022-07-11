from app import app, db
from flask import request, render_template, send_from_directory, jsonify
from controllers import index, show, create, update, destroy
from models.Relics import Relics

# Routes ******************************************************************************************

# Default home route
# @app.route('/')
# def home():
#     return render_template('index.html')

# Catch All Redirect to Index.html
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    print("path accessed:", path)
    return render_template("index.html")

# Added route attempting to fix static favicon.ico bug
# @app.route("/favicon.ico")
# def favicon():
#     path_static = os.path.join(app.root_path, "static")
#     print(path_static)
#     return send_from_directory(
#         path_static, "favicon.ico", mimetype="image/vnd.microsoft.icon"
#     )

# Load New Relic Form
@app.route("/new")
def new_handler():
    return render_template("new.html")

# Load Edit Relic Form - WIP
@app.route("/edit")
def edit_handler():
    relics = db.session.query(Relics).all()
    print(type(relics))
    print(type(relics[0]))
    return render_template("edit.html", relics=relics, Relics=Relics)

# Routes for GET/POST ALL
@app.route("/relics", methods=["GET", "POST"])
def relics_handler():
    fns = {"GET": index, "POST": create}
    if request.method == "POST":
        print("request.form", request.form)
        # dump(request.form)
        obj = {
            "name": request.form["name"],
            "rarity": request.form["rarity"],
            "class_specific": request.form["class_specific"],
            "description": request.form["description"],
            "flavor_text": request.form["flavor_text"],
            "conditions_for_spawning": request.form["conditions_for_spawning"],
        }
        resp, code = fns[request.method](jsonify(obj))
    elif request.method == "GET":
        resp, code = fns[request.method](request)
    return jsonify(resp), code

# Routes for GET/POST/DELETE by ID
@app.route("/relics/<id>", methods=["GET", "PUT", "DELETE"])
def relics_id_handler(id):
    fns = {"GET": show, "PUT": update, "DELETE": destroy}
    resp, code = fns[request.method](request, id)
    return jsonify(resp), code
