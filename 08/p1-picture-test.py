#!/usr/bin/env python3

import sys, os
sys.path.append( os.path.dirname("../lib/") )
import numpy as np
#from math import mod

class SpaceImageFormat():
    def __init__(self):
        self.picture = np.array(None)
        self.shape = self.picture.shape
        
    def _shape(self):
        self.shape = self.picture.shape

    def load_data(self, data):
        empty = []
        if type(data) == type(""):
            empty += list(data.strip())
        else:
            empty += data
        self.picture = np.array(empty, dtype='int')
        self._shape()

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
            self._shape()
        except:
            print("Unable to reshape.")
            exit(1)

    def layer(self, val):
        if self.picture.ndim == 3:
            return self.picture[val,:,:]
        else:
            raise ValueError("Picture has no layers")

    def seek_fewest(self, target):
        least_val = 99999
        least_lyr = -1

        count = 0
        for layer in self.picture:
            bins = np.bincount( layer.ravel() )
            targets = bins[target]
            if targets == least_val:
                print("Found equality between layer {} and {} // {}s = {}".format(
                    least_lyr, count, target, least_val
                ))
                least_lyr = count
            elif targets < least_val:
                print("Lyr {} => {}".format(count, targets))
                least_val = targets
                least_lyr = count
            else:
                pass

            count += 1

        print("Least {}s at layer {}".format(target, least_lyr))
        return least_lyr

    def get_layer(self, l):
        return self.picture[l,:,:]

    def flatten_sif(self, pixel_array):
        decoded = self.picture[0]
        pix_trans = next((key for key,val in pixel_array.items() if val==False), None)
        pix_black = next((key for key,val in pixel_array.items() if val==' '), None)
        pix_white = next((key for key,val in pixel_array.items() if val=='█'), None)
        # next((name for name, age in mydict.items() if age == search_age), None)
        for layer in self.picture:
            decoded = np.where(decoded != pix_trans, decoded, layer)

        decoded = np.where(decoded == pix_white, pixel_array[pix_white], pixel_array[pix_black]) # To make it easier to see
        return decoded

    def print(self, layer_id=-1, layer=np.array([]), join=False):
        if layer_id > -1:
            print("Layer {}\n{}".format( layer_id, self.picture[layer_id,:,:] ))
        elif layer.ndim>0:
            if join:
                print("Layer joined:")
                for row in layer:
                    print("\t{}".format("".join(row)))
            else:
                print("Layer passed:\n{}".format(layer))


if __name__ == "__main__":
    with open("08/input.txt") as fh:
        input = fh.read()

    pict = SpaceImageFormat()
    pict.load_data(input)
    pict.init_size(25, 6)

    print("Shape: ",pict.shape)
    #print("Layer 5:\n",pict.print(layer_id=5))
    few_layer = pict.seek_fewest(0)

    l1 = pict.get_layer(few_layer)
    pict.print(layer_id=few_layer)
    bins = np.bincount(l1.ravel())
    print("Ones: {}\tTwos: {}".format(bins[1],bins[2]))
    prooduct = bins[1] * bins[2]
    print("Product = {}".format(prooduct))

    ## Part 2

    part2 = pict.flatten_sif({0:' ', 1:'█', 2:False})
    pict.print( layer=part2, join=True )
