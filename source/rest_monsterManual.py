import os, sys

try:
    from flask import Flask
    from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
    from flask_sqlalchemy import SQLAlchemy
except:
    try:
        os.system("pip install -U requests flask flask_restful flask_sqlalchemy")
        print("Necessary modules not installed at runtime. Installation through pip has been attempted, please restart the program.")
    except:
        print("Unable to install required modules.")
    sys.exit()

app = Flask(__name__)
api = Api(app)
# unix sqlite: ////absolute/path/to/foo.db
# windows sqlite: ///C:\\absolute\\path\\to\\foo.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Build model for database containing Monster Manual
class MonsterManual(db.Model): 
    __tablename__ = 'MonsterManual'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    armorClass = db.Column(db.Integer, nullable=False)
    movement = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(100), nullable=False)
    
    def __repr__(self): 
        return f"Enemy(Name = {name}, Health = {health}, Armor Class = {armorClass}, Movement = {movement}, Size = {size}" 

# Define arguments to use when adding enemies or updating the stats of a preexisting enemy
mo_enemy_args = reqparse.RequestParser() # For adding enemies to the database
mo_enemy_args.add_argument("name", type=str, help="Name of the enemy required", required=True)
mo_enemy_args.add_argument("health", type=int, help="Health of the enemy required", required=True)
mo_enemy_args.add_argument("armorClass", type=int, help="Armor class of the enemy required", required=True)
mo_enemy_args.add_argument("movement", type=int, help="Movement of the enemy required", required=True)
mo_enemy_args.add_argument("size", type=str, help="Size of the enemy required", required=True)

update_enemy_args = reqparse.RequestParser() # For updating enemies already on the database
update_enemy_args.add_argument("name", type=str, help="Name of the enemy")
update_enemy_args.add_argument("health", type=int, help="Health of the enemy")
update_enemy_args.add_argument("armorClass", type=int, help="Armor class of the enemy")
update_enemy_args.add_argument("movement", type=int, help="Movement of the enemy")
update_enemy_args.add_argument("size", type=str, help="Size of the enemy")

# Define resource fields    
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'health': fields.Integer, 
    'armorClass': fields.Integer,
    'movement': fields.Integer,
    'size': fields.String
}

# Class for the enemies in the Monster Manual, enclosed are functions to perform queries with the sqlite3 database
class Enemy(Resource):
    @app.route("/MonsterManual", methods=["PUT"])
    @marshal_with(resource_fields)
    def put(self, enemy_id):
        # Gather arguments to use
        args = mo_enemy_args.parse_args()
        # Run query to find the enemy we are trying to add to the Monster Manual
        result = MonsterManual.query.filter_by(id=enemy_id).first()
        # If found
        if result:
            abort(409, message="Enemy already exists in this Monster Manual") # 409 since already exists
        # Define enemy based on arguments before putting it into the database
        enemy = MonsterManual(id=enemy_id, name=args['name'], health=args['health'], 
                              armorClass=args['armorClass'], movement=args['movement'], size=args['size'])
        db.session.add(enemy) # Add to database
        db.session.commit() # Commit addition to the database
        # Return things went peachy (200)
        return enemy, 200
        
    @app.route("/MonsterManual", methods=["PATCH"])
    @marshal_with(resource_fields)
    def patch(self, enemy_id):
        # Gather arguments to use
        args = update_enemy_args.parse_args()
        # Run query to find the enemy we are trying to update stats on
        result = MonsterManual.query.filter_by(id=enemy_id).first()
        # If not found in Monster Manual
        if not result:
            abort(404, message="Enemy doesn't exist, please add enemy to database") # 404 as does not exist
        # Otherwise, update whatever stats accordingly, i.e., if provided 
        if args['name']:
            result.name = args['name']
        if args['health']:
            result.health = args['health']
        if args['armorClass']:
            result.armorClass = args['armorClass']
        if args['movement']:
            result.movement = args['movement']
        if args['size']:
            result.size = args['size']
        # Commit changes to the database
        db.session.commit()
        # Return result to show successful update of enemy information
        return result
    
    @app.route("/MonsterManual", methods=["DELETE"]) 
    @marshal_with(resource_fields)
    def delete(self, enemy_id):
        # Run query to check for the presence of the enemy in the Monster Manual
        result = MonsterManual.query.filter_by(id=enemy_id).first()
        # If found
        if result:
            db.session.query(MonsterManual).filter(MonsterManual.id==enemy_id).delete() # Delete the entry from the database
            db.session.commit() # And commit the changes to the database
            return result # Return what has been deleted
        
        # Return that the enemy wasn't found in the Monster Manual database
        return result, 404  
               
    @app.route("/MonsterManual", methods=["GET"])
    @marshal_with(resource_fields)
    def get(self, enemy_id):
        # Run query to check for the presence of the enemy in the Monster Manual
        result = MonsterManual.query.filter_by(id=enemy_id).first()
        # If not found in Monster Manual database
        if not result:
            abort(404, message="Could not find enemy in Monster Manual") # 404 not found
        # Return result to show found enemy
        return result
             
api.add_resource(Enemy, "/enemy/<int:enemy_id>")

if __name__ == "__main__":
    app.run(debug=True)
