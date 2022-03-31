import kanboard1 as kb
import pickle, sys

test = kb.MainTask("Tomorrow", "Yesterday","Nico")
test2 = kb.ProgramTask("Tomorrow","Yesterday","Nico","Facebook")

test3 = kb.MainTask("Tomorrow", "Yesterday","Nico")
test4 = kb.ProgramTask("Tomorrow","Yesterday","Nico","Facebook")
tes = kb.MainTask("Tomorrow", "Yesterday","Nico")
test5 = kb.ProgramTask("Tomorrow","Yesterday","Nico","Facebook")




def save_all():
    print("Saved")
    PIK="pickle.dat"
    # We dump data list which includes classes to pickle.dat
    with open(PIK,"wb") as f:
        pickle.dump(kb.data,f)


# Loads everything from pickle.dat
def load_all(filename):
    try:
        with open(filename, "rb") as f:
            print("Loaded")
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
    except OSError:
        save_all()
        print("Created Pickle ;)")
        with open(filename, "rb") as f:
            print("Loaded")
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break


items = load_all("pickle.dat")

