import scipy.integrate
import numpy as np
import pandas as pd
from simulation_viewer import SimulationViewer

def mrna(X, k_prod, k_degr):
    mrna = X[0]
    rates = [
        k_prod,
        mrna*k_degr,
    ]
    movements = [
        [ 1],
        [-1],
    ]
    return(rates, movements)

if __name__ == "__main__":
    variables = [
        ("max_time", 10, 500),
        ("k_prod", 1, 10),
        ("k_degr", 1, 10),
    ]

    species = [
        ("mrna", 0, 0),
    ]

    app = SimulationViewer(mrna, variables, species)
    app.run()
