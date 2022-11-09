# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%

month = pd.read_excel("surveyresp.xlsx", sheet_name="monthlypay", header=0)
commpref = pd.read_excel("surveyresp.xlsx", sheet_name="extranocom", header=0)
whichserv = pd.read_excel("surveyresp.xlsx", sheet_name="which", header=0)
allresp = pd.read_excel("surveyresp.xlsx", sheet_name="all", header=0)
importance = pd.read_excel("surveyresp.xlsx", sheet_name="important", header=0)
# %%
def str_cleaning(df,column):
    df[column] = df[column].str.lower()
    df[column] = df[column].str.strip()
# %%
for col in allresp.columns:
    if allresp[col].dtype == "O":
        str_cleaning(allresp,col)
# %%
allresp["services"]=allresp.services.str.split(",")
allresp_ex = allresp.explode(column = "services")

# %%
orig = allresp_ex.services.unique()
repl = ["hulu", "netflix", "hbo", "primevideo", "disney",\
    "youtube", "peacock", "netflix","box","appletv", "disney",
    "peacock", "fubo", "youtube","paramount","starz","hbo", "none"]

repldict = dict(zip(orig, repl))
# %%
allresp_ex["services"] = allresp_ex.services.replace(repldict)
# %%
allresp_ex["agebins"] = pd.cut(allresp_ex.Age, bins = [0,25,35,45,100],
                            labels=["under 25","26-35","36-45",">46"])
allresp["agebins"] = pd.cut(allresp.Age, bins = [0,25,35,45,100],
                            labels=["under 25","26-35","36-45",">46"])
# %%
filt = allresp_ex[allresp_ex.services.isin(['netflix',\
    'disney', 'hulu', 'primevideo', 'hbo'])]
sns.countplot(data = filt,\
   x = "agebins", hue = "services", palette="Set2")

# %%
def quick_countplt(df, group, xaxis = "agebins"):
    sns.countplot(data=df, x=xaxis, hue=group)

# %%
sns.countplot(data=allresp, x="agebins", hue="mostpay")
# %%
allresp["payextr"] = np.where(allresp.payextr.str.startswith("y"),"yes","no")
# %%
sns.countplot(data=allresp, x="agebins", hue="payextr")
# %%
important = allresp.Imp.unique()
replimp = ["no commercials", "up to date content", "original content", "many options"]
imprepld = dict(zip(important, replimp))
allresp["Imp"] = allresp.Imp.replace(imprepld)
# %%

# %%
