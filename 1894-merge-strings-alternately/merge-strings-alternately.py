class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        l1=len(word1)
        l2=len(word2)
        i,j=0,0
        while i<l1 and j<l2:
            s+=word1[i]
            s+=word2[j]
            i+=1
            j+=1
        if i>l1-1 and j<=l2-1 :
            s+=word2[j:]
        elif j>l2-1 and i<=l1-1 :
            s+=word1[i:]

        return s
