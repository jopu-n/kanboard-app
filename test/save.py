import kanboard1 as kb
import pickle, sys


# Creates and dumps data into pickle.dat file
def save_all():
    print("Saved")
    PIK="pickle.dat"
    # We dump data list which includes classes to pickle.dat
    with open(PIK,"wb") as f:
        pickle.dump(kb.data,f)


# Loads everything from pickle.dat
def load_all(filename):
    try:
        with open(filename, "rb") as f: # Loads file
            print("Loaded")
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
    except OSError:# Error if there is no pickle file. 
        save_all() # Creates the file
        print("Created Pickle ;)")
        with open(filename, "rb") as f:# Loads from the file after created 
            print("Loaded")
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break



