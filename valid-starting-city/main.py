def validStartingCity(distances, fuel, mpg):
	# initialise the valid_city index to the first city
	valid_city = 0
	# track how much fuel is in the tank. That's 0 initially
	current_distance_in_tank = 0
	# initialise a pointer to iterate through the array
	pointer = 0

	while pointer < len(distances):
		# top up the fuel count with what's available at the current city
		current_distance_in_tank += mpg * fuel[pointer]

		# travel to the next city and consume the amount of fuel it requires
		current_distance_in_tank = current_distance_in_tank - distances[pointer]

		# if the fuel is not negative, the valid_city is still potentially valid, so keep going
		if current_distance_in_tank >= 0:
			pointer += 1
		else:
			# there was a negative fuel balance, so it's impossible for the previous valid city to be
			# the answer. In this case, increment the pointer to the next city, and make it a new potential
			# valid starting city. Also, reset the fuel_in_tank to 0 as we are restarting the search
			pointer += 1
			valid_city = pointer
			current_distance_in_tank = 0

	return valid_city
