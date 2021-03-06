import random
import math
import matplotlib.pyplot as plt

number_of_players_string = input('how many players are you?')
number_of_players = int(number_of_players_string)
number_of_rounds = input('how many rounds do you want to play? ') #Sequence of number of items per round
print(number_of_rounds)
rounds = [int(x) for x in number_of_rounds.split()]
T = sum(rounds) #Number of round
vi = []
v1 = [0] + sorted([random.randint(0,2*T) for i in range(T)], reverse = True)
 #marginal valuation for bidder 1

v2 = [0] + [2*T] + sorted([random.randint(0,T-1) for i in range(T-1)], reverse = True)
 #marginal valuation for bidder 2

print(vi)
for j in range(number_of_players):
	answer_question1 = input('player' + str(j) + ' do you want to set your marginal values? (Y/N)')
	if answer_question1 == "Y" :
		v1[0] = 0 
		for i in range(1,T+1):
			input_1 = input("value:")
			v1[i] = int(input_1)
		vi.append(v1)
	else:
		v1 = [0] + sorted([random.randint(0,2*T) for i in range(T)], reverse = True)
		vi.append(v1)
#print(vi)

#Check that v1/v2 are non-increasing ?
vfi = [[] for i in range(number_of_players)] #valuation function for bidder i


for j in range(number_of_players):
	vfi[j] = [0]*(T+1)

for i in range(T+1):
	for j in range(number_of_players):
		vfi[j][i] = vfi[j][i-1] + vi[j][i]
print(vi)
print(vfi)

#Resolutionn
utility_i = [0]*(number_of_players)
nb_i = [0]*(number_of_players)
bid_i = [0]*(number_of_players)
for i in range(number_of_players):
	utility_i[i] = 0

price = [0]*T #Price of different items
for i in range(number_of_players):
	nb_i[i] = 0 #Number of items got by player i

winner = 0 #winner for round i
monopoly = 0
win = []
i = 1

for rnd in rounds:
	all_bids = []
	for j in range(number_of_players):
			bid_i[j] = input('player' + str(j) + 'input your bid (' + str(rnd) + ' values):')
			bid_i[j] = [int(x) for x in bid_i[j].split()]
			all_bids += [(x,j) for x in bid_i[j]]
	
	all_bids.sort(reverse = True)
	price[i-1]= all_bids[rnd][0]
	
	print("Round",i)
	print("Bids:",bid_i,'->',price[i-1])
	for k in range(rnd):
		winner = all_bids[k][0]
		max_index = all_bids[k][1]
		win.append(winner)
		print("Winner is",winner)
		nb_i[max_index] += 1
		print("price is = " + str(price[i-1]))
		print("value is = " + str(vi[max_index][nb_i[max_index]]))
		utility_i[max_index] += vi[max_index][nb_i[max_index]] - price[i-1]
		print("\nP1:",nb_i,"items, util",utility_i)
		print("\n##############\n")
		
	i += 1
	
print(price)
print(win)
plt.plot(price)
plt.show()
