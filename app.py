from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # ???
from flask_cors import CORS # for routes?
import os

app = Flask(__name__)

# Connect app to local db in heroku
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL').replace("://", "ql://", 1)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

print("hello from app.py")

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
