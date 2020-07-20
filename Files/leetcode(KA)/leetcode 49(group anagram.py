#Given an array of strings, group anagrams together.

"""Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]"""


strs=["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagrams(strs):
    ht={}
    for string in strs:
        ss = ''.join(sorted(string))
        if ss in ht:
            ht[ss].append(string)
        else:
            ht[ss]=[string]

    return ht.values()

print(group_anagrams(strs))