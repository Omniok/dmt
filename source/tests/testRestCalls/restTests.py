from testM import testMonsterManual
from testP import testPlayer
BASE = "http://127.0.0.1:5000/"

# Run tests
testMonsterManual(BASE)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
testPlayer(BASE)
