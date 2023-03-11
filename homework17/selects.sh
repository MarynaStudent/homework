Напишите скрипт, который будет выводить сообщение “Хотите ли Вы установить python?” и варианты ответа “1) Да 2) Нет” 
Если Да, то выдать сообщение “Вы выбрали установить python”
Если Нет, то выдать сообщение “Уходи дверь закрой”

#!/bin/bash
PS3= "Do you want to install python?"
echo
select answer in "yes" "no"
do
case $answer in
 yes) echo "You chose to install python" ;;
 no) echo "Go away close the door" ;;
 esac && break
done