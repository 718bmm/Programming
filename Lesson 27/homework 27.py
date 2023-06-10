import json, csv

compromised_users = []
with open('passwords.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        compromised_users.append(row[0])
        print(row[0])

with open('compromised_users.txt', 'w') as txt_file:
    for user in compromised_users:
        txt_file.write(user + '\n')

boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success",
}

with open('boss_message.json', 'w') as json_file:
    json.dump(boss_message_dict, json_file)

new_password = r"""           
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
with open('new_passwords.csv', 'w') as csv_file:
    csv_file.write(new_password)