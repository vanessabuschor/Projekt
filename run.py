'''
Created on June 2, 2018
@author: vanessa
'''
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()

mc.add_file('songtexte.txt')

lyric = mc.generate_text()
lyric = ' '.join(lyric)

