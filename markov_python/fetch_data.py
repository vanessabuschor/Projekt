'''
Created on June 2, 2018
@author: vanessa buschor
'''

import requests
from bs4 import BeautifulSoup


#list of URLs containing lyrics to Ed Sheeran songs
team_urls = ['http://www.lyricsfreak.com/e/evanescence/all+that+im+living+for_20502714.html',
            'http://www.lyricsfreak.com/e/evanescence/angel+of+mine_20502713.html',
            'http://www.lyricsfreak.com/e/evanescence/anything+for+you_10110713.html',
            'http://www.lyricsfreak.com/e/evanescence/anywhere_10110754.html',
            'http://www.lyricsfreak.com/e/evanescence/before+the+dawn_10110769.html',
            'http://www.lyricsfreak.com/e/evanescence/bleed_20502711.html',
            'http://www.lyricsfreak.com/e/evanescence/breathe+no+more_20051908.html',
            'http://www.lyricsfreak.com/e/evanescence/bring+me+to+life_10110669.html',
            'http://www.lyricsfreak.com/e/evanescence/broken_20502710.html',
            'http://www.lyricsfreak.com/e/evanescence/call+me+when+youre+sober_20502709.html',
            'http://www.lyricsfreak.com/e/evanescence/cartoon+network+song_20502708.html',
            'http://www.lyricsfreak.com/e/evanescence/cloud+nine_20502707.html'
]

found = ' '

#scrape lyrics from sites and compile them under one variable
for url in team_urls:
    page = requests.get(url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.select_one('#content_h')

    for e in soup.find_all('br'):
        e.replace_with('\n')
    found += div.text
    
# Save data in a file
string = ''
for word in found:
    string += word
    string = string.encode('ascii', 'ignore').decode('ascii')

# Open a file
f = open("songtexte.txt", "w")

f.write(string)

# Close open file
f.close()