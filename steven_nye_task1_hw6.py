#!/usr/bin/env python3
# encoding: utf-8

import sys

"""
steven_nye_task1_hw6.py
Created by Steven R. Nye on Nov 12, 2016
Email: stevennye@mail.weber.edu
Description: Minivan task 
"""

def mod1(hr, ld, rd, cl, ml, li, lo, ri, ro, gs):
    print("Heading Record " + str(hr) + ":")
    print("Left dashboard switch (0 or 1): " + str(ld))
    print("Right dashboard switch (0 or 1): " + str(rd))
    print("Child lock switch (0 or 1): " + str(cl))
    print("Master unlock switch (0 or 1): " + str(ml))
    print("Left inside handle (0 or 1): " + str(li))
    print("Left outside handle (0 or 1): " + str(lo))
    print("Right inside handle (0 or 1): " + str(ri))
    print("Right outside handle (0 or 1): " + str(ro))
    print("Gear shift position (P, N, D, 1, 2, 3 or R): " + gs)

    if gs != 'P' or gs != 'N' or gs != 'D' or gs != 'R' or gs != 1 or gs != 2 or gs != 3:
        print("Invalid Record: Both doors stay closed.")
        exit(1)

    if gs != 'P':
        print("Both doors stay closed.")
        exit(1)

    if ml != 1:
        print("Both doors stay closed.")
        exit(1)

    #Check for dashboard switches
    if rd == 1 and ld == 1:
        print("Both doors open.")
        exit(0)
        
    lOpen = False
    rOpen = False

    elif rd == 1:
        rOpen = True
        
    elif ld == 1:
        lOpen = True

    #Check outside handles
    if lo == 1:
        lOpen = True

    if ro == 1:
        rOpen = True

    #Check inside handles
    if li == 1 and cl == 0:
        lOpen = True

    if ri == 1 and cl == 0:
        rOpen = True

    #Print results
    if lOpen == True and rOpen == True:
        print("Both doors open.")
        exit(0)
    elif lOpen == True and rOpen == False:
        print("Left door is open.")
        exit(0)
    elif lOpen == False and rOpen == True:
        print("Right door is open.")
        exit(0)
    else:
        print("Both doors stay closed.")
        exit(1)



def main():
   mod1(1, 1, 0, 0, 1, 0, 1, 0, 0, 'E') 
   pass

if __name__ == "__main__":
    main()
    exit(0)

