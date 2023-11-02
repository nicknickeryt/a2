from enum import Enum

class props(Enum):
    RADIUS = "promień [m]"
    SEMIAXIS = "półoś [m] (półoś>promień)"
    SIDE = "długość boku [m]"
    SIDEA = "długość boku A [m]"
    SIDEB = "długość boku B [m]"
    HEIGHT = "wysokość [m]"
    DENSITY = "gestość [kg/m³]"

class reqs(Enum):
    AREA = "powierzchnia [m²]"
    MASS = "masa [kg]"
    VOLUME = "objetość [m³]"
