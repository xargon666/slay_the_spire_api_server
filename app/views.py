from app import app, db, os
from flask import request, render_template, send_from_directory, jsonify
from controllers import index, show, create, update, destroy

# Routes ******************************************************************************************
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")


@app.route("/new")
def new_handler():
    return render_template("new.html")


@app.route("/edit")
def edit_handler():
    return render_template("edit.html")


@app.route("/relics", methods=["GET", "POST"])
def relics_handler():
    fns = {"GET": index, "POST": create}
    if request.method == 'POST':
        print("request.form",request.form)
        obj = {
            "name": request.form["name"],
            "rarity": request.form["rarity"],
            "class_specific": request.form["class_specific"],
            "description": request.form["description"],
            "flavor_text": request.form["flavor_text"],
            "conditions_for_spawning": request.form["conditions_for_spawning"]
        }
        resp, code = fns[request.method](jsonify(obj))
    elif request.method == 'GET':
        resp, code = fns[request.method](request)
    return jsonify(resp), code


@app.route("/relics/<id>", methods=["GET", "PUT", "DELETE"])
def relics_id_handler(id):
    fns = {"GET": show, "PUT": update, "DELETE": destroy}
    resp, code = fns[request.method](request, id)
    return jsonify(resp), code
