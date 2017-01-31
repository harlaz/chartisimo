import pandas as pd
import numpy as np


def get_open_plus_5(df):
    return df["Open"] + 5


def swing(df):
    return df["High"] - df["Low"]


# def sma(data, window):
#     weights = np.repeat([1.0], window) / window
#     return np.convolve(data, weights, "valid")


def get_definitions():
    definitions = [
        {
            "name": "open5",
            "function": get_open_plus_5
        },
        {
            "name": "swing",
            "function": swing
        }
    ]
    return definitions


def _apply_definition(df, definition):
    name = definition["name"]
    function = definition["function"]
    df[name] = df.apply(function, axis=1)
    return df


def apply_patterns(df, definitions):
    for d in definitions:
        df = _apply_definition(df, d)
    return df
