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

The solution can be found in printnames.sh 

## Data 

## Cron 
- Create a cronjob for the script created in the previous exercise that will run  Tuesdays at 3am and 11pm

##### Solution
	
	# List jobs per user 
	$ cron -l
	# edit/create cronjobs 
	$ cron -e 
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
