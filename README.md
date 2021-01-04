# Tech Exercises

## Table of contents
* [Setup](#setup)
* [Bash](#bash)
* [Data](#data)
* [Cron](#cron)
* [Relationaldb](#relationaldb)
* [LinuxTasks](#linuxtasks)

## Setup

Clone repository 

	$ git clone https://github.com/ChalkingCode/Tech-Exercise.git
	$ cd Tech-Exercise

## Bash 
- Write a bash script called print names that takes 2 arguments and an optional third
- Exit the bash script with an error when the first two arguments are not there
- The bash script should print each argument preceded by “Hello, “ followed by the argument.
- Example output uses
	- ./printnames bob dan (yields: Hello, bob\nHello, dan)
	- ./printnames (yields: You did not specify at least two names)
	- ./printnames bob dan jim (yields: Hello, bob\nHello, dan, Hello jim)

##### Solution 

The Bash script can be seen in repo as printnames.sh or cat printname.sh in terminal
	
	# this will give executable permission to  printnames.sh 
	$ chmod +x printnames.sh
	# the command below will yield You did not specify at least two names  
	$ ./printnames bob
	# the command below will yield Hello, bob\nHello, dan\n
	$ ./printnames bob dan
	# the command below will yield Hello, bob\nHello, dan\nHello jim\n
	$ ./ bob dan jim
	

## Data

- Write a python script called csv2json.py that takes in data_in.csv and generate a data_out.json.


- Data_out.json:
	- {"csv_output": [{"name": "John Doe","exam_id": "abc12345","arrived_timestamp": "2020-08-28 10:35:22"}, {"name": "Jane Doe","exam_id": "abc7854","arrived_timestamp": "2020-08-27 05:26:32"}]}

##### Follow on

- Write a python script called csv2json.py that takes in data_in.csv and generates a separate json for each exam, with the filename being {exam_id}.json.
	
	- Prefix ACC to each exam_id
	- Format timestamp to iso8601
	- Handle patient_type “E”
		- Change  ”E” to “O”
		- Add a key to the payload e_flag set to true
	- Bonus
		- Change given name First Last to Last^First in payloaod

Example:
- abc1234.json:
	- {
	  "name": "DOE^JOHN",
	  "exam_id": "ACCabc12345", 
	  "patient_type":"I",
	  "arrived_timestamp": "2020-08-28 10:35:22"
	  }
 

##### Follow on Solution 

	$ python csv2json.py
	
	
	# code added for solution you can also see csv2json.py 
	# Prefix ACC to each exam_id 	
	if 'exam_id' in rows:
                    prefix = 'ACC'
                    id = row[rows]
                    row[rows] = prefix + id     
	# Handle patient_type E
	if 'patient_type' in rows:
		if row[rows] == 'E':
                        row[rows] = 'O'
                       # Add a key to the payload e_flag set to true 
                        row['e_flag'] = 'True'
                # Bonus Change given name to Last^First in payload
		if 'name' in rows:
                    first = row[rows].split()[0]
                    last = row[rows].split()[-1]
                    row[rows] = first + '^' + last


##### Original Solution

If still running a version of python older than 3.6 you should update or create virtual env. This is due to how json dumps dictionaries are unordered.
	
	# Set up Virtual env if python version older than 3.6 
	$ python3 -m venv nameofenv
	$ source nameofenv/bin/activate
	$ python --version 
	# Run command 
	$ python csv2json.py
	# to see results run below or just open the json file  
	$ cat Data_out.json 
	$ [{"name": "John Doe", "exam_id": "abc12345", "arrived_time": "2020-08-28 10:35:22"}, {"name": "Jane Doe", "exam_id": "abc7854", "arrived_time": "2020-08-27 05:26:32"}]	

Also see csv2json.py in Repo 

## Cron 
- Create a cronjob for the script created in the previous exercise that will run  Tuesdays at 3am and 11pm

##### Solution
	
	# List jobs per user 
	$ crontab -l
	# edit/create cronjobs 
	$ crontab -e
	# you want to use pwd to find the file path of your csv2json.py  
	$ 0 3,23 * * TUE home/user/csv2json.py 

## Relationaldb 

- We want to find our top ordering customers. Write a query to get order counts for each customer (descending by count).

- https://www.w3schools.com/sql/trysql.asp?filename=trysql_op_in

### Solution
##### SQL Statement
	SELECT CustomerId,
 	 COUNT(OrderId)
	FROM Orders
	GROUP BY CustomerId
	ORDER BY COUNT(OrderId) DESC ;

## Linuxtasks

- Given a 50GB volume, partition into 20GB and 30GB parts.
	- Mount 20GB as /servers
		
##### Solution
		
	$ say you have 100GB at /home/ and you want to allocate out 20GB 
	# 20 GB t
	$ df -h
	$ umount /home/ 
	# you will find the path with command df -h 
	$ e2fsck -f filesystem path to /home/ 
	$ resize2fs filesystem/path/to/home 20GB
	$ lvreduce -L 20G filesystem/path/to/home 
	$ mount /home/
	$ df -h /home/ 
	$ lvs 
	$ lvextend -L +20G filesystem/path/to/servers
	$ resize2fs filesystem/path/to/servers/ 20G 
	$ df -h /servers 
	
	- Mount 30GB as /data

##### Solution		
	
	# same as above but for 30G and filesystem/path/to/data

- Add /servers persistently to PATH variable
- Change timezone to localtime

##### Solution

	# how to check current time zone
	$ timedatectl
	# view all available timezones 
	$ timedatectl list-timezones
	# once you find your local time zone run 
	$ sudo timedatectl set-timezone <yourtimezone>
	# example below 
	$ sudo timedatectl set-timezone America/New_York
	# verify change 
	$ timedatectl

- Create a user test1 and group testers

##### Solution 
	
	# Create a user 
	$ sudo useradd -m test1 -p randompassword
	# create group testers
	$ sudo groupadd testers
	
	- Create a folder /servers/tests where you are the owner but testers group can write to the directory
		
##### Solution
		
	$ mkdir /servers/tests
	$ ls -l 
	$ chown username foldername
	$ chmod g+w foldername

## Questions

###### Questions? If you have a question or would like to add feedback please contact me at skylarbarrowman@gmail.com. :)
