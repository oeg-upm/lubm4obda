#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import json
import signal
import sys
import copy
from termcolor import colored
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

os.system("figlet -f standard -c LUBM4OBDA")

custom_style_3 = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    #Token.Selected: '',  # default
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})

run_path = "/repo/LinGBM/tools/datasetgen/"
output_path = "/output/"

q1 = [
    {
        'type': 'input',
        'name': 'q',
        'message': 'Please, specify the scale factor:',
    }
]

r1 = prompt(q1)["q"]

q2 = [
    {
        'type': 'list',
        'name': 'q',
        'message': 'Select the output format:',
        'choices': [

            {
                'name': 'MySQL',
                'value': 'SQL'
            },
            {
                'name': 'PostgreSQL',
                'value': 'PostgreSQL'
            }

        ]

    }
]

r2 = prompt(q2)["q"]

print('\n')


os.system(f'{run_path}./generate.sh -o /temp/ --consolidate Full --format {r2} -u {r1}')


if r2 == 'SQL':
    os.system(f"cat /code/schema_university.sql > {output_path}universities.sql")
elif r2 == 'PostgreSQL':
    os.system(f"cat /code/schema_university_psql.sql > {output_path}universities.sql")

os.system(f"cat /temp/Universities-1.sql >> {output_path}universities.sql")

if r2 == 'SQL':
    os.system(f"echo 'ALTER TABLE graduateStudent CHANGE age undergraduateDegreeYear int;' >> {output_path}universities.sql")
elif r2 == 'PostgreSQL':
    os.system(f"echo 'ALTER TABLE graduateStudent RENAME COLUMN age TO undergraduateDegreeYear;' >> {output_path}universities.sql")


print('')
print(colored("##########################################################", attrs=['bold']))
print(colored("Generation finished! The data is in the current directory.", attrs=['bold']))
print(colored("##########################################################", attrs=['bold']))
print('')
