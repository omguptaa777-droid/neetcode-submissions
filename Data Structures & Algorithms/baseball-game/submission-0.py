class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for x in operations:
            if x == "+":
                score.append(score[-1]+score[-2])
            elif x == "D":
                score.append(2*score[-1])
            elif x == "C":
                score = score[:-1]
            else:
                score.append(int(x))
        
        return sum(score)