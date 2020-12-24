# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:10:20 2020

@author: kevst
"""
#Make custom Smallfuck interpreter

import re

def interpreter(code, tape):
    #Filter out non-command characters
    code_pure = re.findall(r"(\>|\<|\*|\[|\])", code)
    sf = "".join(code_pure)
    #Convert tape to list so that elements are mutable
    tape_list = []
    for bit in tape:
        tape_list.append(bit)
    #Keep track of pointer and instruction position
    pointer = 0
    instr = 0
    brack_pos = [] #Contains positions of "[" brackets
    while instr < len(sf):
        #If pointer goes out of bounds then end the program
        if pointer >= len(tape_list) or pointer < 0:
            return "".join(tape_list)
        #"*" flips the current bit
        if sf[instr] == "*":
            if tape_list[pointer] == "1":
                tape_list[pointer] = "0"
            elif tape_list[pointer] == "0":
                tape_list[pointer] = "1"
            instr += 1
        #Move right one bit
        elif sf[instr] == ">":
            pointer += 1
            instr += 1
        #Move left one bit
        elif sf[instr] == "<":
            pointer -= 1
            instr += 1
        elif sf[instr] == "[":
            #If pointer is on 0, skip the loop
            if tape_list[pointer] == "0":
                brack_cnt = 1
                while brack_cnt != 0:
                    instr += 1
                    if sf[instr] == "[":
                        brack_cnt += 1
                    elif sf[instr] == "]":
                        brack_cnt -= 1
                instr += 1
            #If pointer is 1, step into the loop
            elif tape_list[pointer] != "0":
                brack_pos.append(instr)
                instr += 1
        elif sf[instr] == "]":
            if tape_list[pointer] == "0":
                instr += 1
            elif tape_list[pointer] != "0":
                instr = brack_pos[-1] 
                brack_pos.pop()
        
    return "".join(tape_list)

print(interpreter("[*[>]]", "000")) 
