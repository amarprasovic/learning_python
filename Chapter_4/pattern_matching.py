'''
Created on 12 Mar 2018

@author: amar.prasovic
'''

import re

#match = re.match('Hello[ \t]*(.*)world', 'Hello beautiful Python world')
#print(match.group(1))

match = re.match('[/:](.*)[/:](.*)[/:](.*)','/usr/home:lumberjack')
print(match.groups())

print(re.split('[/:]', '/usr/home/lumberjack'))