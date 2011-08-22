#!/usr/bin/python
#encoding: utf-8
"""
tag_clustering.py

"""

import sys, os
import numpy
from Pycluster import *

class TagClustering(object):
    def __init__(self):
        data = numpy.array([(1,1,0), (1,0,0), (0,0,0)])
        print data

        labels, error, nfound = kcluster(data, 2)

        print labels

if __name__ == '__main__':
    t = TagClustering()
