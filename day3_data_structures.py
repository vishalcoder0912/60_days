nums =[4,2,7,2,4,9,2]

total =0
maximun=nums[0]
minium=nums[0]

for num in nums:
    total +=num

    if num >maximun:
        maximum=num
    if num <minium:
        minium =num

print("sum:",total)
print("maxium:",maximun)
print("minium:",minium)

freq ={}
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

print("frequency:",freq)

reversed_list=[]
i =len(nums)-1
while i>=0:
    reversed_list.append(nums[i])
    i-=1

print("reversed list:",reversed_list)