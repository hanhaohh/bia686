# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

url_get_count= "http://eutils.ncbi.nlm.nih.gov/entrez/eutils\
/esearch.fcgi?db=pubmed&retmax=10000&retmode=json&term=sleep+disorder+Caffeine"
url_id = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id="

# <codecell>

import urllib2
import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
dic = dict()
page = urllib2.urlopen(url_get_count).read()
dic = eval(page.replace("\n",""))
ids = dic["esearchresult"]["idlist"]
records=[]

# <codecell>

for i in range(0,len(ids)/10):
    sep_ids = ",".join(ids[i*10:10*(i+1)])
    # print sep_ids+"*****"
    pg = urllib2.urlopen(url_id+sep_ids).read()
    e = ET.fromstring(pg)
    
    for elem in e.iter(tag='Article'):
		try:
			title = elem.find("ArticleTitle").text
		except:
			title = ""
			print "title error"
			
		try:
			pub_date =elem.find("Journal/JournalIssue/PubDate/Year").text
		except:
			print "date error"
			pub_date = ""
		
		authors = []
		for author in elem.iter(tag = "Author"):
			try:
				if author[0].text+" "+author[1].text:
					authors.append(author[0].text+" "+author[1].text)
			except:
				pass
		authors_string = "|".join(authors)
		print  (title,authors_string,pub_date)
		records.append([title,authors_string,pub_date])

# <codecell>

import pandas as pd 
data = pd.DataFrame(records)
data.rename(columns={0: 'Title', 1: 'Authors',2:'Year'},inplace=True)
data.dtypes

# <codecell>

import numpy as np
data['Year'].replace('', np.nan, inplace=True)
data['Authors'].replace('', np.nan, inplace=True)
data.dropna(inplace=True)

# <codecell>

def permu(arr):
    li = []
    for i in itertools.combinations(arr,2):
        li.append(i)
    return li

# <codecell>

import itertools
import sys 
reload(sys)
sys.setdefaultencoding("utf-8")
data["Year"] = data["Year"].apply(int)
data_2007 = data[data["Year"]>2007]
data_2007["Weight"] = data_2007["Year"] - 2008
print data_2007
w = data_2007["Authors"].str.split("|")
c = w.map(permu)
id_count = c.map(len)
weights = np.repeat(np.array(data_2007.Weight), id_count.values)
words = c.values
final_p1 = []
final_p2 = []
for i in words:
    for j in i:
        final_p1.append(j[0])
for i in words:
    for j in i:
        final_p2.append(j[1])    
target={"Target":final_p1,"Source":final_p2}
pd_print = pd.DataFrame(target)
pd_print["Weight"] = weights
pd_print
pd_print.to_csv("name.csv",encoding='utf-8', index_label=False, index= False)

# <codecell>


# <codecell>


# <codecell>


# <codecell>

range(0,10,1)

# <codecell>

a= "5"
b = int(a)
print b

# <codecell>


