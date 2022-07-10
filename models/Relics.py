from app import db
class Relics(db.Model):
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
