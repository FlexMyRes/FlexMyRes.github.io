
# coding: utf-8

# In[309]:


import PyPDF2
from github import Github
from io import StringIO
import pandas as pd
import spacy
import numpy as np
from collections import Counter
import en_core_web_sm
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import PhraseMatcher
from spacy.matcher import Matcher
from spacy.tokens import Doc
from collections import OrderedDict
import seaborn as sns
#initialize matcher
matcher = Matcher(nlp.vocab)


# In[297]:


#reads into list after applying nlp to each word
def read_pdf(fileName):
        f = PyPDF2.PdfFileReader(fileName)
        f2=f.getPage(0)
        text = str(f2.extractText()).replace('\n',' ')
        return text

#reads txt files
def read_txt(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().replace("\n", " ") #puts the file into an array
    fileObj.close()
    return words


# In[299]:


def extract_name(resume_text):
    nlp_text = nlp(resume_text)
    
    # First name and Last name are always Proper Nouns
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    
    matcher.add('NAME', None, pattern)
    
    matches = matcher(nlp_text)
    
    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text


# In[300]:


def extract_skills2(resume_text):
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    data = pd.read_csv("skills.csv") 
    
    
    # extract values
    skills = list(data.columns.values)
    
    hard_data = nlp(read_txt('hard.txt'))
    hard_tokens = [token.text for token in hard_data]
    hard_skills=[]
    
    soft_data = nlp(read_txt('soft.txt'))
    soft_tokens = [token.text for token in soft_data]
    soft_skills=[]
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in hard_data:
        for token2 in nlp_text.noun_chunks:
            if token.similarity(token2)>0.8:
                hard_skills.append(token)
                
    for token in soft_data:
        for token2 in nlp_text.noun_chunks:
            if token.similarity(token2)>0.7:
                soft_skills.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    return hard_skills,soft_skills


# In[301]:


def graph_hardsoft(hard,soft):
    hard_skills = pd.DataFrame(hard)
    soft_skills = pd.DataFrame(soft)
    hard_skills[0] = hard_skills[0].astype(str).str.strip()
    soft_skills[0] = soft_skills[0].astype(str).str.strip()
    return hard_skills[0].value_counts(),soft_skills[0].value_counts()


# In[ ]:


#code to run in this order
## text=read_pdf(file)

#finding user name
## extract_name(text)

#get skills
##hard,soft = extract_skills2(text)

#get values to plot 
## hard_set,soft_set=graph_hardsoft(hard,soft)

##TYPE THIS IN MANUALLY-- NOT A FUNCTION
### code to run manually to graph the above responses
#hard_plot = hard_skills[0].value_counts().plot.pie(subplots=True)
#soft_plot = soft_skills[0].value_counts().plot(kind='bar')

