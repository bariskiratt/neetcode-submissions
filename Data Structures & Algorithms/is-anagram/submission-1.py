class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for letter in s:
            smap[letter] = smap.get(letter,0) + 1
        for letter in t:
            tmap[letter] = tmap.get(letter,0) + 1
        check = True
        if len(tmap) != len(smap):
            return False
        for letter in tmap:
            if tmap.get(letter) != smap.get(letter):
                check = False
        return check




        