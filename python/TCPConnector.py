__author__ = 'GHajba'

import sys
import socket

""" this is a simple TCP connector class to read from and write to TCP sockets"""


def read_data():
    data = ""
    while True:
        tmp = sf.readline().strip()
        if "update" == tmp:
            break
        # split the data here
        data += tmp
    return data

def compute_move(data):
    return ""

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    sf = s.makefile()
    while True:
        data = read_data()
        print data
        sf.readline()
        move = compute_move(data)
        sf.write('move ' + str(move) + '\n')
        sf.flush()