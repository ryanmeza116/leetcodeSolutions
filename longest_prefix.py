class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest_string = min(strs, key = len)
        # print(shortest_string)
        prefix = ""

        for i, char in enumerate(shortest_string):
            # print(i, char)
            for string in strs:
                # print(string[i], char)
                if string[i] != char:
                    return prefix
            print(prefix)
            prefix += char 
            print(prefix)
        
        return prefix