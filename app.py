from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy, create_engine, text
from flask_migrate import Migrate # ???
from flask_cors import CORS # for routes?
import os

print("hello from app.py")

app = Flask(__name__)

# Connect app to local db in heroku
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL').replace("://", "ql://", 1)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# run db setup and seed
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

with engine.connect() as con:
    with open("./migrations/1_setup.sql") as file:
        query = text(file.read())
        con.execute(query)
    with open("./migrations/seed.sql") as file:
        query = text(file.read())
        con.execute(query)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/product', methods=['GET'])
def get_relics():
    all_relics = "" # db.query.all()


if __name__ == "__main__":

    app.run(debug=True)
