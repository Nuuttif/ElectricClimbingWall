import pickle

class BoulderDataHandler:
    def __init__(self):
        pass

    def deSerializeBoulders(self):
        with open("boulders.pickle", "rb") as infile:
            return pickle.load(infile)

    # @doc
    # var List [] -> Class Grid
    def serializeBoulders(self, grids):
        with open("boulders.pickle", "wb") as outfile:
            pickle.dump(grids, outfile)
