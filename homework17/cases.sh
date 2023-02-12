Напишите скрипт, который будет запрашивать букву на вход и затем выдавать результатом в каком она регистре, либо это число или это спецсимвол

#!/bin/bash
printf "enter a letter"
read input
case $input in
    [0-9]) echo "$input is digit" ;;
    [A-Z]) echo "$input is upper" ;;
    [a-z]) echo "$input is lower" ;;
esac