#!/usr/bin/env python3

# 
# slack-sharedlinks-manager
# Author: Enrico Cambiaso
# Email: enrico.cambiaso[at]gmail.com
# GitHub project URL: https://github.com/auino/slack-sharedlinks-manager
# 

import requests
import json
import argparse
import calendar
import errno
import sys
import os
import time
from datetime import datetime, timedelta
from config import config
from pprint import pprint # for debugging purposes

# import link manager function
from linkmanager import savelinkdata

# constants

# Slack base API url
API = 'https://slack.com/api'

# useful to avoid duplicate downloads
TIMESTAMPFILE = config['maindir']+"offset.txt"

# format a response in json format
def response_to_json(response):
	try:
		res = response.json
		foo = res['ok']
		return res
	except: # different version of python-requests
		return response.json()

# save the timestamp of the last download (+1), in order to avoid duplicate downloads
def set_timestamp(ts):
	try:
		out_file = open(TIMESTAMPFILE,"w")
		out_file.write(str(ts))
		out_file.close()
		return True
	except Exception, e:
		if config['debug']: print str(e)
		return False

# get saved timestamp of last download
def get_timestamp():
	try:
		in_file = open(TIMESTAMPFILE,"r")
		text = in_file.read()
		in_file.close()
		return int(text)
	except Exception, e:
		if config['debug']: print str(e)
		set_timestamp(0)
		return None

# get the list of existent channels
def get_channels_list():
	url = API+'/channels.list'
	data = {'token': config['token'] }
	response = requests.post(url, data=data)
	if config['debug'] and config['extreme_debug']: pprint(response_to_json(response))
	return response_to_json(response)['channels']

# get channel name from identifier
def get_channel_name(id):
	url = API+'/channels.info'
	data = {'token': config['token'], 'channel': id }
	response = requests.post(url, data=data)
	if config['debug'] and config['extreme_debug']: pprint(response_to_json(response))
	return response_to_json(response)['channel']['name']

# get user name from identifier
def get_user_name(id):
	url = API+'/users.info'
	data = {'token': config['token'], 'user': id }
	response = requests.post(url, data=data)
	if config['debug'] and config['extreme_debug']: pprint(response_to_json(response))
	return response_to_json(response)['user']['name']

# request files
def make_requester():
	list_url = API+'/channels.history'

	def all_requester(channel):
		if config['debug']: print('Requesting channel history')
		data = {'token': config['token'], 'channel': channel, 'count': config['messages_count']}
		ts = get_timestamp()
		if ts != None: data['oldest'] = ts
		response = requests.post(list_url, data=data)
		if response.status_code != requests.codes.ok:
			print('Error fetching file list')
			sys.exit(1)
		return response_to_json(response)

	return all_requester

# main function
if __name__ == '__main__':
	# retrieving identifiers of considered channels
	channels_data = get_channels_list()
	channels_id = []
	for channel_data in channels_data:
		if str(channel_data['name']) in config['considered_channels']: channels_id.append({'name':str(channel_data['name']), 'id':str(channel_data['id'])})
	# retrieving links for each channel
	for channel in channels_id:
		print "\nCHANNEL", channel['name'].upper()
		users = dict()
		requester = make_requester()
		ts = None
		json = requester(channel['id'])
		if not json['ok']: print('Error', json['error'])
		messages = json['messages']
		for m in messages:
			try:
				if config['debug'] and config['extreme_debug']: pprint(m)
				date = float(m['ts'])
				if ts == None or float(date) > float(ts): ts = date
				if "<http" in str(m['text'].decode('utf-8')):
					user = get_user_name(m['user'])
					savelinkdata(channel['name'], user, m)
			except Exception, e:
				if config['debug']: pprint(e)
				continue
	if ts != None: set_timestamp(int(ts)+1)
	if config['debug']: print('Finished.')
