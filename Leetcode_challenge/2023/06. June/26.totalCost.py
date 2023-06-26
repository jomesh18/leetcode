'''
2462. Total Cost to Hire K Workers
Medium

975

227

Add to List

Share
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

 

Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.
Example 2:

Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.
 

Constraints:

1 <= costs.length <= 105
1 <= costs[i] <= 105
1 <= k, candidates <= costs.length
'''
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        heap = [(costs[i], i, 0) for i in range(candidates)] + [(costs[i], n+i, 1) for i in range(-candidates, 0, 1)]
        heapify(heap)
        # print(heap)
        count = k
        used = [False]*n
        not_used = deque([i for i in range(candidates, n-candidates)])
        tot = 0
        while count:
            while heap and used[heap[0][1]]:
                curr_cost, curr_i, l = heappop(heap)
                if not_used:
                    if not l:
                        i = not_used.pop_left()
                        heappush(heap, (costs[i], i, 0))
                    else:
                        i = not_used.pop_right()
                        heappush(heap, (costs[i], i, 1))

            curr_cost, curr_i, l = heappop(heap)
            tot += curr_cost
            used[curr_i] = True
            if not_used:
                if not l:
                    i = not_used.popleft()
                    heappush(heap, (costs[i], i, 0))
                else:
                    i = not_used.pop()
                    heappush(heap, (costs[i], i, 1))
            count -= 1
            # print(tot, count, used, not_used, heap)
        return tot



class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Add the first k workers with section id of 0 and 
        # the last k workers with section id of 1 (without duplication) to pq.
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))

        heapify(pq)
        
        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates 

        # Only refill pq if there are workers outside.
        for _ in range(k): 
            cur_cost, cur_section_id = heappop(pq)
            answer += cur_cost
            if next_head <= next_tail: 
                if cur_section_id == 0:
                    heappush(pq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heappush(pq, (costs[next_tail], 1))
                    next_tail -= 1
                    
        return answer