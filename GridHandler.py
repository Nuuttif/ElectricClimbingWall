from Grid import Grid
from BoulderDataHandler import BoulderDataHandler
# TODO:
#   Implement this class
#   Should handle communication between BoulderDataHandler and Grid
#   BoulderDataHandler serializes and loads boulders
#   GridHandler fetches boulders from BoulderDataHandler and sets the state of Grid


class GridHandler:

    # @doc
    # @var Class Grid
    def __init__(self):
        self.grid = Grid()
        self.boulderDataHandler = BoulderDataHandler()

        # @doc
        # @var List [] -> Class Grid
        self.boulders = []

    def setBoulder(self):
        self.grid.setLights(self.grid)


    # TODO:
    #   Add functions to call BoulderDataHandel for:
    #   - Saving a new boulder
    def loadBoulders(self):
        boulders = self.boulderDataHandler.deSerializeBoulders()
        if boulders:
            self.boulders = boulders

    # TODO:
    #   Add a function for selecting a boulder from list of grids