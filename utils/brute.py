#coding=utf-8
import re
from dns import resolver
import threading,Queue,sys
from config import *
rule='(.*?)\n'
target_domain='.'+target_domain
file_name='brute.json'
res=[]
content=Queue.Queue()
with open(dic_path) as dic_file:
	while True:
		line=dic_file.readline()
		if line:
			file_size+=1
			line=re.findall(rule,line)[0]
			content.put(line)
		else:
			break


class dis_brute(threading.Thread):
	def __init__(self,Queue,res):
		threading.Thread.__init__(self)
		self.queue=Queue
		self.res=res

	def run(self):
		global error,right
		while not self.queue.empty():
			sub_domian=self.queue.get()
			sys.stdout.write('\r Finish '+str((1-self.queue.qsize()*1.0/file_size)*100)+'% detect '+sub_domian+'...')
			sys.stdout.flush()
			try:
				resolver.query(sub_domian + target_domain, 'A')
				self.res.append(sub_domian+target_domain)
			except Exception as e:
				pass

def do_brute():
	task=[]
	for i in xrange(thread_count):
		task.append(dis_brute(content,res))
	for i in xrange(thread_count):
		task[i].start()
	for i in xrange(thread_count):
		task[i].join()
	return res

