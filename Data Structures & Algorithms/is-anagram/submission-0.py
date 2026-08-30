class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False #check first for matching length
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1 #count occurences of each character for first string
        
        for ch in t: # for each index in second string, check if index is in count, or if occurence of specific index is greater than count from first string
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True