#!/usr/bin/env python3

import sys, os
sys.path.append( os.path.dirname("../lib/") )
import numpy as np
#from math import mod

class Trinary():
    def __init__(self):
        self.picture = np.array(None)
        
    def load_data(self, data):
        empty = []
        if type(data) == type(""):
            empty += list(data.strip())
        else:
            empty += data
        self.picture = np.array(empty, dtype='int')

    def has_data(self):
        return (self.picture.ndim and self.picture.size)

    def init_size(self, height, width):
        if not self.has_data():
            raise ValueError("Picture array is not yet defined. Please call load_data().")

        if width is None or height is None:
            raise ValueError("Need two arguments to build the picture")

        full_length = len(self.picture)
        if (full_length % (width * height)) != 0:
            raise ValueError("Data length {} not evenly divisble by {}*{}.".format(full_length, width, height))

        try:
            self.picture = self.picture.reshape(-1, width, height)
        except e:
            print("Unable to reshape.")
            exit(1)

    def shape(self):
        return self.picture.shape

    def layer(self, val):
        if self.picture.ndim == 3:
            return self.picture[val,:,:]
        else:
            raise ValueError("Picture has no layers")

    def seek_fewest(self, target):
        (l,w,h) = self.picture.shape
        least_val = 99999
        least_lyr = -1

        for my_id in range(0,l):
            my_layer = self.picture[my_id,:,:]
            bins = np.bincount( my_layer.ravel() )
            targets = bins[target]
            if targets == least_val:
                print("Found equality between layer {} and {} // {}s = {}".format(
                    least_lyr, my_id, target, least_val
                ))
                least_lyr = my_id
            elif targets < least_val:
                print("Lyr {} => {}".format(my_id, targets))
                least_val = targets
                least_lyr = my_id
            else:
                pass

        print("Least {}s at layer {}".format(target, least_lyr))
        return least_lyr

    def get_layer(self, l):
        return self.picture[l,:,:]

def main():
    with open("08/input.txt") as fh:
        input = fh.read()

    pict = Trinary()
    pict.load_data(input)
    pict.init_size(25, 6)

    print("Shape: ",pict.shape())
    #print("Layer 5:\n",pict.layer(5))
    few_layer = pict.seek_fewest(0)

    l1 = pict.get_layer(few_layer)
    print("Layer {}\n".format(few_layer),l1)
    (zeros,ones,twos) = np.bincount(l1.ravel())
    print("Ones: {}\tTwos: {}".format(ones,twos))
    prooduct = ones * twos
    print("Product = {}".format(prooduct))

main()
        