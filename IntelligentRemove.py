print("\n\n     Developement Edition\n\n")

import sys
import os
import io
import argparse


# Variables

version="0.1"
sorts = [""]


# Argparse

parser = argparse.ArgumentParser(description="       Tool to remove anyoing and unnecassary passwords form a wordlist \n\n")
parser.add_argument("-file", "-f",
                    help="This is an input of keyword from a file, every word should be seperated by a new line")
parser.add_argument("--removedouble", "-D",
                    action="store_true",
                    help="This option is to remove double entries")
parser.add_argument("--removeonlynumbers", "-N",
                    action="store_true",
                    help="This option is to remove entries with only numbers")
parser.add_argument("-sort", "-s",
                    help="Let's your sort by a special algorithm you an choose, get it with \"--sorthelp\"")
parser.add_argument("--sorthelp", "-SH",
                    action="store_true",
                    help="Get help about the sort function")
args = parser.parse_args()

if (len(sys.argv)==1):
    print("You did not specify any arguments, get help with --help or -h")
    sys.exit()

# Functions
def readFromFile(file):
    outp = []
    f = io.open(file, "r")
    for line in f:
        outp.append(line)
    return outp
def writeToFile(file, inp):
    f = io.open(file, "w")
    f.write(inp)
    f.write("\n")
    f.close()
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



# Remove Functions

def removeDoubleInList(listin):
    print("[-] Removing Doubles in list... ")
    out = list(set(listin))
    return out

def removeOnlyNumbers(listin):
    is_Number=True
    print("[-] Removing entries with only numbers... ")
    out = []
    round = 0
    for object in listin:
        print(listin[round])
        if 0==1:
            is_Number=False
        if not (is_Number==True):
            out.append(realString(listin[round]))
        round+=1
    return out

# Maaaaaaaaain

def argcheck():
  if (args.sorthelp):
    print("[*] Here is the list of possible sorts you can choose right now\n")
    listPrint(sorts)


def main():
    Myfile = args.file
    Mylist = []
    Mylist = readFromFile(Myfile)
    if (args.removedouble):
        Mylist = removeDoubleInList(Mylist)
    if (args.removeonlynumbers):
        print("This function is not available at the moment, under construction")
        #Mylist = removeOnlyNumbers(Mylist)
    writeToFile(Myfile, realString(Mylist))

        # Execute the stuff
argcheck()
main()
print("\n[*]   Finished, saved to \"" +  args.file + "\"")
