from flaskInit import *
from endpoints.players_Endpoint import playersEP
from endpoints.monsterManual_Endpoint import monsterManualEP

# Create blueprints to record endpoints operations
app.register_blueprint(playersEP)
app.register_blueprint(monsterManualEP)
    
if __name__ == "__main__":
    app.run(debug=True)
    