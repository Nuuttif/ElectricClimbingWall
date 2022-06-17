# TODO:
#   Implement this class
#   Should handle communication between BoulderDataHandler and Grid
#   BoulderDataHandler serializes and loads boulders
#   GridHandler fetches boulders from BoulderDataHandler and sets the state of Grid
class GridHandler:
    # @doc
    # @var Class Grid
    def __init__(self, grid):
        self.grid = grid

    def setBoulder(self):
        self.grid.setLights(self.grid)
