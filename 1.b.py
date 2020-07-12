def insSort(list1):
   for index in range(1,len(list1)):

     currentvalue = list1[index]
     position = index

     while position>0 and list1[position-1]>currentvalue:
         list1[position]=list1[position-1]
         position = position-1

     list1[position]=currentvalue

list1 = [17,22,43,8,12,46,21,40]
insSort(list1)
print(list1)
