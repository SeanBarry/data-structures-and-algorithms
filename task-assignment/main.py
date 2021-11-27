def taskAssignment(k, tasks):
    # set up the results array
    pairedTasks = []
    # create the datastructure that stores the original index of each number 
	taskDurationsToIndices = getTaskDurationsToIndices(tasks)
    # sort the list of tasks
	sortedTasks = sorted(tasks)

    # create a pair for each number in k
	for idx in range(k):
        # the first task is just at the index we are iterating through e.g 0, 1, 2
		task1Duration = sortedTasks[idx]
        # grab the array of indices in which this number was placed in the task list
		indicesWithTaskDuration = taskDurationsToIndices[task1Duration]
        # pop one of the indices from the array
		task1Index = indicesWithTaskDuration.pop()
		
        # as k increments, this will pick numbers k + 1 from the end of the array
		task2SortedIndex = len(tasks) - 1 - idx
        # grab the number that sits at this index 
		task2Duration = sortedTasks[task2SortedIndex]
        # grab the array of indices this number was sitting at 
		indicesWithTask2Duration = taskDurationsToIndices[task2Duration]
        # pop one of the indices from the array
		task2Index = indicesWithTask2Duration.pop()
		
        # append task1 and task2 indices to the results array
		pairedTasks.append([task1Index, task2Index])
		
    # return the results array
	return pairedTasks
	

# this util maps each task duration to the index it sat at originally
def getTaskDurationsToIndices(tasks):
    # create a cache
	taskDurationsToIndices = {}
	
    #iterate through the tasks
	for idx, taskDuration in enumerate(tasks):
        # if the task is in the cache, then append the index to its array
		if taskDuration in taskDurationsToIndices:
			taskDurationsToIndices[taskDuration].append(idx)
		else:
            # otherwise create an array in the cache with the task duration's index
			taskDurationsToIndices[taskDuration] = [idx]

	# return the cache
	return taskDurationsToIndices

