#!/bin/bash
# schema for the foor loop 
if [ condition ]
then
  echo "what to do"
elif [ string1 = string2 ]
then
  echo "what next to do"
else
  echo " the last thing to be don if all condition is false"
fi

# the comparism operator
[ "abc" = "abc" ] # if the string1 is exactly equal to string2(true)
[ "abc" != "abc" ]
[ 5 -eq 5 ]
[ 5 -ne 5 ]
[ 6 -gt 5 ]
[ 5 -lt 6  ]

# Advance string comparism 

[[ "abcd" = *bc* ]] # if abcd container bc (true)
[[ "abc" = ab[cd] ]] or  [["abd" = ab[cd] ]] #if 3rd character of abc is c or d(true)
[[ "abe" = "ab[cd]" ]] # if 3rd character of abc is c or d (false)
[[ "abc" > "bcd" ]] # if "abc" comes after "bcd" when sorted in alphabetic(lexographical) order(false)
[[ "abc" < "bcd" ]] # if "abc" comes before "bcd" when sorted in alphabetical (lexographical) order (true)

# Contional Operators
[ condion 1 ] && [ condition2 ] or [[ condtion1 && condition2 ]]
[ condion 1 ] || [ condition2 ] or [[ condtion1 || condition2 ]]

#Conditional Operator in files

[ -e FILE ] #if the file exist
[ -d FILE ] # if file exist and is a directory
[ -s FILE ] # If file exist and has size greater than zero
[ -x File ] # if the file is executable
[ -w File ] # if the file is writeable

