#!/usr/bin/python
import os

path = os.path.abspath('media/radio_channel/config')
os.system('sed \'s|radiopath|%s|\' settings_base > new.py'%(path))
path = os.path.abspath('media/radio_channel')
os.system('sed \'s|musicpath|%s|\' new.py > new1.py'%(path))
path = os.path.abspath('sql.db')
os.system('sed \'s|sqlpath|%s|\' new1.py > settings.py'%(path))
os.system('rm new*')
