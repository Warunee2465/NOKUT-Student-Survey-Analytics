#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd


# In[69]:


pd.__version__


# In[70]:


import xlrd 


# In[71]:


kb_2018 = pd.read_excel ('2018_kodebook_description.xlsx')


# In[72]:


kb_2019 = pd.read_excel ('2019_kodebook_description.xlsx')


# In[73]:


kb_2020 = pd.read_excel ('2020_kodebook_description.xlsx')


# In[74]:


ds_2018 = pd.read_excel ('Programdata_SB2018.xls')


# In[75]:


ds_2019 = pd.read_excel ('Programdata_SB2019.xls')


# In[76]:


ds_2020 = pd.read_excel ('Programdata_SB2020.xls')


# In[77]:


ds_2018.dtypes


# In[78]:


ds_2019.dtypes


# In[79]:


ds_2020.dtypes


# In[80]:


ds_2018_col = list(ds_2018.columns)
ds_2019_col = list(ds_2019.columns)
ds_2020_col = list(ds_2020.columns)


# In[81]:


bakgrunnsdata_2018_col = ds_2018_col[:41]
bakgrunnsdata_2019_col = ds_2019_col[:43]
bakgrunnsdata_2020_col = ds_2020_col[:43]


# In[82]:


#checking for background data
print('\n','not common between 2018-2019',len(bakgrunnsdata_2018_col),len(bakgrunnsdata_2019_col),len(set(bakgrunnsdata_2018_col) & set(bakgrunnsdata_2019_col)),set(bakgrunnsdata_2018_col) ^ set(bakgrunnsdata_2019_col))

print('\n','not common between 2018-2020',len(bakgrunnsdata_2018_col),len(bakgrunnsdata_2020_col),len(set(bakgrunnsdata_2018_col) & set(bakgrunnsdata_2020_col)),set(bakgrunnsdata_2018_col) ^ set(bakgrunnsdata_2020_col))

print('\n','not common between 2019-2020',len(bakgrunnsdata_2019_col),len(bakgrunnsdata_2020_col),len(set(bakgrunnsdata_2019_col) & set(bakgrunnsdata_2020_col)),set(bakgrunnsdata_2019_col) ^ set(bakgrunnsdata_2020_col))



# we do not need to use these columns that are not common in three table and we delet thes columns in the next steps.

# In[83]:


#checking for questions
question_2018_col = ds_2018_col[41:]
question_2019_col = ds_2019_col[43:]
question_2020_col = ds_2020_col[43:]


# In[84]:


print('\n','not common between 2018-2019',len(question_2018_col),len(question_2019_col),len(set(question_2018_col) & set(question_2019_col)),set(question_2018_col) ^ set(question_2019_col))

print('\n','not common between 2018-2020',len(bakgrunnsdata_2018_col),len(question_2020_col),len(set(question_2018_col) & set(question_2020_col)),set(question_2018_col) ^ set(question_2020_col))

print('\n','not common between 2019-2020',len(bakgrunnsdata_2019_col),len(question_2020_col),len(set(question_2019_col) & set(question_2020_col)),set(question_2019_col) ^ set(question_2020_col))



# In[85]:


#checking for duplicates in datasets
print("Is 'ID' column unique in 2018:", ds_2018['identifikator'].nunique() == len(ds_2018['identifikator']))
print("Is 'ID' column unique in 2019:", ds_2019['identifikator'].nunique() == len(ds_2019['identifikator']))
print("Is 'ID' column unique in 2020:", ds_2020['identifikator'].nunique() == len(ds_2020['identifikator']))

print("duplicated cell in 2019 is", ds_2019[ds_2019.duplicated(subset=['identifikator'], keep=False)]['identifikator'].unique())


# In[86]:


#adding year to each dataset
ds_2018.insert(2, 'Year', 2018) 
ds_2019.insert(2, 'Year', 2019) 
ds_2020.insert(2, 'Year', 2020) 


# In[87]:


#merging dataset
combine_ds = pd.concat([ds_2018, ds_2019, ds_2020],axis=0)
combine_ds


# In[88]:


#deleting unnessessary columns
columns_to_drop = [  
'studiepgm_navn_en','instnr','instnavn_en',
'NUSKODE','fagfelt_nyn','fagfelt_eng',
'faggruppe_nyn','faggruppe_eng','utdanningsgruppe_nyn',
'utdanningsgruppe_eng',
'fagfelt_bama',
'studprog_kod',
'STUDIENIVAKODE',
'utd_type',
'utd_gruppe',
'an_heltd_DBH',
'stupoeng_DBH',
'organis_DBH',
'pc_praksDBH',
'undsprakDBH',
'vidutd_DBH',
'aldmedian_DBH',
'aggregerte_data',
'oppr_utvalg',
'end_utvalg',
'andel_svart',
'terskel',
]
combine_ds.drop(columns=columns_to_drop, inplace=True)


# In[90]:


combine_ds.to_csv('combine_ds.csv',sep=';')


# In[ ]:


#JUST FOR CHECKING
cleaned_ds['instnavn'].isna().sum()


# In[ ]:


cleaned_ds['studiested'].isna().sum()


# In[ ]:


cleaned_ds['fagfelt'].isna().sum()


# In[ ]:


cleaned_ds['faggruppe'].isna().sum()


# In[ ]:


cleaned_ds['utdanningsgruppe'].isna().sum()


# In[ ]:


cleaned_ds['bama'].isna().sum()


# In[ ]:


cleaned_ds['utd_type'].isna().sum()


# In[ ]:


cleaned_ds['utd_gruppe'].isna().sum()

