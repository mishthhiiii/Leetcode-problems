class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        # Step 1: Count how many stones fall into Type 0, Type 1, and Type 2
        type0 = 0
        type1 = 0
        type2 = 0
        
        for s in stones:
            remainder = s % 3
            if remainder == 0:
                type0 += 1
            elif remainder == 1:
                type1 += 1
            else:
                type2 += 1
        
        # Step 2: Check Case 1 (Even number of "Pass" stones)
        if type0 % 2 == 0:
            # Alice wins if she has at least one of both Type 1 and Type 2
            return type1 > 0 and type2 > 0
            
        # Step 3: Check Case 2 (Odd number of "Pass" stones)
        else:
            # Alice wins if one group outnumbers the other by more than 2
            return abs(type1 - type2) > 2
