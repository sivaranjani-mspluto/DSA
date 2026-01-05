class Solution:
    def isValid(self, s: str) -> bool:
        brac={")":"(","}":"{","]":"["}
        stack=[]

        for i in s:
            if i in brac :
                if not stack or stack[-1] != brac[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return len(stack)==0
             

            