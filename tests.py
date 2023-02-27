import db
import config
import random
confi.debug = True

db.create("t")

data = db.get("t")
print(data)

f = ["you gay!", "you not gay!"]
data["you gay?"] = random.choice(f)
db.set("t", data)

print(db.get("t"))

db.delete("t")