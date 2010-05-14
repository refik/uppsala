#!/usr/bin/python
import os
import sys
import shutil
from uppsala.settings import RADIO_P, MUSIC_P

radio_p = RADIO_P
music_p = MUSIC_P

def stations():
	stations = os.listdir(music_p)
	stations.remove('config')
	return stations

def add(station,music):
	if music[-3:] == 'tar':
		os.system('tar -xf %s -C %s/%s' %(music, music_p, station))
	elif music[-3:] == 'zip':
		os.system('unzip -jo %s -d %s/%s' %(music, music_p, station))
	elif music[-3:] == 'bz2':
		os.system('tar -xvjf %s -C %s/%s' %(music, music_p, station))
	else:
		shutil.copy(music,'%s/%s'%(music_p,station))

	

def songs(station):
	songs = os.listdir('%s/%s' %(music_p, station))
	return songs


def restart(station):
	os.system('ps -e | grep icegenerator > %s/input'%(radio_p))
	f = open('%s/input' %(radio_p),'r')
	pids = f.readlines()
	for pid in pids:
		dead = int(pid.split()[0])
		os.kill(dead,9)
	s2bkilled = stations()
	for s in s2bkilled:
		os.system('icegenerator -f %s/%s'%(radio_p,s))

	
def new(station):
	os.system('mkdir %s/%s'%(music_p, station))
	os.system('sed s/first/%s/ %s/first > %s/%s'%(station, radio_p, radio_p, station))
	os.system('icegenerator -f %s/%s'%(radio_p, station))	

def main():
	if len(sys.argv) == 1:
		print 'usage: radio [OPTION]... [STATION] [MUSIC FILE]'
		print '	--new,      create a new station with specified name'
		print '	--restart,  restart the station for effects to take place'
                print '	--list,     list all the songs in a station'
		print '	--add,      add an mp3 file zip or tar archive to station (usa absolute path)'
		sys.exit(0)
	option = sys.argv[1]
	if option =='--stations':
		stations()
	elif option == '--restart':
		station = sys.argv[2]
		restart(station)
	elif option == '--new':
		station = sys.argv[2]
		new(station)
	elif option == '--list':
		station = sys.argv[2]
		songs(station)
	elif option == '--add':
		station = sys.argv[2]
		music = sys.argv[3]
		add(station,music)
	else:
		print 'invalid option'


if __name__ == '__main__':
	main()


