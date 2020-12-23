# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:47:52 2020

@author: kevst
"""
#create an interpreter for MiniStringFuck

import re

def my_first_interpreter(code):
    #Remove characters that aren't + or .
    code_pure = re.findall(r"(\+|\.)", code)
    #print(code_pure)
    msf = "".join(code_pure)
    #print(program)
    index = 0
    output = ""
    for char in msf:
        if char == "+":
            index = (index + 1) % 256
        elif char == ".":
            output += chr(index)
    return output   
    
test = my_first_interpreter("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.")
print(test)