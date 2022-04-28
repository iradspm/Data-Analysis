
import pandas as pd

data = pd.read_csv('Education_attainment.csv', na_values = '---')
data.rename(columns={'Total':'Percentage'},inplace=True)
data = data[data['Year'] == 1980] #select 1980
data = data[data['Min degree'] == "bachelor's"]
data = data[data['Sex'] != 'A']
data = data[['Sex', 'Percentage']]
print(pd.DataFrame(data))