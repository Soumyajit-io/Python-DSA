# LC 1052
# There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

# During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

# The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

# Return the maximum number of customers that can be satisfied throughout the day.

 

# Example 1:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

# Output: 16

# Explanation:

# The bookstore owner keeps themselves not grumpy for the last 3 minutes.

# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

# Example 2:

# Input: customers = [1], grumpy = [0], minutes = 1

# Output: 1









class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        i = 1
        j = minutes

        # base satisfaction (already satisfied customers)
        base = 0
        for k in range(len(customers)):
            if grumpy[k] == 0:
                base += customers[k]

        # initial window (only count grumpy ones)
        loss = 0
        for k in range(0, minutes):
            if grumpy[k] == 1:
                loss += customers[k]

        maxsum = loss

        # sliding window
        while j < len(customers):
            # add new element
            if grumpy[j] == 1:
                loss += customers[j]

            # remove old element
            if grumpy[i-1] == 1:
                loss -= customers[i-1]

            if loss > maxsum:
                maxsum = loss

            i += 1
            j += 1

        return base + maxsum