class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count=collections.Counter(deck)
        l = len(deck)
        for i in range(2,l+1):
            if l%i==0:
                if all(v%i==0 for v in count.values()):
                    return True
        return False