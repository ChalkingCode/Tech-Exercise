# Tech Exercises

## Table of contents
* [Setup](#setup)
* [Bash](#bash)
* [Data](#data)
* [Cron](#cron)
* [Relationaldb](#relationaldb)

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

The Bash script can be seen in repo printnames.sh or cat printname.sh in terminal
	
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

##### Solution 
	# Run command 
	$ python csv2json.py
	# to see results run below or just open the json file  
	$ cat Data_out.json 
	
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

## Questions

###### Questions? If you have a question or would like to add feedback please contact me at skylarbarrowman@gmail.com. :)
