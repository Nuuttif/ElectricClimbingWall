import pickle
import Board

class BoulderDataHandler:
    def __init__(self):
        pass

    def deSerializeBoulders(self):
        with open("boulders.pickle", "rb") as infile:
            return pickle.load(infile)

    # @doc
    # var List [] -> Class Board
    def serializeBoulders(self, boards):
        with open("boulders.pickle", "wb") as outfile:
            pickle.dump(boards, outfile)
