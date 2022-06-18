from Board import Board
from BoulderDataHandler import BoulderDataHandler
# TODO:
#   Implement this class
#   Should handle communication between BoulderDataHandler and Board
#   BoulderDataHandler serializes and loads boulders
#   BoardHandler fetches boulders from BoulderDataHandler and sets the state of Board


class BoardHandler:

    # @doc
    # @var Class Board
    def __init__(self):
        self.board = Board()
        self.boulderDataHandler = BoulderDataHandler()

        # @doc
        # @var List [] -> Class Board
        self.boulders = []

    def setBoulder(self):
        self.board.setLights(self.board)


    # TODO:
    #   Add functions to call BoulderDataHandel for:
    #   - Saving a new boulder
    def loadBoulders(self):
        boulders = self.boulderDataHandler.deSerializeBoulders()
        if boulders:
            self.boulders = boulders

    # TODO:
    #   Add a function for selecting a boulder from list of boards