def frontend():
	import pyautogui as gui

	gui.alert(text = "Welcome to the YouTube downloader", title="", button = 'Thankyou')

	url = gui.prompt("Enter video Url: ")

	if url == '':
		gui.alert(text = "Url cant be left empty!", title="Url cant be left empty!", button = "Retry")
		url = gui.prompt("Enter video Url: ")

	optionArr = ['Only Audio', 'Audio + Video']
	option = gui.confirm(text = 'Enter option', title = 'Enter option', buttons = optionArr)

	'''
	option 1 = Only Audio
	option 2 = Audio + VIdeo
	'''
	optnumber = 0

	if option == 'Only Audio':
		optNumber = 1
	else:
		optNumber = 2

	if downloader(url, optNumber) == True:
		if gui.confirm(title = "Download Completed!!!", text="Download Completed \n Continue", buttons = ['Yes', 'No']) == 'Yes':
			frontend()
		
	else:
		gui.alert(title = "A problem occoured!!", text = "Could Not Complete The download")

'''
api args = url and option

if option =1: download only audio
else: opt = 2 and download both video and audio
'''
import os
import re

basedir = os.path.realpath('bin')
basedir = re.escape(basedir)

def downloader(url, option):
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
if __name__ == '__main__':
	frontend()