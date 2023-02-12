Написать скрипт, который запрашивает число и проверяет. что оно больше 15, но меньше 45 и выдает результат
Написать скрипт, который запрашивает число и проверяет, что число меньше -1 или равно 45 и выдает результат
#!/bin/bash
printf "enter a number"
read input
if (( $input >=15 && $input <=45 ))
then echo "$input is good"
else echo "$input is not good"
fi

#!/bin/bash
printf "enter a number"
read input
if (( $input <= -1 || $input == 45 ))
then echo "$input is good"
else echo "$input is not good"
fi

