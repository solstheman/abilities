import random
from collections import Counter
import numpy as np
import scipy.stats as st
import itertools

def roll():
	val = random.randint(1,6)
	return val

def possibilities():
	possible_rolls = range(1,7)
	all_rolls = []
	for s in possible_rolls:
		for t in possible_rolls:
			for u in possible_rolls:
				for v in possible_rolls:
					all_rolls.append([s,t,u,v])
	return all_rolls

def all_values():
	poss = possibilities()
	values = []
	for roll in poss:
		value = sum(roll) - min(roll)
		values.append(value)

	return values

def roll_stats():
	probabilities = {};
	values = all_values()
	avg = np.mean(values)
	med = np.median(values)
	sd = np.sd(values)
	counts = Counter(values)
	for c in counts:
		probabilities[str (c)] = str (counts[c]) + '/'  + str (len(values))
	return {'avg': avg, 'median': med, 'probabilities': probabilities, 'counts': counts, 'sd': sd}

def get_abilities():
	abilities = [];
	for s in range(0,6):
		rolls = []
		for i in range(0,4):
			rolls.append(roll())
		value = sum(rolls) - min(rolls)
		abilities.append(value)
	return abilities

def ability_possibilities():
	possible_values = all_values()
	six_times_possible_values = possible_values*6
	all_ability_possibilities = itertools.combinations(six_times_possible_values, 6)
	return all_ability_possibilities

def ability_stats():
	ability_sums = []
	all_ability_possibilities = ability_possibilities()
	print(len(list(all_ability_possibilities)))
	return 'done'

stats = ability_stats()
print(stats)
