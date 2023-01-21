#!/bin/bash -x
# checking if the input file is empty
if [[ ! $input_file ]]
then 
echo "Error : nput file is not configured"
exit 1
fi
# checking if the file does not  exist
if [[ ! -e  $input_file ]]
then 
echo "Error : nput file $iput_file does not exist"
exit 1
fi
# checking if the first argument is not empty
if [[ ! $1 ]]
then 
echo "Error : missing parameter : container name"
exit 1
fi
container="$1"
if [[ $2 ]]
then 
directory="$2"
exit 0
else 
 directory="$HOME/reports"
fi
# callling the head command 
head Mountain.csv
mkdir -p -- "$directory"

if grep -- "$container" $input_file > "$directory/${container}_report.csv"
then
echo "wrote report $directory/$container.csv "
else 
echo "ontainer  $container not found in the $input_file"
fi
