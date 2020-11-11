#!/usr/bin/env python3

''' Send SMS to recipient via smsglobal http API

Compile data to send an SMS to a nominated recipient. Credentials and
constants are initially defined. Credentials are then assembled as part of
an HTTP string that is compiled prior to sending. Takes a message as a
parameter. Designed to be imported for chatbot and external API useage.
'''
from configparser import ConfigParser
import urllib.parse
import urllib.request


""" Setup constants and parameters. Import secrets from config """
parser = ConfigParser()
parser.read('config.ini')
username = parser.get('settings', 'username')
password = parser.get('settings', 'password')
sender = "Bot"
alice = "+000000000000"
bob = "+00000000000"


def sendText(message):
	""" Call out to smsglobal gateway and send collected string
	with parameter as http message

	Parameters
    ----------
    "message" : str
        The message to be sent to the recipient.
	"""

	http_req = "http://www.smsglobal.com/http-api.php?action=sendsms&user="
	http_req += urllib.parse.quote(username)
	http_req += "&password="
	http_req += urllib.parse.quote(password)
	http_req += "&from="
	http_req += urllib.parse.quote(sender)
	http_req += "&to="
	http_req += urllib.parse.quote(alice)
	http_req += "&text="
	http_req += urllib.parse.quote(message)
	get = urllib.request.urlopen(http_req)
	get.close()
