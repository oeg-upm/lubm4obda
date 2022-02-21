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
output_path = "/output/output/"

q1 = [
    {
        'type': 'input',
        'name': 'q',
        'message': 'Please, specify the scale factor',
    }
]

r1 = prompt(q1)["q"]

q2 = [
    {
        'type': 'list',
        'name': 'q',
        'message': 'Choose the output format:',
        'choices': [
            {
                'name': 'NTRIPLES',
                'value': 'NTRIPLES'
            },
            {
                'name': 'TURTLE',
                'value': 'TURTLE'
            },
            {
                'name': 'SQL',
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

os.mkdir(output_path)

os.system(run_path+"./generate.sh -t 4 -o "+output_path+" --consolidate Maximal --format "+str(r2)+" -u "+str(r1))


print(colored("The generated data is in the current folder", 'blue'))






def signal_handler(sig, frame):
    print('\nBye! ')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C to exit')
signal.pause()
