'''
1423. Maximum Points You Can Obtain from Cards
Medium

3315

128

Add to List

Share
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 

Constraints:

1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length
Accepted
147,665
Submissions
290,885
'''
#O(n) time for pre_sum, O(k) for main, O(n) space
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        pre_sum = [0] + list(accumulate(cardPoints))
        min_sum = float("inf")
        # print(pre_sum)
        for i in range(k+1):
            min_sum = min(min_sum, pre_sum[i+n-k] - pre_sum[i])
            # print(i, i+n-k, min_sum)
        return pre_sum[-1] - min_sum
    
#O(k), O(2k) for main, O(1)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        win, res = 0, 0
        for i in range(-k, k):
            win += cardPoints[i]
            if i >= 0:
                win -= cardPoints[i-k]
            res = max(res, win)
        return res

#O(k), O(1)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints[:k])
        res = s
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k-i]
            res = max(s, res)
        return res