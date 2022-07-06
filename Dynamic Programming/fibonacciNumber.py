# Time Complexity - O(n)
def fib(self, n: int): 
    return self.fibDp(n, {})

def fibDp(self, n, fibDict):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in fibDict.keys():
        return fibDict[n]
    fibDict[n] = self.fibDp(n-1,fibDict) + self.fibDp(n-2, fibDict)
    return fibDict[n]