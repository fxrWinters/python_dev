# -*- coding: UTF-8 -*-

'''
Created on 2016年1月12日

An example of reading and writing Unicode strings:
Writes a Unicode string to a file in utf-8 and reads itback in.

@author: fxr
'''

CODEC = 'utf-8'
FILE = 'unicode.txt'

if __name__ == '__main__':
    hello_out = u"Hello world\n"
    bytes_out = hello_out.encode(CODEC)
    
    f = open(FILE, "w")
    f.write(bytes_out)
    f.close()
    
    f = open(FILE, "r")
    bytes_in = f.read()
    f.close()
    
    hello_in = bytes_in.decode(CODEC)
    print hello_in