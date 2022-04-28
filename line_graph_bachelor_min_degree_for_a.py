import pandas as pd
import seaborn as sns

data=pd.read_csv("Education_attainment.csv", na_values="---") #load data and replace '---' with NAN
data.rename(columns={'Total':'Percentage'},inplace=True) #rename 'Total' Column to 'Percentage'
filter_bachelor_degree=data['Min degree']=="bachelor's" #select bachelor's as min degree
filter_sex_a=data['Sex']=="A"
sns.lineplot(x=data["Year"], y=data["Percentage"],data=data.where(filter_bachelor_degree&filter_sex_a, inplace=True))