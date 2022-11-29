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
importance = pd.read_excel("surveyresp.xlsx", sheet_name="important", header=1)
# %%
sns.histplot(data = importance, y=importance.iloc[:,1], stat="percent")
# %%
plt.barh(data=importance, y=importance.iloc[:,0],width=importance.iloc[:,1])
# %%
def str_cleaning(df,column):
    df[column] = df[column].str.lower()
    df[column] = df[column].str.strip()

def quick_countplt(df, group, xaxis = "agebins"):
    sns.countplot(data=df, x=xaxis, hue=group)
# %%
# clean all string data
for col in allresp.columns:
    if allresp[col].dtype == "O":
        str_cleaning(allresp,col)
# %%
# explode out services column into new dataframe
allresp["services"]=allresp.services.str.split(",")

# %%
allresp_ex = allresp.explode(column = "services")

# %%
# map services to correct identifiers
allresp_ex["services"] = allresp_ex.services.str.strip()
# %%
orig = allresp_ex.services.unique()
repl = ["hulu","netflix","HBO","prime video","disney+","youtube","peacock",\
    "netflix","box","apple","disney+","peacock","fubo","youtube","paramount",
    "starz","HBO","none"]
# %%
repldict = dict(zip(orig, repl))

allresp_ex["services"] = allresp_ex.services.replace(repldict)
# %%
# make age bins for both dataframes
allresp_ex["agebins"] = pd.cut(allresp_ex.Age, bins = [0,25,35,45,100],
                            labels=["under 25","26-35","36-45",">46"])
allresp["agebins"] = pd.cut(allresp.Age, bins = [0,25,35,45,100],
                            labels=["under 25","26-35","36-45",">46"])
# %%
# filter out services to exclude services with low subscription
filt = allresp_ex[allresp_ex.services.isin(['netflix',\
    'disney+', 'hulu', 'prime video', 'HBO'])]

# %%
# plot services histogram
fig1,ax1 = plt.subplots()
sns.countplot(data = filt,x = "agebins",
              hue = "services", palette="Set2", ax = ax1)
ax1.set_title("Customer subscriptions by age")
ax1.set_ylabel("Count")
ax1.set_xlabel("Age Groups")
ax1.legend(loc="upper right",frameon=False,
            labels=list(map(lambda x: x.title(), filt.services.unique())))
fig1.show()
fig1.savefig("servicesbyuserage.png", dpi=300)
# %%
fig2,ax2 = plt.subplots()
sns.countplot(data = allresp, x="agebins",hue="mostpay",
              hue_order=["<10","10 to 15",">15"],palette="Set2", ax=ax2)
ax2.set_title("Monthly amount customers are willing to\npay for streaming services")
ax2.set_ylabel("Count")
ax2.set_xlabel("Age Groups")
ax2.legend(frameon=False, title="Cost per month in dollars")
fig2.savefig("willingtopaymonthly.png", dpi=300)
# %%
allresp["payextr"] = np.where(allresp.payextr.str.startswith("y"),"Yes","No")
# %%
fig3,ax3 = plt.subplots()
sns.countplot(data=allresp, x="agebins",hue="payextr",palette="Set2",ax=ax3)
ax3.set_title("Customer willingness to pay extra for\ncommercial free streaming")
ax3.set_ylabel("Count")
ax3.set_xlabel("Age Groups")
ax3.legend(frameon=False)
fig3.savefig("payextrafornocommercial.png",dpi=300)

# %%
important = allresp.Imp.unique()
replimp = ["No Commercials", "Up to Date Content", "Original Content", "Many Options"]
imprepld = dict(zip(important, replimp))
allresp["Imp"] = allresp.Imp.replace(imprepld)
# %%
fig4,ax4 = plt.subplots()
sns.countplot(data=allresp, x="agebins", hue="Imp",palette="Set2", ax=ax4)
ax4.set_title("Most important feature in streaming service")
ax4.set_ylabel("Count")
ax4.set_xlabel("Age Groups")
ax4.legend(loc="upper right",frameon=False)
fig4.savefig("customerpreferences.png", dpi=300)
# %%
