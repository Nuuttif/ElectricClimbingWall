# ElectricClimbingWall 

## Description:
Goal is to build:

Software for Moonboard style, led powered, electric climbing wall. 

Leds are light up to visualize boulders on a climbing wall. 

User can set, browse and light up boulders from a GUI.

## Architecture: 
### [BoulderDataHandler](BoulderDataHandler.py)
- Serializes and loads boulders from/to file.

### [GridHandler](GridHandler.py) 
- Handles the communication between BoulderDataHandler and Grid. 
- Boulders are loaded into a list.
- This class sets the state of the Grid.

### [Grid](Grid.py)
- Defines the state of the board -> which leds are light up.
- Sends state to LedHandler, which is the lowest level class communicating with leds.

### [LedHandler](LedHandler.py)
- Sets the led-lights. 
- Called by Grid.

```mermaid
graph TD

A[User] -->|Interact| B[UI]

B[UI] -->|Send command| C[GridHandler]

C -->|Fetch Boulders| D[BoulderDataHandler]
D -->|Return Boulders| C
C -->|Set Grid| E[Grid]
E -->|Call LedHandler| F[LedHandler]
F -->|Light up leds| G[Hardware]
```