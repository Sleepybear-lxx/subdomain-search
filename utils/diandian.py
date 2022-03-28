#coding=utf-8

import requests
import re
import json
from common import *


class Diandian():
	def __init__(self):
		self.url='https://tool.chinaz.com/subdomain/'
		self.file_name='C:\\Users\\Y700\\Desktop\\untitled3\\result\\diandian.json'
	def run(self):
		raw_content=http_requests_get(self.url)
		rule='<a href="//tool\.chinaz\.com/subdomain\?domain=(.*?)" target="_blank">'
		res=re.findall(rule,raw_content)
		return res
