import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()


import numpy as np


from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

with open("./main.spice", 'r') as f:
    netlist_content = f.read()

circuit = Circuit(netlist_content)

print(circuit)
