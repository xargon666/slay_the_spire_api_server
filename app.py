from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine, text
from flask_migrate import Migrate 
from flask_cors import CORS 
import os

print("hello from app.py")

app = Flask(__name__)

# Connect app to local db in heroku
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# postgres://jremcexhoaamgj:781f3245c24665d1e930c6a310d6dd87e934937aa8f5942f120a1aa41114ec52@ec2-3-248-121-12.eu-west-1.compute.amazonaws.com:5432/df67jta2kdc8ba



# Setup Model for db
class RelicModel(db.Model):
    __tablename__ = 'relics'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String())
    rarity = db.Column(db.String())
    class_specific = db.Column(db.String())
    description = db.Column(db.String())
    flavor_text = db.Column(db.String())
    conditions_for_spawning = db.Column(db.String())

    def __init__(self,name,rarity,class_specific,description,flavor_text,conditions_for_spawning):
        self.name = name
        self.rarity = rarity
        self.class_specific = class_specific
        self.description = description
        self.flavor_text = flavor_text
        self.conditions_for_spawning = conditions_for_spawning
    
    def __repr__(self):
        return f"<Relic {self.name}"
    
@app.route('/relics', methods=['POST','GET','DELETE'])
def handle_relics():
    match request.method:
        case 'POST':
            data = request.get_json()
            new_relic = RelicModel(
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
            relics = RelicModel.query.all()
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

        case 'DELETE':
            return
        case _:
            return "Unsupported request"


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
