
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[48]:


def get_repo(url):
    response = requests.get(url)
    html_content = response.content
    dom = BeautifulSoup(html_content,'html.parser')
    repos = dom.select("h3.wb-break-all")
    rep_list = []
    for each in repos:
        href_link = each.a.attrs["href"]
        name = href_link[1:]
        repo={"label":name,"link":url+href_link}
        rep_list.append(repo)
    return rep_list

