#!/usr/local/bin/python3
import operator

data = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,2,23,10,27,1,6,27,31,1,31,6,35,2,35,10,39,1,39,5,43,2,6,43,47,2,47,10,51,1,51,6,55,1,55,6,59,1,9,59,63,1,63,9,67,1,67,6,71,2,71,13,75,1,75,5,79,1,79,9,83,2,6,83,87,1,87,5,91,2,6,91,95,1,95,9,99,2,6,99,103,1,5,103,107,1,6,107,111,1,111,10,115,2,115,13,119,1,119,6,123,1,123,2,127,1,127,5,0,99,2,14,0,0"
data_array = data.split(",")

#data_array[1] = 12
#data_array[2] = 2

offset = 0
is_done = False

def print_data():
    return ",".join([
        str(padded).rjust(8) for padded in data_array
    ])

def next_section():
    try:
        (a,b,c,d) = data_array[ offset : offset+4 ]
    except:
        print("Something went wrong. Aborting.\nData:: {}".format( print_data() ))
        exit()

    (a,b,c,d) = (int(a), int(b), int(c), int(d))
    return (a,b,c,d)

def show_work(op, a1, a2, s):
    ops = {'+': operator.add,
        '*': operator.mul}
    #print("  {{{}}} {} {{{}}}  =>".format( a1, op, a2), end='')
    v1 = int(data_array[a1])
    v2 = int(data_array[a2])
    vs = int(data_array[s])
    #print("  {} {} {}  =>".format( v1, op, v2), end='')
    val = ops[op](v1,v2)
    #print("  {} (store in {})".format(val, s))
    data_array[s] = val


while not is_done:
    (opcode, arg1, arg2, store) = next_section()

    if opcode == 99:
        #print("All done. \nData:: {}".format( print_data() ))
        print("All done. Final answer = {}".format( data_array[0] ))
        is_done = True
        continue
    elif opcode == None:
        print("Rut roh... ran out of data.\n\t{}".format( print_data() ))
        is_done = True
        continue

    #print("O: {}\tA1: {}\tA2: {}\tS: {}".format(opcode, arg1, arg2, store))

    if opcode == 1:
        # Adding arg1 and arg2, storing in store
        show_work( '+', arg1, arg2, store )
    elif opcode == 2:
        show_work( '*', arg1, arg2, store )

    #print("NewData:: {}".format( print_data() ))

    offset = offset + 4
