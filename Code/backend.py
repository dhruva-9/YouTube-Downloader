'''
api args = url and option

if option =1: download only audio
else: opt = 2 and download both video and audio
'''
import os
import re

basedir = os.path.realpath('bin')
basedir = re.escape(basedir)

def main(url, option):
	onlyAudio = "-x"

	if option == 1:
		args = "x -f bestaudio"
		os.system(basedir + '\\youtube-dl.exe ' + args + url)
		return True

	elif option == 2:
		args = "-f bestvideo+bestaudio"
		os.system(basedir + '\\youtube-dl.exe ' + args + " " + url)
		return True

	else:
		return False