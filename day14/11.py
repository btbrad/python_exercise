import pickle

with open(r"./data.dat", "wb") as f:
    d = dict(name="bt", age=18, score=[10, 20, 30])
    pickle.dump(d, f)

with open(r"./data.dat", "rb") as f:
    s = pickle.load(f)
    print(s)