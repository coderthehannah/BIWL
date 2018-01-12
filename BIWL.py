



#####################################
####                            #####
## Beschdl's Intelligent WordLists ##
####                            #####
#####################################

    #Modules


import sys
import os
import argparse
import io
import itertools
from collections import deque
from colorama import Fore, Back, Style


colorama.init()

    # If no Input
if len(sys.argv) == 1:
    print("You didn't specify an argument, get help with --help or -h")
    sys.exit()

    # Variables
version ="0.6"

    #   Arguments
parser = argparse.ArgumentParser(description="       Simple tool to make specified wordlists, for example for informaion you got with doxing \n\n")
parser.add_argument("--lower", "-L",
                    action="store_true",
                    help="Enable to add every word in lowercase, if it isn't already in lowercase")
parser.add_argument("--removedouble", "-RD",
                    action="store_true",
                    help="Removes double entries in the input keywords")
parser.add_argument("-min", "-minimum",
                    type=int,
                    help="The minimum length of the password")
parser.add_argument("-max", "-m", "-maximum",
                    type=int,
                    help="The maximum length of the password")
parser.add_argument("-raw", "-r", nargs="+",
                    help="Raw input of keywords, seperated by simple spaces")
parser.add_argument("-file", "-f",
                    help="This is an input of keyword from a file, every word should be seperated by a new line")
parser.add_argument("-output", "-o",
                    help="This will be the output as a txt file")

args = parser.parse_args()




    # Error check

def errorCheck():
    if args.output==None:
        print("[i]     You need to specify an output!")
        sys.exit()
    if (args.file!=None) and (args.raw!=None):
        print("[i]     You can't use file input and raw input at the same time.")
        sys.exit()
    if (args.file==None) and (args.raw==None):
        print("[i]     Please specify either file input or raw input.")
        sys.exit()
    if args.min==None:
        print("[*]     No minimum specified, set to 8")
        args.min=8
    if args.max==None:
        print("[*]     No maximum specified, set to 16")
        args.max=16

        # Argument CHecks

def argumentCheck():
    Mylist = getTemp()
    if (args.lower):
        y = 0
        for keyword in Mylist:
            lowercase(Mylist[y], Mylist)
            y+=1
    if (args.removedouble):
        Mylist = removeDoubleInList(Mylist)
    return Mylist




    # Funtcions n stuff



def  lowercase(inp, list):
    if (inp.lower()!=inp):
        list.append(inp.lower())

def removeDoubleInList(listin):
    out = list(set(listin))
    return out


def readFromFile(file):
    outp = []
    f = io.open(file, "r")
    for line in f:
        outp.append(line)
    return outp


def writeToFile(file, inp):
    f = io.open(file, "a")
    f.write(inp)
    f.write("\n")
    f.close()


def getTemp():
    if (args.file!=None):
        temp = []
        temp = readFromFile(args.file)
        temp = removeBackslashN(temp)
    elif (args.raw!=None):
        temp = args.raw
    else:
        print(Fore.RED + "[!] Something went wrong, weird....")
        sys.exit()
    return temp


def listPrint(inp):
    y = 0
    for x in inp:
        print(" - " + inp[y])
        y+=1


def realString(inp):
    temp = ''.join(map(str, inp))
    temp = temp.replace("(", "")
    temp = temp.replace(",", "")
    temp = temp.replace("'", "")
    temp = temp.replace(" ", "")
    temp = temp.replace(")", "\n")
    outp = temp
    return outp

def removeBackslashN(inp):
    finalout = []
    y = 0
    for object in inp:
        temp = realString(inp[y])
        temp = temp.replace("\n", "")
        finalout.append(temp)
        y+=1
    return finalout


def checkPwd(inp, file):
            reallength = len(realString(inp))
            if not reallength==0:
                if (reallength>=args.min) and (reallength<=args.max):
                    writeToFile(file, realString(inp))


def makeList(listin, file):
        from collections import deque
        listin = deque(listin)
        for length in range(0, len(listin)):
            for length in range(0, len(listin)+1):
                for temp in itertools.combinations(listin, length):
                    checkPwd(temp, file)
                listin.rotate(-1)



def main():
    keywords = argumentCheck()
    print("\n[*]       Your keywords were:\n")
    listPrint(keywords)
    print("\n")
    makeList(keywords, args.output)
    print("[*] Done, saved list to " + args.output)


errorCheck()
main()
