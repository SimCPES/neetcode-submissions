class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def occurences(word: str) -> tuple:
            res = [0] * 26
            for l in word:
                res[ord(l) - ord('a')] += 1
            return tuple(res)

        groups_map = collections.defaultdict(list)

        for word in strs:
            key = occurences(word)
            groups_map[key].append(word)

        return list(groups_map.values())