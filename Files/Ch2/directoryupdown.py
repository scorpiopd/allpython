import os
from subprocess import call
call(["ls","-l"])

print (os.listdir('.')) # current level
print (os.listdir('..')) # one level up
print (os.listdir('../..')) # two levels up


