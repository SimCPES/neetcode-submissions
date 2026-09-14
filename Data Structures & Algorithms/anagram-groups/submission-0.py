class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def occurences(word: str) -> Dict:
            res = {}
            for l in set(word):
                res[l] = word.count(l)
            return res

        decomp_words = [occurences(word) for word in strs]
        groups = []
        groups_dicts = []

        for i, word in enumerate(strs):
            if decomp_words[i] in groups_dicts:
                corresponding_group = groups_dicts.index(decomp_words[i])
                groups[corresponding_group].append(word)
            else:
                groups.append([word])
                groups_dicts.append(decomp_words[i])

        return groups
