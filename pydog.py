#/usr/bin/python

__description__ = 'Tool to create passwords based on a given word.'
__author__ = 'maudits'
__version__ = '0.1'
__date__ = '2012/04/28'

# methods are: 
#   - word + dumb suffix
#   - l33t of single char
#   - combo l33t
#   - capitalise single letter
#   - (not implemented: multi capital letters)
#   - capitalise + l33t
#   - capitalise + dumb suffix
#   - capitalise + l33t + dumb suffix

import itertools
import sys

# dumb suffix list - add more if you want
el= [ '','0','1','01','001','2','02','002','3','03','003','123','12','321','32','21','1234','12345','321','1!','1!!!','!','!!','!!!','123!','123!!','123!!!','!@#','!@#$','!!@@##','!@#$%','?' ]


if len(sys.argv) < 2:
   print "Usage: python " + sys.argv[0] + " <word>"
   exit(0)

word = sys.argv[1]
#word = raw_input("give me the word to mangle: ")

pw_list = []


# l33t chars - add more if you want
leet = {'a':'@', 'e':'3', 'i':'1', 's':'5', 'o':'0'}



def single_leet(text, dic):
    for i, j in dic.iteritems():
        if text.find(i) != -1:
           pw_list.append(text.replace(i, j))


def combo_leet(text, dic, n):
    leeted = []
    count = 0
    for i, j in dic.iteritems():
        if text.find(i) != -1:
           text = text.replace(i, j)
	   pw_list.append(text)
	   leeted.append(text)
	count = count + 1
	if count > n:
	   break
    return leeted


def dumb_suffix(text, suff):
    for i in suff:
        pw_list.append(text + str(i))



# dumb suffix
dumb_suffix(word, el)

# single l33t
single_leet(word, leet)

# combo l33t
leeted = combo_leet(word, leet, len(leet.items()))

# UPPERCASE
uppercase = word.upper()
dumb_suffix(uppercase, el)
pw_list.append(uppercase)

# UPPERCASE for leeted
for x in leeted:
    dumb_suffix(x.upper(), el)


# capitalise + l33t + dumb suffix
capital = word.title()
dumb_suffix(capital, el)

# multi capitalise + l33t + dumb suffix
copycat = [] 
for i in pw_list:
    copycat.append(i.title())

pw_list = pw_list + copycat


# append suffix to leeted new words
for x in leeted:
    dumb_suffix(x, el)


# print out & good luck!
remocc = set(pw_list)
for e in remocc:
    print e


