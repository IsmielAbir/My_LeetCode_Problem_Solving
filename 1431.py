class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        li = []
        maxi = 0

        for i in candies:
            if i > maxi:
                maxi = i

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= maxi:
                li.append(True)
            else:
                li.append(False)
        return li