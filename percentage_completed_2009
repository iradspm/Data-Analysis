import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("Education_attainment.csv", na_values="---") #replace '---' with NAN
data.rename(columns={'Total':'Percentage'},inplace=True)
#bar chart
#filter year 2009
filyer_year=data['Year']==2009
#filter minimum degree =high school
filter_degree=data['Min degree']=="high school"
percentage_completed = sns.barplot(x=data["Sex"], y=data["Percentage"], data=data.where(filyer_year&filter_degree, 
                                                                                        inplace=True))
plt.title("Percentage Completed High School by Sex")