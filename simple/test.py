'''
Created on 

@author: haoweizh
'''

import re
r = re.compile(r"^(.*?)(\@(\d{4}-\d{2}-\d{2}))?\.(yang|yin)$")
m = r.search('c:/wei/haowei@2017-11-11.yang')
(name, _dummy, rev, format) = m.groups()
print(name, _dummy, rev, format) 

comment = '(/\*([^*]|[\r\n\s]|(\*+([^*/]|[\r\n\s])))*\*+/)|(//.*)|(/\*.*)'
re_comment = re.compile(comment)
m = re_comment.match("/*haoweihaowei")
identifier = r"[_A-Za-z][._\-A-Za-z0-9]*"
prefix = identifier
keyword = '((' + prefix + '):)?(' + identifier + ')'
comment = '(/\*([^*]|[\r\n\s]|(\*+([^*/]|[\r\n\s])))*\*+/)|(//.*)|(/\*.*)'

# no group version of keyword
keyword_ng = '(?:(' + prefix + '):)?(?:' + identifier + ')'

re_keyword = re.compile(keyword)
re_keyword_start = re.compile('^' + keyword)
re_comment = re.compile(comment)
print(m.group(0))
print(m.end())

m = re_keyword.match('haowei:zhang')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
