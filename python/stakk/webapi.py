#!/usr/bin/env python
#encoding: utf-8
from sys import path
from urllib2 import unquote

directory = "/home/nokuno/nokuno/python/stakk"
path.append(directory)
from pos_bigram import Converter

dictionary = directory + "/data/dictionary.txt"
connection = directory + "/data/connection.txt"
converter = Converter(dictionary, connection, "\t")

def application(environ, start_response):
    status = '200 OK'
    query = environ['QUERY_STRING'].split('=',1)[1]
    query = unquote(query)
    output = converter.convert(query)
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    make_server('', 8080, application).serve_forever()

