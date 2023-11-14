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

#Writing data to a JSON file
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')


#Created loaded data from JSON file
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

#Modifiying the data. Added interests to the end(append)
loaded_data['age'] = 27
loaded_data['interests'].append('Shopping')

#Writing the modified data back to JSON file
with open('data.json', 'w') as json_file:
   json.dump(loaded_data, json_file, indent=4)

print('modified data written to data.json')
