import json
f = open("test.json","r")
d = f.read()
d = json.loads(d)
print(d["highscore"])
f.close()
r = open("test.json","w")
d["highscore"]+=1
d = json.dumps(d)
r.write(d)
r.close()