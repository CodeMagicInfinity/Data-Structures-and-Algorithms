# https://www.geeksforgeeks.org/find-the-first-repeated-character-in-a-string/

def firstRecurringCharacter(s):
    # Time Complexity - O(n) and Space Complexity - O(n)
    hash_map = {}
    for c in s:
        if c in hash_map.keys():
            return c
        else:
            hash_map[c] = True 
    return -1
    
    # Time Complexity - O(n*n)
    # min_index = float('inf')
    # output_char = s[0]
    # for i in range(0, len(s)-1):
    #     for j in range(i+1, len(s)):
    #         if s[i] == s[j]:
    #             if j < min_index:
    #                 min_index = j
    #                 output_char = s[i]
    # if min_index == float('inf'):
    #     return -1
    # else:
    #     return output_char