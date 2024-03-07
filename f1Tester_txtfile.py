from urllib.request import urlopen
import json
import csv

response = urlopen('https://api.openf1.org/v1/car_data?driver_number=55&session_key=9159&speed>=315')
carData = json.loads(response.read().decode('utf-8'))

#defines the field names in the dictionary values from the dataset given
carFields = ['driver_number', 'rpm','speed','throttle','brake','drs','date','session_key','meeting_key',
             'n_gear']
#creates a variable of the file name e.g f1tester
fileName = "f1tester.txt"
print(carData)
#creates and opens the csv file in write mode to stop repeating entries
#(instead of using append mode)

#removes all whitespace in current text file and imports the stripped
#data into a new file
with open( 
    "f1tester.txt", 'r') as r, open( 
        'output.txt', 'w') as o: 
    for line in r: 
        #strip() function 
        if line.strip(): 
            o.write(line)
            
f = open("output.txt", "r") 
print("New text file:\n",f.read())


