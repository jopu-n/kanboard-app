from kanboard import *
import pickle

test = MainTask("Tomorrow", "Yesterday","Nico")
test2 = ProgramTask("Tomorrow","Yesterday","Nico","Facebook")

test3 = MainTask("Tomorrow", "Yesterday","Nico")
test4 = ProgramTask("Tomorrow","Yesterday","Nico","Facebook")
tes = MainTask("Tomorrow", "Yesterday","Nico")
test5 = ProgramTask("Tomorrow","Yesterday","Nico","Facebook")

PIK="pickle.dat"

# We dump data list which includes classes to pickle.dat
with open(PIK,"wb") as f:
    pickle.dump(data,f)

# Loads everything from pickle.dat
def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

items = loadall("pickle.dat")

# Print all items in pickle.dat
for i in items:
    for obj in i:
        print(obj.ticket_id)

