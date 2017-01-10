import sys

winConditions = {{0,1,2},{0,4,8},{0,3,6},{1,4,7},{2,4,6},{2,5,8},{3,4,5},{6,7,8}}


function checkWinPossible(array,symbol):
    for i in winConditions.len():
        temp = winConditions[i]
        count = 0
        for i in temp.len():
            if temp[i] == symbol:
                count++
            if count == 2:
                if temp[0] == temp[1] == symbol:
                    return temp[2]
                elif temp[1] == temp[2] == symbol:
                    return temp[0]
                elif temp[0] == temp[2] == symbol:
                    return temp[1]
    return -1
        

function nextMove(array,symbol):
    if array.len() == 0:
        return -1;
    else:
        if checkWinPossible(array,symbol) != -1:
            