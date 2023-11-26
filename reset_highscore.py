import pickle

data = {"highscore": 0}

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)
print("Done!")
input("Press Enter to continue...")
