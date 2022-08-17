import re

def getBrailFromLetter(char):
    brillesLib = ["000000", "100000", "110000", "100100", "100110", "100010", "110100", "110110", "110010", "010100", "010110", "101000", "111000", "101100", "101110", "101010", "111100", "111110", "111010", "011100", "011110", "101001", "111001", "010111", "101101", "101111", "101011"]
    captialize = "000001"

    def getIndex(char): 
        asciiChars = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for index, letter in enumerate(asciiChars):
            if char == letter:
                return index
    
    if re.findall("[a-z]", char):
        return brillesLib[getIndex(char)]
    elif re.findall("[A-Z]", char):
        return captialize + brillesLib[getIndex(char.lower())]
    else:
        return brillesLib[0]

def solution(str):
    if (len(str) < 51):
        string = ""
        for i in str:
            string += getBrailFromLetter(i)
        return string
    else:
        return "Please enter an input with less than 50 characters"

# print(solution("Hello World"))
# print(solution("This is a test that will verify that the 50 characters limit actually works. Should return 'Please enter an input with less than 50 characters'..."))