class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        HashMap + sort each word as key and group them
        TC: sort: O(nklok) - k is max length of a word; n is count of strs
        SC: nk
        or
        HashMap + convert each word to list of count in array
        ex: act; [1,0,1,0,0,0,0,0,0,0,...]
        TC: no sort: nk
        SC: n

        anagramsMap = {
        (0, 0, ...): [],
        
        
        }
        return list(anagramsMap.values())

        """
        anagramsMap = collections.defaultdict(list)

        for s in strs:
            anagramsList = [0 for i in range(26)]

            for c in s:
                index = ord(c) - ord('a')
                anagramsList[index] += 1
            key = tuple(anagramsList)
            anagramsMap[key].append((s))


        return list(anagramsMap.values())

        """
        notes on ord vs chr:
        ord(c) vs chr(i)
        ord(c): chr -> int
        chr(i): int -> chr
        """






















