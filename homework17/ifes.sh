Создать скрипт, который принимает аргументом число и сравнивает, что число больше 0.
Если больше, то выводит  сообщение “{ЧИСЛО} положительное”
Если меньше, то выводит сообщение “{ЧИСЛО} отрицательное”
Создать скрипт, который принимает аргументом путь к файлу или директории  и выдает: существует файл, директория или нет

#!/bin/bash
if (( $1 >= 0 ))
then echo "$1 is positive"
else echo "$1 is nagative"
fi
mydir=/Users/user/Dropbox/Mac/Desktop/linux
if [ -d $mydir ]
then echo "The $mydir directory exists"
cd $mydir
ls
else echo "The $mydir directory does not exist"
fi