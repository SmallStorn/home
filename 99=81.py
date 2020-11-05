# -*- coding:utf-8 -*-
for x in range(1,10):
    for y in range(1,x+1):
        print("{0}*{1}={2}\t".format(x,y,x*y),end="")
    print("\n");