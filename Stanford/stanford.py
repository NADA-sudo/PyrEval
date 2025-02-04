# Script for running StanfordCoreNLP

#    Copyright (C) 2017 Yanjun Gao

#    This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Aug 6, 2017
# Step 0, move this file to stanford-corenlp folder 
# mode: 1: peer summries; 2: wise_crowd_summaries, 3:test_summaries 
# Usage: python stanford.py mode 

import os
import sys
#from lib_preprocessing import *

path_ = sys.argv[1]
mode = sys.argv[2]
pyrEval = sys.argv[3]
if len(sys.argv) == 5:
	java_exec = sys.argv[4]
else:
	java_exec = 'java'


# Clean Summary before XML dump
if os.path.isdir(path_):
	for filename in os.listdir(path_):
		if filename[0] != '.':
			full_path = os.path.join(path_,filename)
			with open(full_path, 'r') as infile:
				lines = infile.readlines()
			clean = []
			for line in lines:
				line = line.replace("'", '').replace('`', '')
				# if '.' in line:
				# 	ind = line.index('.')
				# 	if len(line) == ind + 1:
				# 		pass
				# 	elif line[ind + 1] != ' ':
				# 		line[ind] = ' '
				clean.append(line)
			with open(full_path, 'w') as outfile:
				for line in clean:
					outfile.write(line)

	filename = os.path.abspath(path_)
	print "current filename", filename
	print mode
	if int(mode) == 1:
		outpath = os.path.join(pyrEval, 'Preprocess', 'peer_summaries')
	elif int(mode) == 2:
		outpath = os.path.join(pyrEval, 'Preprocess', 'wise_crowd_summaries')
	#elif int(mode) == 3:
		#outpath = pyrEval + "/Preprocess/test_summaries"
	else:
		print "Option doesn't exist!!!"
	if outpath:
		print outpath
		# TODO: Very clunky solution to set max heap size here
		command2 = java_exec + ' -Xmx2g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,parse,depparse -file ' + filename + ' -outputDirectory ' + outpath
		os.system(command2)

