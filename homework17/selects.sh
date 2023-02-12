Напишите скрипт, который будет выводить сообщение “Хотите ли Вы установить python?” и варианты ответа “1) Да 2) Нет” 
Если Да, то выдать сообщение “Вы выбрали установить python”
Если Нет, то выдать сообщение “Уходи дверь закрой”

#!/bin/bash
printf "Do you want to install python?"
read answer
case $answer in
Yes) echo "You chose to install python" ;;
No) echo "Go away close the door" ;;
esac