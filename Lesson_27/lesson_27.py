import json, csv


# with open("purchase_1.json") as purchase_json:
#     # convert data into python dict
#     purchase_data = json.load(purchase_json)

# print(purchase_data, purchase_data["user"])
# # Prints 'ellen_greg'


# turn_to_json = {
#     "eventId": 674189,
#     "dateTime": "2015-02-12T09:23:17.511Z",
#     "chocolate": "Semi-sweet Dark",
#     "isTomatoAFruit": "True",
# }

# with open("output.json", "w") as json_file:
#     json.dump(turn_to_json, json_file)

# print(turn_to_json)

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
