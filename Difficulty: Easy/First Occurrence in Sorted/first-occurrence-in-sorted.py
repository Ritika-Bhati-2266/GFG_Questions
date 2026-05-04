class Solution:
    def firstSearch(self, arr, k):
        # Code Here
        if k in arr:
            return arr.index(k)
        return -1
        