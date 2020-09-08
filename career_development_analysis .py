#!/usr/bin/env python
# coding: utf-8

# In[96]:


data = pd.read_excel("d:/downloads/Career Development Survey for Individuals (Responses).xlsx")
data_2=data.copy()
data_2.head()
data_2.columns = ["timestamp","name","email","domain","satisfaction","challenges","what_challenges",
                  "pursuing_course","importance","motivation_factor","skills_looking_for","approval",
                  "frequency_of_pursue","mode","prefer_councelor","personnalised","duration"]
data_2.head()
cat_data = data_2[["domain","satisfaction","importance","pursuing_course","prefer_councelor","approval",
                          "personnalised"]]


# In[3]:


data_2["new"] = data_2["what_challenges"].str.split(",",expand=False)
data_2
frequency = {}
for i in data_2["new"]:
    for j in i:
        if j in frequency:
            frequency[j] = frequency[j]+1
        else:
            frequency[j] = 1


# In[52]:



value = list(d.values())
index = list(d.keys())
for i in range(6):
    value.pop()
    index.pop()
sns.set_style("white")
axes = sns.barplot(value,index,palette="rocket")
#sns.set_context("talk")
sns.plotting_context("notebook",font_scale=1.5)
axes.set(xlabel='Number of student opted', ylabel="worried about")

plt.title("Problems")
sns.despine()
plt.show()


# In[51]:


# sum of the top motivation factors choosen by students
data_2["m_factor"] = data_2["motivation_factor"].str.split(",",expand=False)
data_2
frequency_m = {}
for i in data_2["m_factor"]:
    for j in i:
        if j in frequency_m:
            frequency_m[j] = frequency_m[j]+1
        else:
            frequency_m[j] = 1
frequency_m = sorted(frequency_m.items(), key=lambda item: item[1],reverse = True)
d={}
for i in frequency_m:
    d[i[0]] = i[1]
value = list(d.values())
value = value[0:5]
index = list(d.keys())
index = index[0:5]
sns.set_style("white")
axes = sns.barplot(value,index,palette="rocket")
sns.set_context("talk")
sns.plotting_context("notebook",font_scale=1.5)
axes.set(xlabel='Number of students opted', ylabel="w")

plt.title("Reasons for pursuning carrier development courses")
sns.despine()
plt.show()
    


# In[7]:


# domain wise analysis
data_2["domain"] = data_2["domain"].str.strip()
data_2["domain"] = data_2["domain"].str.lower()
data_2["domain"].value_counts()
marketing_data = data_2[data_2["domain"]=="marketing"]


# In[8]:


import plotly.express as px
import plotly.graph_objects as go
marketing_data["duration"].value_counts()
value = marketing_data["duration"].value_counts().values
index = marketing_data["duration"].value_counts().index
colors = px.colors.sequential.RdBu
fig = go.Figure(data=[go.Pie(labels=index, values=value, 
                             pull=[0, 0.1, 0, 0,0],insidetextorientation='radial')])
fig.update_traces(textposition='inside', textinfo='percent+label',marker = dict(colors = colors))
fig.update_layout(title_text="Choice of Course duration in marketing students")
fig.show()


# In[9]:



value = marketing_data["satisfaction"].value_counts().values
index = marketing_data["satisfaction"].value_counts().index
colors = px.colors.sequential.RdBu
fig = go.Figure(data=[go.Pie(labels=["satisfied","Not satisfied","very satisfied"], values=value, 
                             pull=[0, 0.1, 0, 0,0],insidetextorientation='radial')])
fig.update_traces(textposition='inside', textinfo='percent+label',marker = dict(colors = colors))
fig.update_layout(title_text="Satisfaction level among marketing students")
fig.show()


# In[94]:


#domain wise satisfaction level
data_3 = data_2[(data_2["domain"]=="marketing")|(data_2["domain"]=="finance")|(data_2["domain"]=="it")]
total = float(len(data_3))
g= sns.countplot(x="approval", hue="domain", data=data_3, palette="rocket")
sns.set_context("talk")
sns.plotting_context("notebook",font_scale=1.5)
g.set(xlabel='', ylabel="Number of students")
plt.title("Willingness to opt for courses")

plt.legend()
sns.despine()
plt.show()


# In[23]:


cat_data = data_2[["domain","satisfaction","importance","pursuing_course","prefer_councelor","approval",
                          "personnalised"]]
cat_data = cat_data[(data_2["domain"]=="marketing")|(cat_data["domain"]=="finance")|(cat_data["domain"]=="it")]
cat_data.head()
cr=pd.crosstab(cat_data["domain"],cat_data["personnalised"])
print(cr)
    


# In[ ]:


# graphs 


# In[37]:


value = [31,3,23,2,11,30]
index =["Byju's","Great learning","Unacademy","Toppr","Upgrad","Others"]
colors = px.colors.sequential.RdBu
colors = ['rgb(103,0,31)',
 'rgb(178,24,43)',
 'rgb(214,96,77)',
 'rgb(244,165,130)',
 'rgb(253,219,199)',
 'rgb(5,48,97)']
fig = go.Figure(data=[go.Pie(labels=index, values=value, 
                             pull=[0.1, 0, 0, 0,0,0],insidetextorientation='radial')])
fig.update_traces(textposition='inside', textinfo='percent+label',marker = dict(colors = colors))
fig.update_layout(title_text="Market share")
fig.show()


# In[ ]:





# In[93]:


value = data_2["prefer_councelor"].value_counts().values
index =data_2["prefer_councelor"].value_counts().index
colors = px.colors.sequential.RdBu
fig = go.Figure(data=[go.Pie(labels=index, values=value, 
                             pull=[0, 0, 0, 0,0,0],insidetextorientation='radial')])
fig.update_traces(textposition='inside', textinfo='percent+label',marker = dict(colors = colors))
fig.update_layout(title_text="Will you prefer counsellor?")
fig.show()


# In[ ]:





# In[92]:


data_2["new"] = data_2["skills_looking_for"].str.split(",",expand=False)
data_2
frequency = {}
for i in data_2["new"]:
    for j in i:
        if j in frequency:
            frequency[j] = frequency[j]+1
        else:
            frequency[j] = 1
frequency = sorted(frequency.items(), key=lambda item: item[1],reverse = True)
d={}
for i in frequency:
    d[i[0]] = i[1]


# # skills graph

# In[56]:


value = list(d.values())
index = list(d.keys())
for i in range(6):
    value.pop()
    index.pop()
sns.set_style("white")
axes = sns.barplot(value,index,palette="rocket")
#sns.set_context("talk")
sns.plotting_context("notebook",font_scale=1.5)
axes.set(xlabel='Number of student opted', ylabel="skills")

plt.title("Skills on which institute need to work on")
sns.despine()
plt.show()


# # checking co-relation between variables
# 
# 
# 
# 

# 
# # checking co-relation with chi_2 test

# In[87]:


import scipy.stats as stats
vector = cat_data.columns
z = []
for i in vector:
    k = []
    for j in vector:
        cr=pd.crosstab(cat_data[i],cat_data[j])
        m = stats.chi2_contingency(cr)[1]
        k.append(m)
    z.append(k)
labels = ["Domain","Satisfaction","How important","Pursuing course",
          "Will prefer counsellor","Interested in new course","Personnalised"]
p_value = pd.DataFrame(z,index=labels,columns=labels)
p_value = p_value.round(3)


# # P-value table

# In[90]:


p_value


# # showing co-relation on heatmaps

# In[91]:


sns.heatmap(p_value,annot=True)
plt.show()

