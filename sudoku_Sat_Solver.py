#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:15:00 2023

@author: juanmi
"""


import argparse
from typing import Tuple

from pysat.formula import CNF
from pysat.solvers import Solver #Specify Solver if necessary

import math

import string

import os

import pickle
import json

import time
import re


def display_solution(model, number, all_solutions):
    
    
    solution = {}
    for literal in model:
        if 0 < literal <= N*N*N:
            # The positive encoding literals give us the values
            (row, column, value) = var_inv(literal)
            if (row, column) in solution:
                err(f'Found a solution with two values '
                    f'for the cell at ({row}, {column})')
            solution[(row, column)] = value

    validate_solution(solution, clues)
    

    if all_solutions == False:
        size = "9x9/" if "9x9" in clues else "25x25/"         
        
    else:
        size = "all9x9/" if "all9x9" in clues else "all25x25/" 
        
    with open('./outputs/' + size + os.path.basename(clues), 'w+') as f:                
        for row in range(1, N+1):
            f.write(' '+' '.join([str(solution[(row, column)])
                                for column in range(1, N+1)]))
            f.write('\n')
        filename = './outputs/' + size + os.path.basename(clues) + '_' + str(number) + '.html'
        
        with open(filename, 'w+') as f2: 
            
            grid = open('./outputs/' + size + os.path.basename(clues)).read()
            
            first = str(D)+'n'
            second = 'n+'+str(N)
            
            html = '''
                <html>
                <head>
                <style>
                table {
                  border-collapse: collapse;
                }
                
                td {
                  border: 1px solid black;
                  width: 30px;
                  height: 30px;
                  text-align: center;
                }
                
                tr:nth-child(
                '''
            html+= first 
            html+= '''
                ) td {
                  border-bottom: 10px solid black; 
                }
                
                tr:nth-child(
                '''
            html+= second
            html+= '''
                ) td {
                  border-bottom: 1px solid black;
                } 
                
                td:nth-child(
                '''
            html+= first 
            html+= '''
                ) {
                  border-right: 10px solid black;
                }
                
                td:nth-child(
                '''
            html+= second 
            html+= '''
                ) {
                  border-right: 1px solid black; 
                }
                </style>
                </head>
                <body>
                '''
                
            html += '<table>'
    
            for line in grid.split('\n'):
              html += '<tr>'
    
              for num in line.split():
                html += f'<td>{num}</td>'
    
              html += '</tr>'
    
            html += '</table>'
            
            html += '''
                </body>
                </html>
                '''
            
            f2.write(html)
        

def encode(clues):
    
    cnf = CNF()

    
    
    return cnf



def solve_and_decode(clues, cnf, all_solutions):



def validate_solution(solution, clues):
    
    

def solve_sudoku(clues, all_solutions):
    
    cnf = encode(clues)
    solve_and_decode(clues, cnf, all_solutions)
    print("Done!")

if __name__ == '__main__':
    
    files_9x9 = [os.path.join('./inputs/9x9/', f) for f in os.listdir('./inputs/9x9/') if f.endswith('.json')]
    files_25x25 = [os.path.join('./inputs/25x25/', f) for f in os.listdir('./inputs/25x25/') if f.endswith('.json')]
    
    files_all9x9 = [os.path.join('./inputs/all9x9/', f) for f in os.listdir('./inputs/all9x9/') if f.endswith('.json')]
    
    # Create directories
    dirs = [
        './outputs',
        './outputs/9x9',
        './outputs/all9x9',
        './outputs/25x25',
        './outputs/all25x25'
    ]
    
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            
    # The symbols allowed in the Sudoku instance text file
    # DIGITS from 1 to 9 in 9x9, A to Y -> 1 to 25 in 25x25
    DIGITS = {}
    for i in range(1, 9+1):
        DIGITS[str(i)] = i
          
    NOCLUE = '.'
    
    letters = string.ascii_uppercase[:25]
    digits = range(1, 25+1)
    letter_to_num = {}
    for letter, digit in zip(letters, digits):
        letter_to_num[letter] = digit
        
    
    for clues in files_9x9:
        with open(clues, "rb") as f:
            lines = json.load(f)
            
            is_square = int(3 + 0.5) ** 2 == len(lines)
            if not is_square:
                print("input incorrect!!!")
                exit(0)
    
            D = int(math.sqrt(len(lines))) 
            N = D*D 
        
            DIGITS = {}
            for i in range(1, N+1):
                DIGITS[str(i)] = i
                  
            NOCLUE = '.'
            
            solve_sudoku(clues, False)
    
    
    for clues in files_all9x9:
    
        if not re.search(r"_7\.json$|_8\.json$|_9\.json$|_10\.json$", clues): #REMOVE ONLY FOR MAXIMUM GRADE ACTIVITIES
            with open(clues, "rb") as f:
                lines = json.load(f)
                
                is_square = int(3 + 0.5) ** 2 == len(lines)
                if not is_square:
                    print("input incorrect!!!")
                    exit(0)
        
                D = int(math.sqrt(len(lines)))
                N = D*D
            
                print(clues)
                solve_sudoku(clues, True)
        
    
    for clues in files_25x25[:20]: #REMOVE ONLY FOR MAXIMUM GRADE ACTIVITIES
        
        with open(clues, "rb") as f:
            lines = json.load(f)
            
            is_square = int(5 + 0.5) ** 2 == len(lines)
            if not is_square:
                print("input incorrect!!!")
                exit(0)
                
            D = int(math.sqrt(len(lines))) 
            N = D*D 
            
            print("Solving: " + clues)
            solve_sudoku(clues, False)
            print(clues + " solved!")