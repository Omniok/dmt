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

# Build model for table containing Player Table
class players(db.Model): 
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    armorClass = db.Column(db.Integer, nullable=False)
    movement = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(100), nullable=False)
    
    def __repr__(self): 
        return f"Player(Name = {name}, Health = {health}, Armor Class = {armorClass}, Movement = {movement}, Size = {size}" 

# Define arguments to use when adding enemies or updating the stats of a preexisting player
mo_player_args = reqparse.RequestParser() # For adding enemies to the database
mo_player_args.add_argument("name", type=str, help="Name of the player required", required=True)
mo_player_args.add_argument("health", type=int, help="Health of the player required", required=True)
mo_player_args.add_argument("armorClass", type=int, help="Armor class of the player required", required=True)
mo_player_args.add_argument("movement", type=int, help="Movement of the player required", required=True)
mo_player_args.add_argument("size", type=str, help="Size of the player required", required=True)

update_player_args = reqparse.RequestParser() # For updating enemies already on the database
update_player_args.add_argument("name", type=str, help="Name of the player")
update_player_args.add_argument("health", type=int, help="Health of the player")
update_player_args.add_argument("armorClass", type=int, help="Armor class of the player")
update_player_args.add_argument("movement", type=int, help="Movement of the player")
update_player_args.add_argument("size", type=str, help="Size of the player")

# Define resource fields    
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'health': fields.Integer, 
    'armorClass': fields.Integer,
    'movement': fields.Integer,
    'size': fields.String
}

# Class for the enemies in the Player Table, enclosed are functions to perform queries with the sqlite3 database
class Player(Resource):
    @app.route("/players", methods=["PUT"])
    @marshal_with(resource_fields)
    def put(self, player_id):
        # Gather arguments to use
        args = mo_player_args.parse_args()
        # Run query to find the player we are trying to add to the Player Table
        result = players.query.filter_by(id=player_id).first()
        # If found
        if result:
            abort(409, message="Player already exists in this Player Table") # 409 since already exists
        # Define player based on arguments before putting it into the database
        player = players(id=player_id, name=args['name'], health=args['health'], 
                              armorClass=args['armorClass'], movement=args['movement'], size=args['size'])
        db.session.add(player) # Add to database
        db.session.commit() # Commit addition to the database
        # Return things went peachy (200)
        return player, 200
        
    @app.route("/players", methods=["PATCH"])
    @marshal_with(resource_fields)
    def patch(self, player_id):
        # Gather arguments to use
        args = update_player_args.parse_args()
        # Run query to find the player we are trying to update stats on
        result = players.query.filter_by(id=player_id).first()
        # If not found in Player Table
        if not result:
            abort(404, message="Player doesn't exist, please add player to database") # 404 as does not exist
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
        # Return result to show successful update of player information
        return result
    
    @app.route("/players", methods=["DELETE"]) 
    @marshal_with(resource_fields)
    def delete(self, player_id):
        # Run query to check for the presence of the player in the Player Table
        result = players.query.filter_by(id=player_id).first()
        # If found
        if result:
            db.session.query(players).filter(players.id==player_id).delete() # Delete the entry from the database
            db.session.commit() # And commit the changes to the database
            return result # Return what has been deleted
        
        # Return that the player wasn't found in the Player Table database
        return result, 404  
               
    @app.route("/players", methods=["GET"])
    @marshal_with(resource_fields)
    def get(self, player_id):
        # Run query to check for the presence of the player in the Player Table
        result = players.query.filter_by(id=player_id).first()
        # If not found in Player Table database
        if not result:
            abort(404, message="Could not find player in Player Table") # 404 not found
        # Return result to show found player
        return result
             
api.add_resource(Player, "/player/<int:player_id>")

if __name__ == "__main__":
    app.run(debug=True)
