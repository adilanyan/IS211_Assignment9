#!/usr/bin/env python
# coding: utf-8

# In[3]:


conda install -c anaconda urllib3 


# In[1]:


conda install -c anaconda beautifulsoup4


# In[8]:


from bs4 import BeautifulSoup
import urllib.request

URL = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2020-season-regular-category-touchdowns"

def football_stats():
    request = urllib.request.urlopen(URL)
    response = request.read()
    soup = BeautifulSoup(response, 'html.parser')
    data = soup.find_all(class_={'row1', 'row2'})[:20]
    stats = 'Player: {} -> Position: {} -> Team: {} -> Touchdowns: {}'
    for row in data:
        print(stats.format(row.contents[0].text, row.contents[1].text,
                           row.contents[2].text, row.contents[6].text))

if __name__ == '__main__':
    football_stats()


# In[ ]:




