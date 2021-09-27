# O(n^2) time | O(n) space
def arrayOfProducts(array):
	results = [None] * len(array)

	for i in range(len(array)):
		runningProduct = 1

		for j in range(len(array)):
			if i != j:
				runningProduct *= array[j]
				
		results[i] = runningProduct
	
	return results
				
# O(n) time | O(n) space
def arrayOfProducts(array):
    # initialise 3 arrays, one for the final products, the others
    # for the products to the left and right of each index of the array
	products = [1 for _ in range(len(array))]
	leftProducts = [1 for _ in range(len(array))]
	rightProducts = [1 for _ in range(len(array))]
	
    # initialise a running product at 1 for the left array
	leftRunningProduct = 1
	for i in range(len(array)):
		leftProducts[i] = leftRunningProduct
		leftRunningProduct *= array[i]
		
    # initialise a running product at 1 for the right array
	rightRunningProduct = 1
	for i in reversed(range(len(array))):
		rightProducts[i] = rightRunningProduct
		rightRunningProduct *= array[i]
		
    # for each index in the array, multiply the left and right products
	for i in range(len(array)):
		products[i] = leftProducts[i] * rightProducts[i]
		
	return products
    
# O(n) time | O(n) space
# This is the same as the above solution but uses one less loop to achieve the final result
def arrayOfProducts(array):
	products = [1 for _ in range(len(array))]
	
	leftRunningProduct = 1
	for i in range(len(array)):
		products[i] = leftRunningProduct
		leftRunningProduct *= array[i]
		
	rightRunningProduct = 1
	for i in reversed(range(len(array))):
		products[i] *= rightRunningProduct
		rightRunningProduct *= array[i]
		
	return products
    
