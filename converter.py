import sys
import os
import numParser
import getopt
import exceptions
import configParser

def main():
    # Gets the command line arguments
    opts, _ = getopt.getopt(sys.argv[1:], "ri:o:")
    inputfile = ""
    outputfile = "output.txt"
    # Variable that checks if we're trying to generate from a machine parser
    fromMachineTable = False

    for opt, arg in opts:
        if(opt == "-r"):
            fromMachineTable = True
        elif(opt == "-i"):
            inputfile = arg
        elif(opt == "-o"):
            outputfile = arg
    
    # Read file
    try:
        file = open(inputfile, "r")
    except:
        print("Input file not found! Usage: converter.py (-r) -i inputfile.txt -o outputfile.txt")
        sys.exit(2)
    number = file.read()
    file.close()

    # Creating teh correct parser
    if(not fromMachineTable):
        parser = numParser.numParser()
    else:
        parser = configParser.configParser()

    # Write output to file
    outFile = open(outputfile, "w")
    try:
        outFile.write(parser.parse(number))
    except exceptions.IllegalMachineNumberException as err:
        print(err)
        sys.exit(2)
    except exceptions.IllegalMachineInstructionException as err:
        print(err)
        sys.exit(2)
    
    outFile.close()

if __name__ == "__main__":
    main()