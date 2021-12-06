def minimumWaitingTime(queries):
    # sort the queries array
    queries.sort()
    # initialise the results variable
    waiting_time = 0

    # iterate through the queries
    for idx, duration in enumerate(queries):
        # at each index, work out how many queries follow this one in the array
        queries_left = len(queries) - (idx + 1) # *see note
        # multiply the current duration by the number of queries left
        # and add that to the total waiting time
        waiting_time += queries_left * duration

    # return the result
    return waiting_time


"""
*Note

queries_left = len(queries) - (idx + 1) 

We need to account for the fact that we begin at index 0:

[1, 4, 6, 7, 10] <- Values
[0, 1, 2, 3, 4] <- Indexes

Index 0: len(queries) - (idx + 1) -> 5 - (0 + 1) = 4
Index 1: len(queries) - (idx + 1) -> 5 - (1 + 1) = 3
Index 2: len(queries) - (idx + 1) -> 5 - (2 + 1) = 2
Index 3: len(queries) - (idx + 1) -> 5 - (3 + 1) = 1
Index 4: len(queries) - (idx + 1) -> 5 - (4 + 1) = 0
"""