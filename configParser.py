import exceptions as exc
import re

# Parser class that parses Turing machine tables and generates a description number.
class configParser:
    __s1 = "ə"
    __s0 = "_"
    # NOT ELEGANT constructor allows user input for first two symbols choice
    def __init__(self, s0 = "_", s1 = "ə"):
        self.__s0 = s0
        self.__s1 = s1
    
    # Dictionary that gives each symbol a unique encoding
    __symbols = {__s0 : "3", __s1 : "32"}

    # Keeps count of what symbol number we are on
    __symbolnum = 2

    # Pattern for keeping matching machine instructions
    __pattern = r"^\n?q(\d*[1-9]\d*) +([^ ]+) +([^ ]+) +([LRN]) +q(\d*[1-9]\d*)$"

    # Dictionary for translating direction instructions into lines.
    __translate = {
        "L" : "4",
        "R" : "5",
        "N" : "6"
    }

    # Main parse method, parses machine tables and returns a description number.
    def parse(self, number):
        output = ""
        configs = re.split(";", number)
        for x in configs[0:(len(configs)-1)]: # Ignore the last element since it will be blank
            if (re.match(self.__pattern, x)):
                seperated = self.__seperate(x)
                pretty = self.__makepretty(seperated)
                output += pretty
            else:
                raise exc.IllegalMachineInstructionException("The machine instructions passed are not valid")
        return output
    
    # Seperates out different parts of machine instruction
    def __seperate(self, instruction: str):
        parts = re.search(self.__pattern, instruction)
        result = [None] * 5
        for i in range(5):
            result[i] = parts.group(i+1)
        return result

    # Converts the parts of the machine instruction into a number
    def __makepretty(self, instruction : list):
        outnum = ""
        state = "3" + "1" * (int(instruction[0]))
        outnum += state
        outnum += self.__symbolrep(instruction[1])
        outnum += self.__symbolrep(instruction[2])
        outnum += self.__translate[instruction[3]]
        outstate = "3" + "1" * (int(instruction[4]))
        return outnum + outstate + "7"

    # Returns the symbol numerical representation for given symbol
    def __symbolrep(self, symbol: str):
        if symbol in self.__symbols:
            return self.__symbols[symbol]
        else: # If it's not in the dictionary, create a new entry with a new symbol.
            representation = "3" + "2" * self.__symbolnum
            self.__symbolnum += 1
            self.__symbols.update({symbol : representation})
            return representation