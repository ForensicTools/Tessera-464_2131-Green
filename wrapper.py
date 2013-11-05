#!/bin/python
# Will use Python 2.7 Libraries

# Code and Pseudocode for Current Implementation of Tessera Wrapper
# Haven't done a test run for this yet. Don't advise that anyone should make a run at this yet
# Notes: Future Implementations will probably run in C++ for speed reasons
# Proof of concept for this is going to be done in python since that's what Volatility uses. 

'''        
import os
# Taken from the Volatility Website to use Vol as a Library
import volatility.conf as conf
import volatility.registry as registry
import volatility.commands as commands
import volatility.addrspace as addrspace
import volatility.utils as utils
registry.PluginImporter()
config = conf.ConfObject()
registry.register_global_options(config, commands.Command)
registry.register_global_options(config, addrspace.BaseAddressSpace)

# Start program header
print '
===================================== 
 _____                            
|_   _|                           
  | | ___  ___ ___  ___ _ __ __ _ 
  | |/ _ \/ __/ __|/ _ \ '__/ _` |
  | |  __/\__ \__ \  __/ | | (_| |
  \_/\___||___/___/\___|_|  \__,_|
====================================='

# Name the case; similar to Autopsy
caseName = raw_input('\nEnter case name: ')

# Get the Investigators' names and put them on a list; May use this for report generation
invGtrs = []
name = ''
print 'Enter investigator names: '
while (name != '.'):
	name = raw_input()
	if (name != '.'):
		push(invGtrs, name)

# Get full path to image
image = raw_input('Enter full path to image: ')

# Check if the image exists
exist = os.path.isfile(image)

# If the image can't be found, ask for a new full path
if (exist != true):
	image = raw_input('Image location DNE.\nEnter full path to image: ')
	exist = os.path.isfile(image)

########################### SEMI-PSEUDOCODE FROM HERE ON OUT
########################### Don't know how to call vol plugins from library yet
########################### import volatility.plugins.imageinfo as imageinfo?

# Get the profile for the image
profile = (could do an exec(python vol.py -f image imageinfo)
profile = split(pull out first suggested profile)

print 'Profile appears to be '+profile+'. Is this correct?'
profCor = raw_input()
if (profCor == 'false')
	profile = raw_input('Enter profile: ')


# Taken from the Volatility website ot use Vol as a library
config.parse_options()
config.PROFILE=profile
config.LOCATION=image
import volatility.plugins.taskmods as taskmods
p = taskmods.PSList(config)
for process in p.calculate():
       	print process

######################### TO DO: determine a way to verify case successfully built or not
# For right now, assume case built

print '\nCase successfully built.'

running = true
while (running):
	raw_input('Get what data from image?')

'''
