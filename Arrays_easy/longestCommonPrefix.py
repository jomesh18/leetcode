class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) == 0: return ""
        min_len = len(strs[0])
        for i in strs:
            if min_len>len(i):
                min_len = len(i)
        res = []
        temp = ""
        common = True
        j = 0
        while j < min_len:
            for i in range(len(strs)):
                if i == 0:
                    temp = strs[i][j]
                else:
                    if strs[i][j] != temp:
                        common = False
                        break
            if common:
                res.append(temp)
                j += 1
            else:
                return "".join(res)
        return "".join(res)

a = Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs) =='fl')
#Edge cases
strs = [""]
print(a.longestCommonPrefix(strs)=="")
strs = []
print(a.longestCommonPrefix(strs)=="")
strs = ["", ""]
print(a.longestCommonPrefix(strs)=="")
strs = ["a"]
print(a.longestCommonPrefix(strs)=="a")
strs = ["a", "", "c"]
print(a.longestCommonPrefix(strs)=="")
strs = ["c","c"]
print(a.longestCommonPrefix(strs)=="c")
