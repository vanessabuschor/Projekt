#Diese Program holt einen Text aus dem Internet

import urllib2
from bs4 import BeautifulSoup


#function to fetch data
def fetch_data(url):
 #get html from http://australienblog.com/
    response = urllib2.urlopen(url)
    html = response.read()
    return clean_code(html)



#function to get rid of html code etc
def clean_code(html):
 #clean up text
    soup = BeautifulSoup(html, 'html.parser')
    clean_soup = (soup.get_text())
    #cut text to only the story
    start_index = clean_soup.find("Australien ist")
    end_index = clean_soup.find("sei dahingestellt")
    story = clean_soup[int(start_index):int(end_index)]
    return story