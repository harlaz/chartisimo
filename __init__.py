import pandas as pd
import chartpatterns as cp
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame().from_csv("data/sample-prices.csv")
patterns = cp.get_definitions()
patternDF = cp.apply_patterns(df, patterns)
print( patternDF )