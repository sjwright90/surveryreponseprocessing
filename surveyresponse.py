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
allresp["services"]=allresp.services.str.split(",")
allresp = allresp.explode(column = "services")
allresp["services"] = allresp.services.str.lower()
allresp["services"] = allresp.services.str.strip()
# %%
orig = allresp.services.unique()
repl = ["hulu", "netflix", "hbo", "primevideo", "disney",\
    "youtube", "peacock", "netflix","box","appletv", "dis",
    "peacock", "fubo", "youtube","paramount","starz","hbo", "none"]

repldict = dict(zip(orig, repl))
# %%
allresp["services"] = allresp.services.replace(repldict)
# %%
allresp.groupby("services")["Age"].value_counts()
# %%
ageservice = allresp[["agebins","services"]]
# %%
servicegroup = allresp.groupby("services")["agebins"]
# %%
sns.histplot(ageservice.value_counts())
# %%
