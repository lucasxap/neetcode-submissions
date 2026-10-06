#check top left corners of each box so theres 9 lists and scan list 1, 2 ,3 from  [0-2] then [3-5] then [6-8] 
# just make 3 things
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temparray = [] 

        #thing 1
        for row in board:
            temparray.clear()
            for digits in row:
                if digits in temparray and digits != ".":
                 
                    return False
                temparray.append(digits)
        for i in range(9):
            temparray.clear()
            for j in range(9):
                if board[j][i] in temparray and board[j][i] != ".":
                    return False
                temparray.append(board[j][i])
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temparray.clear()
                for k in range(3):
                    for l in range(3):
                        val = board[l+i][k+j]
                        if val in temparray and val != ".":
                            return False
                        temparray.append(val)


        return True
                

        