from datetime import datetime
from configparser import ConfigParser

import requests
import json

config = ConfigParser()
config.read('./conf/setup.ini')

class Slack(object):
	def __init__(self):
		self.time_now = datetime.now()
		self.timestamp = datetime.timestamp(self.time_now) 
		self.slack_webhook_url = config['SLACK']['slack_webhook_url']
		self.slack_channel = config['SLACK']['slack_channel']
		self.slack_username = config['SLACK']['slack_username']
		
	def Alert(self, text, title, body, priority, color):
		payload = {
		    'username': self.slack_username,
		    'text': text,
		    'attachments': [
                        {
			    'color': color,
			    'title': title,
			    'text': body,
                            "fields": [
                                {
                                    "title": "Priority",
                                    "value": priority,
                                }
                            ],
                            "ts": self.timestamp
			}
                    ]
		}
		
		response = requests.post(
                   self.slack_webhook_url, data=json.dumps(payload),
                   headers={'Content-Type': 'application/json'}
		)
		return(response)
