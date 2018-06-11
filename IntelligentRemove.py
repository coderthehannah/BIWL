print("\n\n     Developement Edition\n\n")

import signal
import threading
import sys
import os
import io
import argparse
import re
done = False
version = "0.4"
# Argparse

parser = argparse.ArgumentParser(description="       Tool to remove anyoing and unnecassary passwords form a wordlist \n\n")
parser.add_argument("-file", "-f",
                    help="This is an input of keyword from a file, every word should be seperated by a new line")

parser.add_argument("--animation", "-A",
                    action="store_true",
                    help="Shows the animation")
parser.add_argument("-minimum", "-min",
                    help="Defines the minimum length of an entry")
parser.add_argument("-maximum", "-max",
                    help="Defines the maximum length of an entry")
parser.add_argument("--removedouble", "-D",
                    action="store_true",
                    help="This option is to remove double entries")
parser.add_argument("--removeonlynumbers", "-N",
                    action="store_true",
                    help="This option is to remove entries with only numbers")
parser.add_argument("--removeemptyentries", "-E",
                    action="store_true",
                    help="Removes blank entries in wordlist (\\n)")
parser.add_argument("--removelowercase", "-L",
                    action="store_true",
                    help="Removes all entries with only lowercase letters and numbers")
parser.add_argument("--removestring", "-S",
                    action="store_true",
                    help="Removes all entries with only letters")
parser.add_argument("-startwith", "-sw",
                    help="Checks if entry contains the string given behind the \"startwith\" argument")

parser.add_argument("--full", "-F",
                    action="store_true",
                    help="Goes to every algorithm available, gives the most efficient passwordlist, but also the shortest")
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

def animation():
    import time
    import itertools
    try:
        for char in itertools.cycle(['|', '/', '-', '\\']):
            sys.stdout.write('Loading ' + char)
            sys.stdout.flush()
            time.sleep(0.15)
            if done:
                break
    except KeyboardInterrupt:
        sys.stdout.write('Done!     ')
        sys.exit()
t = threading.Thread(target=animation)

 # Functions

def checkMax(listin):
    print("[-]Removing entries that are to long...")
    out=[]
    round = 0
    for object in listin:
        temp = listin[round]
        length = len(temp.replace("\n", ""))
        if not (length>int(args.maximum)):
            out.append(realString(listin[round]))
        round+=1
    return out
def checkMin(listin):
    print("[-]Removing entries that are to short...")
    out=[]
    round = 0
    for object in listin:
        temp = listin[round]
        length = len(temp.replace("\n", ""))
        if not (length<int(args.minimum)):
            out.append(realString(listin[round]))
        round+=1
    return out


# Remove Functions

def removeLowerCase(listin):
    print("[-] Removing entries with lowercase letters and numbers only...")
    out=[]
    round = 0
    for object in listin:
        temp = listin[round]
        lowered = temp.lower()
        if not (temp==lowered):
            out.append(realString(listin[round]))
        round+=1
    return out


  
def startWith(listin):
  print("[-] Removing entries that don't start with" + args.startswith)
  return 0
  
  
def removeString(listin):
    print("[-] Removeing entries that consists of strings only...")
    out=[]
    round = 0
    for object in listin:
        if not (listin[round].replace("\n", "").isalpha()):
            out.append(realString(listin[round]))
        round+=1
    return out

def removeEmptyEntries(listin):
    print("[-] Removing empty entries...")
    out = []
    round = 0
    for object in listin:
        if not (listin[round]=="\n"):
            out.append(realString(listin[round]))
        round+=1
    return out


def removeDoubleInList(listin):
    print("[-] Removing Doubles in list... ")
    out = list(set(listin))
    return out
    done = True

def removeOnlyNumbers(listin):
    print("[-] Removing entries with only numbers... ")
    out = []
    round = 0
    for object in listin:
        if not (listin[round].replace("\n", "").isdigit()):
            out.append(realString(listin[round]))
        round+=1
    return out

# Maaaaaaaaain
def checkErrors():
    import os



def main():
    if (args.animation):
        t.start()
        sys.exit()
    Myfile = args.file
    Mylist = []
    Mylist = readFromFile(Myfile)
    if (args.removedouble or args.full):
        Mylist = removeDoubleInList(Mylist)
    if (args.removeonlynumbers or args.full):
        Mylist = removeOnlyNumbers(Mylist)
    if (args.removeemptyentries or args.full):
        Mylist = removeEmptyEntries(Mylist)
    if (args.removelowercase or args.full):
        Mylist = removeLowerCase(Mylist)
    if (args.removestring or args.full):
        Mylist = removeString(Mylist)
    if (args.startswith!=None):
      Mylist = checkStart(Mylist)
    if (args.minimum!=None):
        Mylist = checkMin(Mylist)
    if (args.maximum!=None):
        Mylist = checkMax(Mylist)

    writeToFile(Myfile, realString(Mylist))

        # Execute the stuff
checkErrors()
main()
print("\n[*]   Finished, saved to \"" +  args.file + "\"")
