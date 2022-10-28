'''
49. Group Anagrams
Medium

12504

378

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            arr = ['0']*26
            for c in s:
                pos = (ord(c)-ord('a'))
                arr[pos] = str(int(arr[pos]) + 1)
            d[','.join(arr)].append(s)
        return list(d.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[(ord(c)-ord('a'))] += 1
            d[tuple(arr)].append(s)
        return list(d.values())