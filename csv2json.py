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

            payload = {}
            row.update({'e_flag': 'False'})

            for rows in row:

                if 'arrived_time' in rows:
                        row[rows] = datetime.strptime(row[rows].strip(),'%Y%m%d%H%M%S').strftime("%Y-%m-%d %H:%M:%S")
            #add this python dict to json array
           # jsonArray.append(row)
                if 'exam_id' in rows:
                    prefix = 'ACC'
                    id = row[rows]
                    row[rows] = prefix + id 
                if 'patient_type' in rows:
                    if row[rows] == 'E':
                        row[rows] = 'O'
                       # row.update({'e_flag': 'True'})
                        row['e_flag'] = 'True'
                if 'name' in rows:
                    first = row[rows].split()[0]
                    last = row[rows].split()[-1]
                    row[rows] = first + '^' + last
			



            jsonArray.append(row)


    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csvFilePath = r'data_in.csv'
jsonFilePath = r'Data_out.json'

get_em(csvFilePath, jsonFilePath)
