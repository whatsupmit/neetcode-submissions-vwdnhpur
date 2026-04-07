class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        returnList = []
        length = len(arr)
        for i in range(0, length):
            if i == (length - 1):
                returnList.append(-1)
            else:
                returnList.append(max(arr[i+1:]))
        return returnList
