# simple link manager sample
# this module should implement the following method:
#  savelinkdata(channel, user, data)

import os
from config import config # generic configuration settings

def savelinkdata(channel, user, data):
	# retrieving absolute output directory
	outputdir = config['maindir']+config['outputdir']
	# creating main output directory, if needed
	try: os.stat(outputdir)
	except: os.mkdir(outputdir)
	# retrieving needed missing data
	date = float(data['ts'])
	text = data['text'] # saving full text
	# retrieving output file name
	filename = outputdir+"/"+channel+'.txt'
	try:
		# computing link data string
		s = "["+str(date)+"] "+user+": "+text
		print s
		# appening link data to output
		out_file = open(filename, "a")
		out_file.write(s+"\n")
		out_file.close()
	except: return False
	# everything is ok
	return True
