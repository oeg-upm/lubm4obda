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

try:
    int(r1)
except:
    print(colored("\nERROR: you need to provide a valid integer for the scale factor.\n", attrs=['bold']))
    sys.exit()

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
    output_file_name = f'lubm4obda_{r1}_mysql.sql'
    os.system(f"cat /code/schema_university.sql > {output_path}{output_file_name}")
elif r2 == 'PostgreSQL':
    output_file_name = f'lubm4obda_{r1}_postgresql.sql'
    os.system(f"cat /code/schema_university_psql.sql > {output_path}{output_file_name}")

os.system(f"cat /temp/Universities-1.sql >> {output_path}{output_file_name}")

if r2 == 'SQL':
    os.system(f"echo 'ALTER TABLE graduateStudent CHANGE age undergraduateDegreeYear int;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduateStudent set undergraduateDegreeYear=\"2010\" where undergraduateDegreeYear=20;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduateStudent set undergraduateDegreeYear=\"2011\" where undergraduateDegreeYear=21;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduateStudent set undergraduateDegreeYear=\"2012\" where undergraduateDegreeYear=22;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduateStudent set undergraduateDegreeYear=\"2013\" where undergraduateDegreeYear=23;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduateStudent set undergraduateDegreeYear=\"2014\" where undergraduateDegreeYear=24;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduateStudent set undergraduateDegreeYear=\"2015\" where undergraduateDegreeYear=25;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduateStudent set undergraduateDegreeYear=\"2016\" where undergraduateDegreeYear=26;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduateStudent set undergraduateDegreeYear=\"2017\" where undergraduateDegreeYear=27;' >> {output_path}{output_file_name}")
elif r2 == 'PostgreSQL':
    os.system(f"echo 'ALTER TABLE graduatestudent RENAME COLUMN age TO undergraduatedegreeyear;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduatestudent set undergraduatedegreeyear=2010 where undergraduatedegreeyear=20;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduatestudent set undergraduatedegreeyear=2011 where undergraduatedegreeyear=21;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduatestudent set undergraduatedegreeyear=2012 where undergraduatedegreeyear=22;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduatestudent set undergraduatedegreeyear=2013 where undergraduatedegreeyear=23;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduatestudent set undergraduatedegreeyear=2014 where undergraduatedegreeyear=24;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduatestudent set undergraduatedegreeyear=2015 where undergraduatedegreeyear=25;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduatestudent set undergraduatedegreeyear=2016 where undergraduatedegreeyear=26;' >> {output_path}{output_file_name}")
    os.system(f"echo 'UPDATE graduatestudent set undergraduatedegreeyear=2017 where undergraduatedegreeyear=27;' >> {output_path}{output_file_name}")


print('')
print(colored("##########################################################", attrs=['bold']))
print(colored("Generation finished! The data is in the current directory.", attrs=['bold']))
print(colored("##########################################################", attrs=['bold']))
print('')
