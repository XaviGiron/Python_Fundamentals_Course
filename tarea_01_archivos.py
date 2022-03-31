import pandas as pd
import numpy as np
import csv
datos = pd.read_csv("athlete_events.csv")


print("Medallista de oro más jóven")
datos["Age"].min() and datos[datos["Medal"] == "Gold"]
print("Medallista de oro más mayor")
datos["Age"].max() and datos[datos["Medal"] == "Gold"]
