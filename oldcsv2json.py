import csv
import json
from datetime import datetime


def change_format():
                with open('data_change.csv', 'r') as source:
                        with open('data_in.csv', 'w') as result:
                                writer = csv.writer(result)
                                reader = csv.reader(source)
                                source.readline()
                                for row in reader:

                                        ts = row[2]
                                        ts = datetime.strptime(ts, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
                                        if ts != "":
                                                row[2] = ts
                                                writer.writerow(row)
                source.close()
                result.close()

def get_data():
        csvfile = open('data_in.csv', 'r')
        jsonfile = open('Data_out.json', 'w')

        fieldnames = ("name","exam_id","arrived_time")
        reader = csv.DictReader( csvfile, fieldnames)
        for row in reader:
                json.dump(row, jsonfile)
                jsonfile.write('\n')

change_format()
get_data()

