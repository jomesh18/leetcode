'''
2551. Put Marbles in Bags
Hard

908

35

Add to List

Share
You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble distributions.

 

Example 1:

Input: weights = [1,3,5,1], k = 2
Output: 4
Explanation: 
The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
Thus, we return their difference 10 - 6 = 4.
Example 2:

Input: weights = [1, 3], k = 2
Output: 0
Explanation: The only distribution possible is [1],[3]. 
Since both the maximal and minimal score are the same, we return 0.
 

Constraints:

1 <= k <= weights.length <= 105
1 <= weights[i] <= 109
'''
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            return 0
        max_heap, min_heap = [], []
        for i in range(len(weights)-1):
            if len(min_heap) < k-1:
                heappush(min_heap, weights[i]+weights[i+1])
                heappush(max_heap, -(weights[i]+weights[i+1]))
            else:
                heappushpop(min_heap, weights[i]+weights[i+1])
                heappushpop(max_heap, -(weights[i]+weights[i+1]))
        
        return sum(min_heap)-sum(-i for i in max_heap)


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0
        pairs = [0]*(n-1)
        for i in range(n-1):
            pairs[i] = weights[i]+weights[i+1]
        pairs.sort()
        ans = 0
        for i in range(k-1):
            ans += pairs[-1-i] - pairs[i]
        
        return ans