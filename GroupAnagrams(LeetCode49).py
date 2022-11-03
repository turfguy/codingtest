#LeetCode 49.Group Anagrams
#문자 배열을 받아, 애너그럼 단위로 그룹핑하라.
#입력:
# ["eat","tea","tan","ate","nat","bat"]
import collections

strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = collections.defaultdict(list)

for word in strs:
    anagrams[''.join(sorted(word))].append(word)

print(list(anagrams.values()))