#Bash

#Write a bash script called print names that takes 2 arguments and an
#optional third

#Exit the bash script with an error when the first two arguments are
#not there

#The bash script should print each argument preceded by “Hello, “
#followed by the argument.

#Example output uses

#./printnames bob dan (yields: Hello, bob\nHello, dan)

#./printnames (yields: You did not specify at least two names)

#./printnames bob dan jim (yields: Hello, bob\nHello, dan, Hello jim)

#if file is not set to execute run chmod +x printnames.sh

if [ $# = 2 ];
then
   printf "Hello, $1\nHello, $2\n"
elif [ $# -lt 2 ];
then
   printf "You did not specify at least two names\n"
elif [ $# > 2 ];
then
   printf "Hello, $1\nHello, $2\nHello, $3\n"
fi

