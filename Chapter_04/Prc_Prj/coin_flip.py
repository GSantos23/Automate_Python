'''
Coin Flip Streaks

For this exercise, we'll try doing an experiment. If you flip a coin 100 times
and write down an "H" for the heads and "T" for each tails, you'll create a list
that looks like "T T T T H H H H T T". If you ask a human to make up 100 random
coin flips, you'll probably end up with an alterning head-tail result like
"H T H T H H T H T T", which looks random (to humans), but isn't mathematically
random. A human will almost never write down a streak of six heads or six tails
in a row, even though it is highly likely to happen in truly random coin flips.
Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six
tails comes up in a randomly generated list of heads or tails. Your program 
breaks up the experiment into two parts: the first part generates a list of 
randomly selected 'heads' and 'tails' values, and the second part checks if 
there is a streak in it. Put all of this code in a loop that repeats the
experiment 10,000 times so we can find out what percentage of the coin flips
contains a streak of six heads or tails in a row. As a hint, the function call
random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the
other 50% of the time. You can start with the following template.

Of course, this is only an estimate, but 10,000 is a decent sample size.
Some knowledge of mathematics could give you the exact answer and save
you the trouble of writing a program, but programmers are notoriously bad
at math.

'''  

import random

numberOfStreaks = 0
headStreak = 0
tailStreak = 0
coinList = []

for experimentNumber in range(10000):
	# code that creates a list of 100 heads or tails values
	if experimentNumber < 101:
		coinValue = random.randint(0, 1)

		if coinValue == 0:
			coinList.append('H')
			headStreak = headStreak + 1
			# code that checks if there is a streak of 6 heads or tails in a row
			if headStreak >= 6:
				numberOfStreaks = numberOfStreaks + 1
		elif coinValue == 1:
			coinList.append('T')
			tailStreak = tailStreak + 1
			# code that checks if there is a streak of 6 heads or tails in a row
			if tailStreak >= 6:
				numberOfStreaks = numberOfStreaks + 1
			

print(coinList)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))