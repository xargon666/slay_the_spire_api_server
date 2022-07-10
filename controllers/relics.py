from werkzeug.exceptions import BadRequest
from models.Relics import Relics
from app import db

def index(req):
    print(Relics)
    relics = db.session.query(Relics).all()
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
    return results, 200

def create(req):
    data = req.get_json()
    new_relic = Relics(
        name=data['name'],
        rarity=data['rarity'],
        class_specific=data['class_specific'],
        description=data['description'],
        flavor_text=data['flavor_text'],
        conditions_for_spawning=data['conditions_for_spawning']
    )
    db.session.add(new_relic)
    db.session.commit()
    return {"message":f"New relic {new_relic.name} has been added to the db"}, 201

def show(req,id):
    relic = db.session.query(Relics).get(id)
    results = {
        "id": relic.id,
        "name": relic.name,
        "rarity": relic.rarity,
        "class_specific": relic.class_specific,
        "description": relic.description,
        "flavor_text": relic.flavor_text,
        "conditions_for_spawning": relic.conditions_for_spawning
    }
    return results, 200

def update(req,id):
    # get the record from the db
    relic = db.session.query(Relics).get(id)
    # take update values from req body
    name=req.json['name'],
    rarity=req.json['rarity'],
    class_specific=req.json['class_specific'],
    description=req.json['description'],
    flavor_text=req.json['flavor_text'],
    conditions_for_spawning=req.json['conditions_for_spawning']
    # update relic values
    relic.name = name
    relic.rarity = rarity
    relic.class_specific = class_specific
    relic.description = description
    relic.flavor_text = flavor_text
    relic.conditions_for_spawning = conditions_for_spawning
    # commit changes
    db.session.commit()
    return {"message":f"Relic {relic.name} has been updated"}, 200

def destroy(req,id):
    relic = db.session.query(Relics).get(id)
    db.session.delete(relic)
    db.session.commit()
    return {"message":f"{relic.id} has now been deleted"},204


# def new(req):
#     return something, 200

# def edit(req):
#     return something, 200


"""

            return "You have made an unsupported request"
"""
