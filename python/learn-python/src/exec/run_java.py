#!/usr/bin/python
"""
CLASSPATH=/home/nigel/projects/python/learn-python/out/production/learn-python
~/projects/python/learn-python/src/exec $ ./run_java.py -cp $CLASSPATH exec.com.Sample -margs "what's up doc"

"""

import argparse
import os
import subprocess
from subprocess import STDOUT, PIPE

parser = argparse.ArgumentParser(description='runs a java program.')
parser.add_argument('-cp', metavar='C', type=str, help='the classpath')
parser.add_argument('main', type=str, help='the main class')
parser.add_argument('-margs', metavar='N', type=str, nargs='+', help='program arguments')
parser.add_argument('-stdin', type=str, help='input from stdin')

args = parser.parse_args()

cmd = ['java']

my_env = os.environ.copy()
if "CLASSPATH" not in my_env.keys():
    my_env["CLASSPATH"] = ""
my_env["CLASSPATH"] += "/home/nigel/projects/python/learn-python/out/production/learn-python"

if args.cp is not None:
    my_env["CLASSPATH"] += ":" + args.cp

print "classpath: ", my_env["CLASSPATH"]

cmd.append(args.main)

if args.margs is not None:
    cmd.extend(args.margs)

print "running command: ", cmd

proc = subprocess.Popen(cmd, env=my_env, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
stdout, stderr = proc.communicate(args.stdin)
print (stdout)
