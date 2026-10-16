class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for score in operations:
            if score == "+":
                add = (scores[-1] + scores[-2])
                scores.append(add)
                
            
            elif score == "C":
                scores.pop(-1)
            
            elif score == "D":
                double = scores[-1] * 2
                scores.append(double)

            
            else:
                scores.append(int(score))
            print(score)
            print(scores)
        total = 0
        for score in scores:
            total += score
        return total


        