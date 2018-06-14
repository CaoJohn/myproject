#!/anaconda3/bin/python3.6
# coding=utf-8
'''
Created on 2018年5月11日

@author: jiangwen
'''
import yaml
import codecs

class BaseParameter(object):
    def __init__(self,filename):
        with codecs.open(filename) as f:
            self.x = yaml.load(f)
        print(self.x)

if __name__=="__main__":
    print("*****")
    filename = r'/Users/jiangwen/Documents/John/work/projects/python/Ules/para_test051101.yaml'
    bp = BaseParameter(filename)
    print(bp)
#     print(bp.x['Source'])
#     type(bp)
#     print(bp.x['Source'][0]['para'])
#     print(list(map(int,bp['Source'])))