
def calculateProfit(n, earnings, cost, e): 
	profit = 0; 
	for i in range(n): 
		earning_per_day = 0; 
		daily_spent_food = 0; 

		if (i == (n - 1)): 
			earning_per_day = earnings[i] * e; 
			profit = profit + earning_per_day; 
			break; 

		# Else buy food to gain 
		# energy for next day 
		if (cost[i] < earnings[i]): 
			
			# Update earning per day 
			earning_per_day = earnings[i] * e; 
			daily_spent_food = cost[i] * e; 

			# Update profit with daily spent 
			profit = (profit + earning_per_day -
							daily_spent_food); 

	print(profit); 

# Driver Code 
if __name__ == '__main__': 
	
	# Given days 
	n = 4; 

	# Given earnings 
	earnings = [ 1, 8, 6, 7 ]; 

	# Given cost 
	cost = [ 1, 3, 4, 1 ]; 

	# Given energy e 
	e = 5; 

	# Function call 
	calculateProfit(n, earnings, cost, e); 
