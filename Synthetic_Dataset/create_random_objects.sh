#!/bin/bash

#   Script: create_random_objects.sh.
#	Author: Vitor Hugo Galhardo Moia, Ph.D student
# 		Department of Computer Engineering and Industrial Automation (DCA)
#		School of Electrical and Computer Engineering (FEEC)
#		University of Campinas (UNICAMP)
#		Campinas, SP, Brazil 13083-852
#		Email: vhgmoia@dca.fee.unicamp.br / vitormoia@gmail.com
#		Page: http://www.dca.fee.unicamp.br/~vhgmoia/
#
#	Purpose: This script creates random objects. Duplicates of each created item are made with the addition of random changes.
#
#	INPUT:
#	1. File path of object sizes information in the form: OBJECTNAME|SIZE. Each pair is separated by a newline character
#	2. Number of objects created for each item in the list of objects given as argument
#
#	OUTPUT:
#	Random object and a duplicate of it with random changes
#
#	November, 20th 2019	

if [ $# -lt 2 ];
then	
	echo "Running this script requires two arguments:"
	echo "   1. File path of object sizes information"
	echo "   2. Number of objects created for each item in the list of objects given as argument"
	exit 1
fi

f_sizes=$1			
num_duplicates=$2

#how many bytes (in percentage) will be changed in the duplicated version of the object
#note that passing two or more values, two or more duplicates will be created, one for each value
percentages=( "0.5" "1.0" "1.5" "2.0" "2.5" "5.0" "10.0" "25.0" )

while IFS='' read -r line || [[ -n "$line" ]]; do

	set -f; IFS='|'
	set -- $line
	name=$1
	file_size=$2

	i=1

	while [ $i -le $num_duplicates ];
	do

		new_obj_name="$name-$i.bin"
		
		# Generate random data
		dd if=/dev/urandom of=$new_obj_name bs=$file_size count=1 iflag=fullblock

		#Performing changes on the duplicate version
		for p_changes in "${percentages[@]}"
		do
			output_file="$name-$i-$p_changes.bin"

			#calling a python script to perform the changes
			python random_noise_alg.py $new_obj_name $file_size $p_changes $output_file

		done

		i=$((i + 1));

	done

done < "$f_sizes"