

def insert(color: str, arr: list[str], iteration: int) -> list[str]:
    for i in range(iteration):
        for j in range(len(arr)):
            if arr[i] == 




def treeDiagram(color: str):
    colorArr = ['R','R','R','B','B']
    red = 'R'
    blue = 'B'
    for i in range(len(colorArr)):
        if colorArr[i] == red and color == red or color == 'r':
            colorArr[i] = blue
        if colorArr[i] == blue and color == blue or color == 'b':
            colorArr[i] = red
        break
    
    arrayCount = len(colorArr)
    redCount = colorArr.count(red)
    blueCount = colorArr.count(blue)
    print(f"Edited Color Array: {colorArr}")
    print()
    print(f"Red: {redCount}\nBlue: {blueCount}")
    
    
treeDiagram('r')