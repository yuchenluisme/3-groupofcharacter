format="hello,%s. %s enough for you"
values=('world','hot')
format % values

#'HELLO,kate '
from string import Template
tmpl=Template("HELLO,$WHO ")
tmpl.substitute(WHO="kate")

#'heis,'
"{}{},".format("he","is")

#'Mr yu'.'the number is 9'
fullname=["yu"]
"Mr {name[0]}".format(name=fullname)
#format的用法：“{}”.format("")
"the number is {n}".format(n=9)

#
from math import pi
"{pi}".format(pi=pi)
'3.141592653589793'
"{pi:.2f}".format(pi=pi)
'3.14'

#左对齐右对齐居中
print('{0:<10.2f}'.format(pi))
3.14
print('{0:>10.2f}'.format(pi))
      3.14
print('{0:^10.2f}'.format(pi))
   3.14
"it is a joke".center(20)
'    it is a joke    '
#.find找东西

#
p=['1','2','3']
q='+'
q.join(p)
'1+2+3'

#
"it".replace('i','k')
'kt'