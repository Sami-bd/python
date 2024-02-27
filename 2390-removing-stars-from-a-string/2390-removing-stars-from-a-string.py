class Solution:
    def removeStars(self, s: str) -> str:
        s_list = []
        for i in s:
            s_list.pop() if i == '*' else s_list.append(i)
        return ''.join(s_list)