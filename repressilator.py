import scipy.integrate
import numpy as np
import pandas as pd
from simulation_viewer import SimulationViewer

def repressilator(t, X, alpha, beta, alpha_zero, n):
    laci_mrna, laci_protein, tetr_mrna, tetr_protein, ci_mrna, ci_protein = X
    return(
        [
            (-laci_mrna) + (alpha / (1 + ci_protein**n)) + alpha_zero,   # lacI mRNA
            -beta * (laci_protein - laci_mrna),                          # lacI Protein
            (-tetr_mrna) + (alpha / (1 + laci_protein**n)) + alpha_zero, # tetR mRNA
            -beta * (tetr_protein - tetr_mrna),                          # tetR Protein
            (-ci_mrna) + (alpha / (1 + tetr_protein**n)) + alpha_zero,   # cI mRNA
            -beta * (ci_protein - ci_mrna),                              # cI Protein
        ]
    )

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
