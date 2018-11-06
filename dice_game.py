"""
Dice Game:
guess the right number
"""

from random import randint
from time import sleep

def get_user_guess():
  guess=int(raw_input("Enter your guess: "));
  return guess;

def roll_dice(number_of_sides):
  first_roll=randint(1,number_of_sides);
  second_roll=randint(1,number_of_sides);
  max_val=number_of_sides*2;
  print "the max value is %d" % max_val;
  guess=get_user_guess();
  if guess>max_val:
    print "you entered an invalid number";
  else:
    print "rolling...";
    sleep(2);
    print "The first dice produced %d" % first_roll;
    sleep(1);
    print "The second dice produced %d" % second_roll;
    total=first_roll+second_roll;
    print "total is %d" % total;
    print "result...";
    sleep(1);
    if guess==total:
      print "genius, you guessed the right number";
    else:
      print "bad luck,you failed";
            
roll_dice(6);
    
