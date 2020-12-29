import csv 
import json 
from datetime import datetime

def get_em(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath,) as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 
    

        #convert each csv row into python dict
        for row in csvReader:
            
            for rows in row:
                
                if 'arrived_time' in rows:
                        row[rows] = datetime.strptime(row[rows].strip(),'%Y%m%d%H%M%S').strftime("%Y-%m-%d %H:%M:%S")
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w') as jsonf: 
        jsonString = json.dumps(jsonArray)
        jsonf.write(jsonString)
          
csvFilePath = r'data_in.csv'
jsonFilePath = r'Data_out.json'
get_em(csvFilePath, jsonFilePath)
