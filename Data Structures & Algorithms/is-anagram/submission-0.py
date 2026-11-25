from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s = "racecar", t = "carrace"

        s_counter:
        a: 2
        c: 2
        e: 1
        r: 2

        t_counter:
        a: 2
        c: 2
        e: 1
        r: 2
        
        check two counters (could use collections.Counter or just regular dictionary)
        """
        # s_counter, t_counter = Counter(s), Counter(t)
        return Counter(s) == Counter(t)
