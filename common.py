import requests,json
from config import *



def http_requests_get(url,target_domain=target_domain,headers=headers):
	res = requests.get(url=url + target_domain, headers=headers)
	return res.content


def save_file(file_name,res):
	try:
		with open(file_name, 'w') as json_file:
			json.dump(res, json_file,indent=4)
			json_file.close()
	except Exception,e:
		pass

