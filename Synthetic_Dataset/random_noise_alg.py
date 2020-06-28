#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Script: random_noise_alg.sh.
#	Author: Vitor Hugo Galhardo Moia, Ph.D student
#		ANDRÉ SEIKI KAMEYAMA, B.S student
# 			
#		Department of Computer Engineering and Industrial Automation (DCA)
#		School of Electrical and Computer Engineering (FEEC)
#		University of Campinas (UNICAMP)
#		Campinas, SP, Brazil 13083-852
#		Email: vhgmoia@dca.fee.unicamp.br / vitormoia@gmail.com
#		Page: http://www.dca.fee.unicamp.br/~vhgmoia/
#
#	Purpose: This python script perform random changes on objects
#		(i) inserting a new word;
#		(ii) deleting an existing word;
#		(iii) swapping two words;
#    		(iv) substituting a word for another word;
#    		(v) replacing 10 occurrences of a character for another character;
#    		(vi) deleting 10 occurrences of a character.
#
#	INPUT:
#	1. File path of object sizes information in the form: OBJECTNAME|SIZE. Each pair is separated by a newline character
#	2. Number of objects created for each item in the list of objects given as argument
#
#	OUTPUT:
#	Randomly changed object
#
#   November, 20th 2019	


import sys
import os
import string
import random
import math


def insert_word(filedata):

	# Choosing words
	words = filedata.split()
	word_1 = random.choice(words)
	word_2 = random.choice(words)

	#Avoiding repeated words
	while word_1 == word_2:
		word_2 = random.choice(words)

	#Inserting word and making sure to not overwrite any other one
	aux = ""
	aux = word_1 + " " + word_2 + " "
	filedata = filedata.replace(word_1, aux, 1)

	return filedata, len(word_2)


def substitute_word(filedata):

	#choosing words
	words = filedata.split()
	word_1 = random.choice(words)
	word_2 = random.choice(words)	

	#Avoiding repeated words
	while word_1 == word_2:
		word_2 = random.choice(words)

	#Replacing one word for another
	filedata = filedata.replace(word_1, word_2, 1)

	return filedata, len(word_1)


def delete_word(filedata):

	words = filedata.split()
	w = random.choice(words)	

	#Deleting chosen word from file
	filedata = filedata.replace(w, "", 1)

	return filedata, len(w)


def swap_word(filedata):

	words = filedata.split()
	word_1 = random.choice(words)
	word_2 = random.choice(words)	

	#avoiding repeated words
	while word_1 == word_2:
		word_2 = random.choice(words)

	#Replacing one word for another
	filedata = filedata.replace(word_1, '%temp%', 1).replace(word_2, word_1, 1).replace('%temp%', word_2, 1)

	return filedata, (len(word_1) + len(word_2))/2


def replace_10_chars(filedata):

	c1 = random.choice(string.letters)
	c2 = random.choice(string.letters)

	while filedata.count(c1) < 10:
		c1 = random.choice(string.letters)

	#Replacing chosen character by another one
	filedata = filedata.replace(c1, c2, 10)

	return filedata, 10


def delete_10_chars(filedata):

	c = random.choice(string.letters)

	while filedata.count(c) < 10:
		c = random.choice(string.letters)

	#removing chosen char from file
	filedata = filedata.replace(c, "", 10)

	return filedata, 10


#Program arguments
input_file=sys.argv[1]
filesize=sys.argv[2]
p_to_change=sys.argv[3]
output_file=sys.argv[4]

bytes_to_change=(float(filesize)*float(p_to_change))/100

#initializing internal state of the random number generator
random.seed()

with open(input_file, 'r') as file :
	filedata = file.read()

while bytes_to_change > 0:

	random_op=random.randint(0,5)

	if(random_op == 0):
		filedata,bytes_changed=insert_word(filedata)
	elif (random_op == 1):
		filedata,bytes_changed=substitute_word(filedata)
	elif (random_op == 2):
		filedata,bytes_changed=delete_word(filedata)
	elif (random_op == 3):
		filedata,bytes_changed=swap_word(filedata)
	elif (random_op == 4):
		filedata,bytes_changed=replace_10_chars(filedata)
	elif (random_op == 5):
		filedata,bytes_changed=delete_10_chars(filedata)

	bytes_to_change = bytes_to_change - bytes_changed

with open(output_file, 'w') as file:
  	file.write(filedata)
