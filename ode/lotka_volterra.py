import scipy.integrate
import numpy as np
import pandas as pd
from simulation_viewer import SimulationViewer

def lotka_volterra(t, X, alpha, beta, delta, gamma):
    prey, predator = X
    return(
        [
            (alpha * prey) - (beta * prey * predator),
            (delta * prey * predator) - (gamma * predator)
        ]
    )

if __name__ == "__main__":
    variables = [
        ("max_time", 10, 50),
        ("alpha", 1, 3),
        ("beta", 1, 3),
        ("delta", 1, 3),
        ("gamma", 1, 3),
    ]

    species = [
        ("prey", 20, 100),
        ("predator", 2, 100),
    ]

    app = SimulationViewer(lotka_volterra, variables, species)
    app.run()
