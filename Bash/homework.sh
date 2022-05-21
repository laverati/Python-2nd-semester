#!/bin/bash

#Реализовать скрипт на bash, который на основе файла 
#имён пользователей и их паролей формирует другой файл 
#с именами и пользователей и хэшами паролей

let i=0
echo -n > new_passwords.txt
while IFS= read line
do (( i++ ))
if  [ $((i % 2)) == 0 ]
then
  echo -n "$line" | md5sum >> new_passwords.txt
else
    echo "$line" >> new_passwords.txt
fi
done < passwords.txt
echo $passwords