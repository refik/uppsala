import sys
import os
import shutil
import random

os.system('find . mp3 > input')
if os.path.isdir('output'):
	shutil.rmtree('output')
os.mkdir('output')
songs = open('input').readlines()
for i in range(int(sys.argv[1])):
	shutil.copy(songs[random.randrange(0,len(songs))].replace('\n',''),'output')
os.system('tar -jcvf output%i.tar.bz2 output'%(random.randrange(0,30)))
