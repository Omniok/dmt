from flaskInit import db

# Build model for table containing Player Table
class players(db.Model): 
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    armorClass = db.Column(db.Integer, nullable=False)
    movement = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(100), nullable=False)
    spellSlots = db.Column(db.Integer, nullable=False)
    
    def __repr__(self): 
        return f"Player(Name = {name}, Health = {health}, Armor Class = {armorClass}, Movement = {movement}, Size = {size}, Spell Slots = {spellSlots}" 
