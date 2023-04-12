import os
import pandas as pd

# awk - F ',' - v OFS = "," '{print $5}' ~ / Downloads / data / AAP.csv >../ data / AAP.csv
filename = "_SP500"
if ".csv" in filename:
    filename = filename.strip(".csv")
raw_data = pd.read_csv(os.path.join("..", "data", filename + ".csv"))
outputPath = os.path.join("..", "data", filename + "_bin.csv")
#print(raw_data)
# max_value_of_col = raw_data.loc[raw_data[raw_data.columns[-1]].idxmax()]
# print(max_value_of_col[-1])
# fifty_percent_of_max_value = 0.5*max_value_of_col[-1]
# print(fifty_percent_of_max_value)
sellValue = [1 if raw_data[raw_data.columns[-1]][x] >= raw_data[raw_data.columns[-1]][x+1]
              else -1
              for x in range(0,len(raw_data[raw_data.columns[-1]])-1)]
sellValue.append(0)
raw_data["ClassificationValue"] = sellValue
print(raw_data)
raw_data.to_csv(outputPath, index=False)