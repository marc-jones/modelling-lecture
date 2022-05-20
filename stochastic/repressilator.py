import scipy.integrate
import numpy as np
import pandas as pd
from simulation_viewer import SimulationViewer

def repressilator(X, alpha, beta, alpha_zero, n):
    laci_mrna, laci_protein, tetr_mrna, tetr_protein, ci_mrna, ci_protein = X
    rates = [
        alpha_zero + (alpha / (1 + ci_protein**n)),
        laci_mrna,
        laci_mrna*beta,
        laci_protein*beta,
        alpha_zero + (alpha / (1 + laci_protein**n)),
        tetr_mrna,
        tetr_mrna*beta,
        tetr_protein*beta,
        alpha_zero + (alpha / (1 + tetr_protein**n)),
        ci_mrna,
        ci_mrna*beta,
        ci_protein*beta,
    ]
    movements = [
        [ 1,  0,  0,  0,  0,  0],
        [-1,  0,  0,  0,  0,  0],
        [ 0,  1,  0,  0,  0,  0],
        [ 0, -1,  0,  0,  0,  0],
        [ 0,  0,  1,  0,  0,  0],
        [ 0,  0, -1,  0,  0,  0],
        [ 0,  0,  0,  1,  0,  0],
        [ 0,  0,  0, -1,  0,  0],
        [ 0,  0,  0,  0,  1,  0],
        [ 0,  0,  0,  0, -1,  0],
        [ 0,  0,  0,  0,  0,  1],
        [ 0,  0,  0,  0,  0, -1],
    ]
    return(rates, movements)


if __name__ == "__main__":
    variables = [
        ("max_time", 10, 200),
        ("alpha", 200, 500),
        ("beta", 0.2, 1),
        ("alpha_zero", 0.2, 1),
        ("n", 2, 10),
    ]

    species = [
        ("laci_mrna", 0.1, 1),
        ("laci_protein", 0.1, 1),
        ("tetr_mrna", 0, 1),
        ("tetr_protein", 0, 1),
        ("ci_mrna", 0, 1),
        ("ci_protein", 0, 1),
    ]

    app = SimulationViewer(repressilator, variables, species)
    app.run()
