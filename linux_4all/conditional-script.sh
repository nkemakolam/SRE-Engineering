#!/bin/bash
#Develop a shell script /home/bob/print-month-name.sh that accepts the number of a month as input and prints the name of the respective month. eg ./print-month-name.sh 1 should print January and ./print-month-name.sh 5 should print May. Also keep these in mind.

#The script must accept a month number as a command line argument.

#If a month number is not provided as command line argument, the script must exit with the message No month number given.

#The script must not accept a value other than 1 to 12. If not the script must exit with the error Invalid month number given.
#Use -z $1 to check for command line argument.

month_number=$1

if [ -z $month_number ]
then
  echo "No month number given. Please enter a month number as a command line argument."
  echo "eg: ./print-month-number 5"
  exit
fi

if [[ $month_number -lt 1 ]] || [[ $month_number -gt 12 ]]
then
  echo "Invalid month number given. Please enter a valid number - 1 to 12."
  exit
fi

if [ $month_number -eq 1 ]
then
  echo "January"
elif [ $month_number -eq 2 ]
then
  echo "February"
elif [ $month_number -eq 3 ]
then
  echo "March"
elif [ $month_number -eq 4 ]
then
  echo "April"
elif [ $month_number -eq 5 ]
then
  echo "May"
elif [ $month_number -eq 6 ]
then
  echo "June"
elif [ $month_number -eq 7 ]
then
  echo "July"
elif [ $month_number -eq 8 ]
then
  echo "August"
elif [ $month_number -eq 9 ]
then
  echo "September"
elif [ $month_number -eq 10 ]
then
  echo "October"
elif [ $month_number -eq 11 ]
then
  echo "November"
elif [ $month_number -eq 12 ]
then
  echo December
fi