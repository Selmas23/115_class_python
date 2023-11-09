#
import json


#Create the data dictionary
data = {

        'name': 'Selma Torres',
        'age':26,
        'city': 'San Fransisco,CA',
        'interests': ['cooking','gym','painting'],
        'is_student': True

}

##
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')


#
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)