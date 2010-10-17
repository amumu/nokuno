#!/usr/bin/env python
from optparse import OptionParser
from urllib import quote, urlopen
from time import sleep
from sys import exit

parser = OptionParser()
parser.add_option("-f", dest="filename")
parser.add_option("-n", dest="name", default="test")
parser.add_option("-l", dest="line", type="int", default=10)
parser.add_option("-t", dest="time", type="int", default=5)
parser.add_option("-m", dest="maximum", type="int", default=2000)
parser.add_option("-s", dest="size", type="int", default=1000)
parser.add_option("-b", dest="base")
parser.add_option("-w", dest="work", action="store_true")
parser.add_option("-d", dest="debug", action="store_true")
parser.add_option("-o", dest="open", action="store_true")
parser.add_option("-r", dest="response", action="store_true")
(options, args) = parser.parse_args()

contents = open(options.filename).readlines()
if len(contents) >= options.size:
    print "size over!", len(contents)
    exit()

for i in range(0, len(contents), options.line):
    name = options.name + "%03d" % int(i/options.line)
    u = options.base + "?file=" + name + "&text="
    u += quote(''.join(contents[i:i+options.line]))
    if len(u) >= options.maximum:
        print "length over!", len(u), 'line', i
        exit()
    if options.work:
        print 'working', int(i/options.line), '/', int(len(contents)/options.line)
    if options.debug:
        print len(u), u
    if options.open:
        result = urlopen(u).read()
        if options.response:
            print result
    sleep(options.time)
