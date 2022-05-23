import scipy.integrate
import numpy as np
import pandas as pd
from simulation_viewer import SimulationViewer

def lotka_volterra(X, alpha, beta, delta, gamma):
    prey, predator = X
    rates = [
        prey*alpha,
        prey*predator*beta,
        prey*predator*delta,
        predator*gamma
    ]
    movements = [
        [ 1,  0],
        [-1,  0],
        [ 0,  1],
        [ 0, -1]
    ]
    return(rates, movements)

if __name__ == "__main__":
    variables = [
        ("max_time", 10, 50),
        ("alpha", 1, 10),
        ("beta", 1, 1),
        ("delta", 1, 1),
        ("gamma", 1, 10),
    ]

    species = [
        ("prey", 20, 100),
        ("predator", 2, 100),
    ]

    app = SimulationViewer(lotka_volterra, variables, species)
    app.run()
