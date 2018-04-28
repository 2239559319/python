import re
data='Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'

patt='^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
m=re.match(patt,data)
print m.group()
#   output id 'Thu'
print m.group(1)
#   output id 'Thu'
print m.groups()
#   output is '('Thu',)'

patt='^(\w{3})'
m=re.match(patt,data)
if m is not None:
    print m.group()
#   output is 'Thu'
print m.group(1)
#   output is 'Thu'
patt='^(\w){3}'
m=re.match(patt,data)
if m is not None:
    print m.group()
#   output is 'Thu'
print m.group(1)
#   output is 'u'

patt='\d+-\d+-\d+'
print re.search(patt,data).group()
#   output is '1171590364-6-8'
patt='.+\d+-\d+-\d+'
print re.match(patt,data).group()
#   output is 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'

patt='.+(\d+-\d+-\d+)'
print re.match(patt,data).group(1)
#   output is '4-6-8'

patt='.+?(\d+-\d+-\d+)'
print re.match(patt,data).group(1)
#    output is '1171590364-6-8'

patt='-(\d+)-'
m=re.search(patt,data)
print m.group()
#    output is '-6-'
print m.group(1)
# output is '6'