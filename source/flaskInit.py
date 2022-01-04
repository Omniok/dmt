import os, sys
try:
    from flask import Flask
    from flask_restful import Api
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
