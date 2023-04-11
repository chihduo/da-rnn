import os
import pandas as pd

filename = "A1"
if ".csv" in filename:
    filename = filename.strip(".csv")
raw_data = pd.read_csv(os.path.join("..", "data", filename + ".csv"))
outputPath = os.path.join("..", "data", filename + "_bin.csv")
#print(raw_data)
max_value_of_col = raw_data.loc[raw_data[raw_data.columns[-1]].idxmax()]
print(max_value_of_col[-1])
fifty_percent_of_max_value = 0.5*max_value_of_col[-1]
print(fifty_percent_of_max_value)
sellValue = []
for x in  raw_data[raw_data.columns[-1]]:
    if x > fifty_percent_of_max_value:
        sellValue.append(1)
    else:
        sellValue.append(0)
raw_data["ClassificationValue"] = sellValue
print(raw_data)
raw_data.to_csv(outputPath)