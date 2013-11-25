#!/bin/python
# Uses Python 2.7 Libraries

# Code and current implementation of Tessera Wrapper
# Notes: Future Implementations will probably run in C++ for speed reasons
# Proof of concept for this is going to be done in python since that's what Volatility uses. 
   
import os
import re
import hashlib
from subprocess import *
import datetime

# Taken from the Volatility Website to use Vol as a Library

# Start program header
print "====================================="
print " _____"
print "|_   _|"
print "  | | ___  ___ ___  ___ _ __ __ _"
print "  | |/ _ \/ __/ __|/ _ \ '__/ _` |"
print "  | |  __/\__ \__ \  __/ | | (_| |"
print "  \_/\___||___/___/\___|_|  \__,_|"
print "=====================================\n"

case = raw_input ('\nWould you like to make a case? (y/n) : ')

# Getting Case Information
if case == 'y':
	# Name the case; similar to Autopsy
	caseName = raw_input('Enter case name: ')
	# Get the Investigators' names and put them on a list; May use this for report generation
	invGtrs = []
	name = ''
	# Stop entering investigator names by entering a single '.' on a line
	print 'Enter investigator names: '
	while (name != '.'):
		name = raw_input()
		if (name != '.'):
			invGtrs.append(name)
	current = datetime.datetime.now()
	
	# Create an array to store the list of volatility commands used in the case
	commands = []

	# Create a directory to store case information in
	cwd = os.getcwd()
	caseDir = cwd+'/'+caseName
	# Check first to see if the directory already exists
	if (not os.path.isdir(caseDir)):
		os.mkdir(caseDir)
	print 'Case will be stored in '+caseDir+'\n'
else:
	# If no case is created, case information gets stored in CWD
	caseDir = os.getcwd()
	commands = []

# Get full path to image
image = raw_input('Enter full path to image: ')

# Check if the image exists
exist = os.path.isfile(image)

# If the image can't be found, ask for a new full path
if (exist != True):
	image = raw_input('Image location DNE.\nEnter full path to image: ')
	exist = os.path.isfile(image)

# Get the SHA-1 Hash for the image
print '\nChecking hash of image...\n'
f = open(image)
L = 128
m = hashlib.sha1()
while L == 128:
        block = f.read(128)
	m.update(block)
	L = len(block)	        
sha = m.hexdigest()
f.close()

print 'SHA-1 hash is: '+sha+'\n'

# Get the profile for the image
print 'Processing to discover profile...'

# Add volatility command to get profile to command list
commands.append('vol -f '+image+' imageinfo')
profile = Popen(['vol', '-f', image, 'imageinfo'], stdout=PIPE, stderr=PIPE)
out, err = profile.communicate()

# Make a regex to pull out the suggested profiles
out = re.search("Suggested Profile\(s\) : .*\n", out).group(0)
out = out[23:-1]
profile = out.split(', ')

# Choose an image from either the guessed setup, or use "other" image and enter your own
print '\nChoose an image profile: '
i = 1
for each in profile:
	print str(i)+'. '+each
	i+=1
print str(i)+'. Other'

# User makes Choice
prof = raw_input('Choice: ')

# Error Checking
while (not prof.isdigit()):
	prof = raw_input('Please choose a number: ')
# If 'other' was selected, have the user enter their own profile. This HAS to be correct; if they goof up the syntax, it's going to throw errors later
if (int(prof) == i):
	profile = raw_input('Enter profile: ')
else:
	prof=int(prof)-1
	profile = profile[prof]

######################### TO DO: determine if the profile chosen is legit

# Build the list of supported plugins from the plugins.txt list
cwd = os.getcwd()
f = open(cwd+'/plugins.txt')
plugins = f.readlines()
plugins = [line.strip() for line in plugins]
f.close()

# Choose whether or not to write results to a file
write = raw_input('\nWrite plugin results to file? (y/n) : ')
if (write == 'y'):
	write = True
else:
	write = False

# All info is loaded for case
print '\nCase successfully built.'

running = True

# Now we're ready for interactive mode!
while (running):
	entry = raw_input('Choose a plugin (Type exit to quit): ')
	if (entry in plugins):
		commands.append('vol -f '+image+' '+entry+' --profile='+profile)
		if (write):
			output = Popen(['vol', '-f', image, entry, '--profile='+profile], stdout=PIPE, stderr=PIPE)
			out, err = output.communicate()
			print out
			f = open(caseDir+'/'+entry, 'w')
			f.write(out)
			f.close()
		else: 
			call(['vol', '-f', image, entry, '--profile='+profile])
	if (entry == 'exit'):
		# Write the list of commands if a case was built
		if (case == 'y'):
			f = open(caseDir+'/command_list', 'w')
			f.write(str(commands))
			f.close()
		# Exit the program gracefully
		running = False
	print '\n'
