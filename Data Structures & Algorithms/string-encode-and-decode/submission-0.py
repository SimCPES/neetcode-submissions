class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += (word + "Simeon")
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strings = []
        current_string = s[:]
        while "Simeon" in current_string:
            next_index = current_string.index("Simeon")
            strings.append(current_string[:next_index])
            current_string = current_string[next_index+6:]
        return strings
