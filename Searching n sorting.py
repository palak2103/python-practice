array=[8,45,34,89,90,34,12,67]
array.sort()
print(array)
#target=12
#for i in range(len(array)):
#  if array[i]==target:
#    print(i)
#two pointers
target=90
start=0
end=len(array)-1
while start<=end:
  mid=(end+start)//2
  if target==array[mid]:
    print (mid)
    break
  elif target>array[mid]:
    start=mid+1
  else:
    end=mid-1    
    


