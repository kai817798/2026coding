# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #for i in range(1,n+1):
            #if guess(i)==0:return i
        return bisect_left(range(n+1),0,key=lambda x:-guess(x))
        left,right = 1,n+1
        while left < right:
            mid = (left + right)//2
            if guess(mid)==0:return mid
            if guess(mid)>0: left = mid + 1
            else:right = mid
        return left
