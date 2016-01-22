# simple link manager sample
# this module should implement the following method:
#  savelink(channel, user, data)

import os
from config import config # generic configuration settings

def savelink(channel, user, data):
	# retrieving absolute output directory
	outputdir = config['maindir']+config['outputdir']
	# creating main output directory, if needed
	try: os.stat(outputdir)
	except: os.mkdir(outputdir)
	# retrieving needed missing data
	date = float(data['ts'])
	url = data['text'][1:-1]
	# retrieving output file name
	filename = outputdir+"/"+channel+'.txt'
	try:
		# computing link data string
		s = "["+str(date)+"] "+user+": "+url
		print s
		# appening link data to output
		out_file = open(filename, "a")
		out_file.write(s+"\n")
		out_file.close()
	except: return False
	# everything is ok
	return True
