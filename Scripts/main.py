import csv
import pandas as pd


df = pd.read_csv("SPARCS2014_test.csv", index_col = None, header = 0, low_memory = False)
df[0]
