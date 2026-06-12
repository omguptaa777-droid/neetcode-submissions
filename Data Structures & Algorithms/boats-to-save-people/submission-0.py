class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        n = len(people)
        i = 0
        j = n - 1
        boats = 0

        while i < j:
            total_wt = people[i] + people[j]

            if total_wt > limit:
                j -= 1
                boats += 1
            else:
                i += 1
                j -= 1
                boats += 1

        if i == j:
            boats += 1
        
        return boats