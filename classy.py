class Solution:
    # add your logic here
    def __init__(self):
        self.lkDict = dict()
        self.length = 0
        self.maxLen = 0
        self.result = []

    def _getLengthOfLIS(self, A):
        n = len(A)
        for i in range(0, n):
            li = []
            for j in range(i+1, n):
                if A[j] > A[i]:
                    li.append(j)
            self.lkDict[i] = li

    def reGetLengthOfLIS(self, A, index: int):
        self.result.append(A[index])
        # self.length += 1
        _max = 0
        if self.lkDict[index]:
            for i in self.lkDict[index]:
                _max = max(_max, 1 + self.reGetLengthOfLIS(A, i))
            return _max
        else:
            # if self.length > self.maxLen:
            if _max > 
                self.maxLen = self.length
                print(self.result)
        # self.length -= 1
        self.result.pop()

    def getLengthOfLIS(self, A) -> int:
        self.__init__()
        self._getLengthOfLIS(A)
        for i in range(len(A)):
            self.length = 0
            self.result = []
            self.reGetLengthOfLIS(A, i)
        return self.maxLen

    def printDict(self, arr):
        for key, values in self.lkDict.items():
            print(arr[key], end="")
            print(": ", end="")
            li = []
            for i in values:
                li.append(arr[i])
            print(li)


a = [10, 20, 2, 5, 3, 8, 8, 25, 6]
b = [10, -63, 7, -50, 32, -9, -3]
c = [71, 0, 4, 42, -31, 4, -42]
d = [77, 0, -2, 25, 1, 70]
e = [2, 2, 1, 5, 7, -50, 80]


obj = Solution()

print(obj.getLengthOfLIS(a))
print(obj.getLengthOfLIS(b))
print(obj.getLengthOfLIS(c))
#obj.printDict(c)
print(obj.getLengthOfLIS(d))
print(obj.getLengthOfLIS(e))
