# Name:         savepy
# Modified by:  Johannes Natunen, Nico Kranni
# Description:  Program that handles loading and saving data


import kanboard_classes as kb
import pickle, sys


# Creates and dumps data into pickle.dat file
def save_all():
    PIK="pickle.dat"
    # We dump data list which includes classes to pickle.dat
    with open(PIK,"wb") as f:
        pickle.dump(kb.data,f)


# Loads everything from pickle.dat
def load_all(filename):
    try:
        with open(filename, "rb") as f: # Loads file
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
    except OSError:# Error if there is no pickle file. 
        save_all() # Creates the file
        with open(filename, "rb") as f:# Loads from the file after created 
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break



