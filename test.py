import os
import pickle
import json
l = [1,2,3,4]
t = ('a','b','c','d')
d = {'name':'pzs', 'age':20, 'score': 99}
l2 = [d,t,l]
class Person(object):
	def __init__(self,name,id,gender,city):
		self.name = name
		self.id = id
		self.gender = gender
		self.city = city
def p2dict(std):
		return {
			'name':std.name,
			'id':std.id,
			'gender':std.gender,
			'city':std.city
		}
p = Person('pzs',2019011464,'male','beijing')
js = json.dumps(p, default = p2dict)
print(js)
# with open('test.txt','wb') as f:
# 	pickle.dump(d,f)
# with open('test.txt','rb') as f:
# 	d = pickle.load(f)
# 	print(d)
# with open('test.txt','wb') as f:
# 	pickle.dump(l,f)
# with open('test.txt','rb') as f:
# 	l = pickle.load(f)
# 	print(l)
# f = open('test.json','wb')
# js = json.dumps(l2)
# with open('test.txt','w') as f:
# 	f.write(js)
# with open('test.txt','r') as f:
# 	js = f.read()
# l3 = json.loads(js)
# print(l3)

