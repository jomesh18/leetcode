'''
Add and Search Word - Data structure design

Solution
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
   Show Hint #1  
You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
'''
class TrieNode:
    def __init__(self):
        self.chilren = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            
            curr = curr.chilren.setdefault(c, TrieNode())
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            curr = curr.chilren.get(c)
            if not curr: return False
        return curr.isEnd == True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

null = None
true = True
false = False

inp1 = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
inp2 = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output = [null,null,null,null,false,true,true,true]

obj = WordDictionary()
res = [None]

for fn, para in zip(inp1, inp2):
    if fn == "addWord":
        res.append(obj.addWord(para))
    elif fn == "search":
        res.append(obj.search(para))
    else:
        continue

print(res)
print(Output)
print(res == Output)
