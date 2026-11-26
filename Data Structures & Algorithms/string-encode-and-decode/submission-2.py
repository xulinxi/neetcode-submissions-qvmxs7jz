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

        python syntax notes:
        "".join(list)
        """
        # res = "" 
        res = []

        # for s in strs:
        #     l = len(s)
        #     res += str(l) + "#" + s
        for word in strs: #count#word
            res.append(f"{len(word)}#{word}")

        # print(res)
        # return res
        return "".join(res)



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
        isdecimal()	十进制数字	      5、3
        isdigit()	十进制数字及其他   digit 字符	5、²
        isnumeric()	最广泛的数字字符   5、²、½、四

        - check char:
        - check alphanum:

        - find("#") 找第一个#
        - j = s.find("#", i) #从index i开始找

        """
        res = []
        i = j = 0
        while i < len(s):
            # while s[j].isdigit():
            #     j += 1
            j = s.find("#", i) 
            # print(s[i:j])
            l = int(s[i:j])

            start = j+1
            end = start + l

            # word = s[j+1: j+1+l]
            # print(word)
            # res.append(word)
            res.append(s[start:end])
            # i = j = j + 1 + l
            i = end
        return res




















