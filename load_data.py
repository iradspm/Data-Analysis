import pandas as pd
data=pd.read_csv("Education_attainment.csv", na_values="---") #replace '---' with NAN
data.head(10)