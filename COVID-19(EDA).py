#!/usr/bin/env python
# coding: utf-8

# ## Coronavirus in India (Exploratory Data Analysis)

# In[8]:


import numpy as np 
import pandas as pd 
import os
from plotly import tools
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
init_notebook_mode(connected=True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)
import operator
import numpy
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from collections import Counter       
from datetime import datetime             
import os


# In[9]:


individual = pd.read_csv("IndividualDetails.csv")
s_testing= pd.read_csv("StatewiseTestingDetails.csv")
hospital = pd.read_csv("HospitalBedsIndia.csv")
india = pd.read_csv("covid_19_india.csv")
agegrp = pd.read_csv("AgeGroupDetails.csv")
testinglab = pd.read_csv("ICMRTestingLabs.csv")
census = pd.read_csv("population_india_census2011.csv")

print("data Shape:", individual.shape)


# In[14]:


state_hospital = hospital[hospital['State/UT']!="All India"]
top_20_u=state_hospital.nlargest(20,'NumUrbanHospitals_NHP18')
top_20_r=state_hospital.nlargest(20,'NumRuralHospitals_NHP18')


trace1 = go.Bar(x=top_20_u["NumUrbanHospitals_NHP18"], y=top_20_u['State/UT'], orientation='h', name="Urban Hospitals", marker=dict(color='yellow'))
trace2 = go.Bar(x=top_20_r["NumRuralHospitals_NHP18"], y=top_20_r['State/UT'], orientation='h', name="Rural Hospitals", marker=dict(color='blue'))
                                                                                                                       

data = [trace1,trace2]
layout = go.Layout(title="Urban and Rural Hospitals By States", legend=dict(x=0.1, y=1.1, orientation="h"),plot_bgcolor='rgba(0,0,0,0)')
fig = go.Figure(data, layout=layout)
fig.show()


# In[15]:


hospital = hospital.fillna(0)
state_hospital = hospital[hospital['State/UT']!="All India"]
ind=['NumUrbanBeds_NHP18', 'NumRuralBeds_NHP18', 'NumPublicBeds_HMIS']

fig = go.Figure(data=[
    go.Bar(name='Public Beds', x=state_hospital["State/UT"], y=state_hospital.NumPublicBeds_HMIS),
    go.Bar(name='Rural Beds', x=state_hospital["State/UT"], y=state_hospital.NumRuralBeds_NHP18),
    go.Bar(name='Urban Beds', x=state_hospital["State/UT"], y=state_hospital.NumUrbanBeds_NHP18)
    

])

fig.update_layout(
    height=500,
    showlegend=False,barmode='stack',
    title_text="Beds in Hospitals by States in india",
)
fig.show()


# In[19]:


ind=['NumUrbanBeds_NHP18', 'NumRuralBeds_NHP18', 'NumPublicBeds_HMIS']
trace = go.Pie(labels=ind, values=[431173,279588,739024], pull=[0.05, 0], marker=dict(colors=['blue','yellow','green']))
layout = go.Layout(title="Overall Beds available in India", height=400, legend=dict(x=1
                                                                                          , y=1.1))
fig = go.Figure(data = [trace], layout = layout)
iplot(fig)


# In[20]:


col = "type"
grouped = testinglab[col].value_counts().reset_index()
grouped = grouped.rename(columns = {col : "count", "index" : col})

## plot
trace = go.Pie(labels=grouped[col], values=grouped['count'],  hole=.3,pull=[0.05, 0], marker=dict(colors=['blue','yellow','green']))
layout = go.Layout(title="Types of Lab Testing Centers in India", height=400, legend=dict(x=1
                                                                                          , y=1.1))
fig = go.Figure(data = [trace], layout = layout)
iplot(fig)


# In[18]:


govlab= testinglab[testinglab['type']=="Government Laboratory"]
colsite = testinglab[testinglab['type']=="Collection Site"]
pvtlab = testinglab[testinglab['type']=="Private Laboratory"]

col = "state"

vc1 = govlab[col].value_counts().reset_index()
vc1 = vc1.rename(columns = {col : "count", "index" : col})
vc1['percent'] = vc1['count'].apply(lambda x : 100*x/sum(vc1['count']))

vc2 = colsite[col].value_counts().reset_index()
vc2 = vc2.rename(columns = {col : "count", "index" : col})
vc2['percent'] = vc2['count'].apply(lambda x : 100*x/sum(vc2['count']))

vc3 = pvtlab[col].value_counts().reset_index()
vc3 = vc3.rename(columns = {col : "count", "index" : col})
vc3['percent'] = vc3['count'].apply(lambda x : 100*x/sum(vc3['count']))

trace1 = go.Bar(x=vc1[col], y=vc1["count"], name="Government Laboratory", marker=dict(color='blue'))
trace3 = go.Bar(x=vc3[col], y=vc3["count"], name="Private Laboratory", marker=dict(color='yellow'))
data = [trace1,trace3]
layout = go.Layout(title="Test Centers by states", legend=dict(x=0.1, y=1.1, orientation="h"),plot_bgcolor='rgba(0,0,0,0)')
fig = go.Figure(data, layout=layout)
fig.show()


# In[25]:


fig = go.Figure(data=[go.Table(
    header=dict(values=list(["City","Address"]),
                fill_color='blue',
                align='left'),
    cells=dict(values=[pvtlab.city,pvtlab.lab],
               fill_color='white',
               align='left',line_color='darkslategray'))
])

fig.update_layout(
    height=400,
    showlegend=False,
    title_text="Private Testing Centers In India",
)
fig.show()


# In[26]:


fig = go.Figure(data=[go.Table(
    header=dict(values=list(["City","Address"]),
                fill_color='BLUE',
                align='left'),
    cells=dict(values=[govlab.city,govlab.lab],
               fill_color='white',
               align='left',line_color='darkslategray'))
])

fig.update_layout(
    height=400,
    showlegend=False,
    title_text="Government Testing Centers In India",
)
fig.show()


# In[ ]:




