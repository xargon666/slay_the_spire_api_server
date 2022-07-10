from app import app, db, os
from flask import request, render_template, send_from_directory, jsonify
from controllers import index, create, show, update, destroy # new, edit

# Routes ******************************************************************************************
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/relics', methods=['GET','POST'])
def relics_handler():
    fns = {
        'GET': index,
        'POST': create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/relics/<id>', methods=['GET','PUT','DELETE'])
def relics_id_handler(id):
        fns = {
        'GET': show,
        'PUT': update,
        'DELETE': destroy
    }
        resp, code = fns[request.method](request,id)
        return jsonify(resp), code
