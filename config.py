import os

config = {}

# API Token: see https://api.slack.com/web
config['token'] = "<your_token>"

# selected/considered channels
config['considered_channels'] = [ "general", "random" ]

# how many messages retrieve at most?
config['messages_count'] = 10000

# output main directory, without slashes
config['outputdir'] = "links"

# enable debug?
config['debug'] = False

# enable extremely verbose debug?
config['extreme_debug'] = False

# main program directory (automatically computed)
config['maindir'] = os.path.dirname(os.path.realpath(__file__))+'/'
