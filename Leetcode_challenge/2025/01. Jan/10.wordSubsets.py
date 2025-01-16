'''
916. Word Subsets
Solved
Medium
Topics
Companies
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

Output: ["facebook","google","leetcode"]

Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

Output: ["leetcode"]

Example 3:

Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

Output: ["cccbb"]

 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        f = [0]*26
        for w in words2:
            curr_f = [0]*26
            for c in w:
                curr_f[ord(c)-ord('a')] += 1
            for i in range(26):
                f[i] = max(f[i], curr_f[i])
        
        result = []
        for w in words1:
            curr_f = [0]*26
            for c in w:
                curr_f[ord(c)-ord('a')] += 1
            is_universal = True
            for i in range(26):
                if f[i] > curr_f[i]:
                    is_universal = False
                    break
            if is_universal:
                result.append(w)
        
        return result