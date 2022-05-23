import scipy.integrate
import numpy as np
import pandas as pd
from simulation_viewer import SimulationViewer

def mrna(t, X, k_prod, k_degr):
    mrna = X
    return(
        [
            k_prod - mrna*k_degr
        ]
    )

if __name__ == "__main__":
    variables = [
        ("max_time", 10, 50),
        ("k_prod", 4, 10),
        ("k_degr", 1, 10),
    ]

    species = [
        ("mRNA", 0, 0),
    ]

    app = SimulationViewer(mrna, variables, species)
    app.run()
