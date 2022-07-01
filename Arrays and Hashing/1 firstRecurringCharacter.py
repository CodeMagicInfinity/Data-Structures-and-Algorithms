# https://www.geeksforgeeks.org/find-the-first-repeated-character-in-a-string/
# Time Complexity - O(n), Space Complexity - O(n) 
# Note - Time for Lookup in Hash Map - O(1)

def firstRecurringCharacter(input):
    recurring_dict = {}
    for c in input:
        if c in recurring_dict.keys():
            return c
        else:
            recurring_dict[c] = True
    return -1