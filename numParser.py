import exceptions as exc
import re

# Parser class that parses Turing machine description number and returns a generated machine table
class numParser:
    def __init__(self, s0 = "_", s1 = "ə"): # offers the user option to change the default first two symbols
        self.s0 = s0
        self.s1 = s1
    
    # Regex pattern used to match instruction lines
    __pattern = "^(31+)(32*)(32*)([456])(31+)$"

    # Dictionary that translates movement instructions
    __translate = {
        "4" : "L",
        "5" : "R",
        "6" : "N"
    }

    # Main parse method, takes a string of a valid machine descriptuion number and generatess machien table
    def parse(self, number):
        output = ""
        configs = re.split("7", number)
        for x in configs[0:(len(configs)-1)]:
            if (re.match(self.__pattern, x)):
                seperated = self.__seperate(x)
                pretty = self.__makepretty(seperated)
                output += pretty
            else:
                raise exc.IllegalMachineNumberException("The number passed is not valid")
        return output
    
    # sepearates the 5 elements of the instruction into a list
    def __seperate(self, nums: str):
        parts = re.search(self.__pattern, nums)
        result = [None] * 5
        for i in range(5):
            result[i] = parts.group(i+1) # +1 needed because regex capture groups start at index 1
        return result

    # Takes the list of seperated elemnts and translates them into readable instructions
    def __makepretty(self, config : list):
        out = ""
        out += "q{} ".format(str(self.__countNums(config[0])))
        sym1 = "S{} ".format(str(self.__countNums(config[1])))
        out += self.__specialSymbol(sym1)
        sym2 = "S{} ".format(str(self.__countNums(config[2])))
        out += self.__specialSymbol(sym2)
        out += "{dir} ".format(dir = self.__translate[config[3]])
        out += "q{};\n".format(str(self.__countNums(config[4])))
        return out
    
    # Helper method that counts number of 1s or 2s in a string
    def __countNums(self, str: str):
        i=0
        for x in str:
            if(x == '2' or x == '1'):
                i +=1
        return i

    # Helper method that makes S0 and S1 into special symbols (specified in constructor)
    def __specialSymbol(self, symbol: str):
        if(symbol == "S0 "):
            return "{} ".format(self.s0)
        elif(symbol == "S1 "):
            return "{} ".format(self.s1)
        else:
            return symbol