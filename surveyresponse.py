# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%

month = pd.read_excel("survey resp.xlsx", sheet_name="monthlypay", header=0)
commpref = pd.read_excel("survey resp.xlsx", sheet_name="extranocom", header=0)
whichserv = pd.read_excel("survey resp.xlsx", sheet_name="which", header=0)
allresp = pd.read_excel("survey resp.xlsx", sheet_name="all", header=0)
importance = pd.read_excel("survey resp.xlsx", sheet_name="important", header=0)
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
