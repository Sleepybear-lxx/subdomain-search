#coding=utf-8

from utils import diandian,brute
from config import *
from common import *
import os

sub_domain_res=[]
script_path=os.path.dirname(os.path.abspath(__file__))
cach_path=os.path.join(script_path,'result\\'+target_domain)
if not os.path.exists(cach_path):
	os.makedirs(cach_path,0777)
print ('Start sub_domian search:search')
search=diandian.Diandian()
search_res=search.run()
cach_file=os.path.join(cach_path,'diandian.json')
save_file(cach_file,search_res)
print ('Finish sub_domian search:search and save!')
print ('Start sub_domian search:brute')
brute_res=brute.do_brute()
cach_file=os.path.join(cach_path,'brute.json')
save_file(cach_file,brute_res)
print ('\nFinish sub_domian search:brute and save!')
