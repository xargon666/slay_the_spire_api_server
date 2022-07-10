from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine, text
from flask_migrate import Migrate 
from flask_cors import CORS 
import os
from models.Relics import Relics

print("hello from app.py")

app = Flask(__name__)

# Connect app to local db in heroku
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

#SQLALCHEMY_TRACK_MODIFICATIONS

if __name__ == "__main__":
    app.run(debug=True)

# Routes ******************************************************************************************
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    return render_template("index.html")

@app.route('/relics', methods=['POST','GET'])
def handle_relics():
    match request.method:
        case 'POST':
            data = request.get_json()
            new_relic = Relics(
                name=data['name'],
                rarity=data['rarity'],
                class_specific=data['class_specific'],
                description=data['description'],
                flavor_text=data['flavor_text'],
                conditions_for_spawning=data['conditions_for_spawning']
            )
            db.session.add(new_relic)
            db.sessions.commit()
            return {"message":f"New relic {new_relic.name} has been added to the db"}

        case 'GET':
            relics = Relics.query.all()
            results = [
            {
                "id": relic.id,
                "name": relic.name,
                "rarity": relic.rarity,
                "class_specific": relic.class_specific,
                "description": relic.description,
                "flavor_text": relic.flavor_text,
                "conditions_for_spawning": relic.conditions_for_spawning
            } for relic in relics ]
            return {"count": len(results), "relics": results}
        case _:
            return "You have made an unsupported request"

@app.route('/relics/<id>', methods=['PUT','GET'])
def handle_relics_id(id):
    match request.method:
        case 'PUT':
            data = request.get_json()
            new_relic = Relics(
                name=data['name'],
                rarity=data['rarity'],
                class_specific=data['class_specific'],
                description=data['description'],
                flavor_text=data['flavor_text'],
                conditions_for_spawning=data['conditions_for_spawning']
            )
            db.session.add(new_relic)
            db.sessions.commit()
            return {"message":f"New relic {new_relic.name} has been added to the db"}

        case 'GET':
            relics = Relics.query.all()
            results = [
            {
                "id": relic.id,
                "name": relic.name,
                "rarity": relic.rarity,
                "class_specific": relic.class_specific,
                "description": relic.description,
                "flavor_text": relic.flavor_text,
                "conditions_for_spawning": relic.conditions_for_spawning
            } for relic in relics ]
            return {"count": len(results), "relics": results}
        case _:
            return "You have made an unsupported request"


# # # run db setup and seed
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# with engine.connect() as con:
#     with open("./migrations/1_setup.sql") as file:
#         query = text(file.read())
#         con.execute(query)
#     with open("./migrations/2_seed.sql") as file:
#         query = text(file.read())
#         con.execute(query)

# @app.route('/product', methods=['GET'])
# def get_relics():
#     all_relics = "" # db.query.all()
