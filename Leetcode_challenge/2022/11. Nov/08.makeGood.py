'''
1544. Make The String Great
Easy

1995

84

Add to List

Share
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"
 

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.
'''
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and ((c.isupper() and stack[-1].islower() and stack[-1].upper() == c) or (c.islower() and stack[-1].isupper() and stack[-1] == c.upper())):
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        i = 0
        for j in range(len(s)):
            if i > 0 and abs(ord(s[i-1])-ord(s[j])) == 32:
                i -= 1
            else:
                s[i] = s[j]
                i += 1
        return ''.join(s[:i])
