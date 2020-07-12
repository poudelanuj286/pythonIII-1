def bubbleS(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [7,22,43,8,12,46,21,40]
bubbleS(list)
print(list)
