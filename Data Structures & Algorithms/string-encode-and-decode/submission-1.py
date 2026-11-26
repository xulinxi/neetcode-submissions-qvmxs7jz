class Solution:
    """
    Input: strs = ["Hello","World"]

    Output: ["Hello","World"]
    """

    def encode(self, strs: List[str]) -> str:
        """
        Input: strs = ["Hello","World3"]
        5#Hello6#World3

        Output: ["Hello","World"]

        """
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + "#" + s
        # print(res)
        return res



    def decode(self, s: str) -> List[str]:
        """
        Input: 
        res = 
        51#Hello6#World3
        i
           j
           [j+1:j+1+num] - word

        if integer: get range until # -> num
        word: [j+1 : j + 1 + num] - apppend to res
        i = j + 1 + num

        Output: ["Hello","World"]

        python notes:
        - check number: char.isnumeric(), char.isdigit(), https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth
        
        - check char:
        - check alphanum:

        """
        res = []
        i = j = 0
        while i < len(s):
            while s[j].isdigit():
                j += 1
            print(s[i:j])
            l = int(s[i:j])
            word = s[j+1: j+1+l]
            print(word)
            res.append(word)
            i = j = j + 1 + l
        return res




















