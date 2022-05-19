import numpy as np
import pandas as pd
import scipy.integrate
from dash import Dash, Input, Output, dcc, html
import dash_bootstrap_components as dash_bs
import plotly.express as px

time_sampling_rate = 10

class SimulationViewer:
    def __init__(self, simulation_func, variable_list, species_list):
        self.func = simulation_func
        self.app = Dash(__name__, external_stylesheets=[dash_bs.themes.BOOTSTRAP])
        self.setup_layout(variable_list, species_list)
        self.setup_callbacks(variable_list, species_list)
        self.setup_plotting(species_list)

    def run(self):
        self.app.run_server(debug=True)

    def setup_layout(self, variable_list, species_list):
        control_list = []
        for var_name, var_start, var_max in variable_list + species_list:
            control_list.append(html.Label(var_name))
            control_list.append(
                html.Div(
                    dcc.Slider(
                        id="{}-slider".format(var_name),
                        min=0,
                        max=var_max,
                        value=var_start,
                    )
                )
            )
        self.app.layout = dash_bs.Container(
            dash_bs.Row(
                [
                    dash_bs.Col([dcc.Graph(id='output-graph')], lg=9),
                    dash_bs.Col(
                        html.Div(
                            control_list,
                            className="card-body"
                        ),
                        className="card bg-default",
                        lg=3,
                    )
                ]
            )
        )

    def setup_plotting(self, species_list):
        self.species_names = [entry[0] for entry in species_list]

    def setup_callbacks(self, variable_list, species_list):
        callback_args = [Output("output-graph", "figure")]
        for var_name, var_start, var_max in species_list + variable_list:
            callback_args.append(Input("{}-slider".format(var_name), "value"))
        self.app.callback(*callback_args)(self.update_figures)

    def update_figures(self, *args):
        arg_list = list(args)
        start_state = [arg_list.pop(0) for species in self.species_names]
        max_time = arg_list.pop(0)
        solution = scipy.integrate.solve_ivp(
            self.func,
            [0, max_time],
            start_state,
            args=arg_list,
            dense_output=True
        )
        t = np.linspace(0, max_time, int(max_time * time_sampling_rate))
        X = solution.sol(t)
        df = pd.DataFrame.from_dict(
            {
                "t": np.tile(t, X.shape[0]),
                "number": X.flatten(),
                "species": np.repeat(self.species_names, X.shape[1])
            }
        )
        fig = px.line(df, x="t", y="number", color="species")
        return fig
