# arr=[5,10,15,20,25,30,35]
# pos=3
# for i in range(len(arr)-1,pos-1,-1):
#     arr[i]=arr[i-pos]
# for i in range(pos):
#     arr[i]=0
# print(arr)
# o/p=[0, 0, 0, 5, 10, 15, 20]


# ---------------------------------------------------------------------------
# left shifting
# arr=[5,10,15,20,25,30]
# pos=1
# for i in range(0,len(arr)-pos):
#     arr[i]=arr[i+pos]                #[10, 15, 20, 25, 30, 30]
# for i in range(-1,pos-1):
# # for i in range(len(arr)-pos,len(arr),1):
#     arr[i]=0                        #[10, 15, 20, 25, 30, 0]
# print(arr)


# o/p=[10,15,20,25,30,0]



# ---------------------------------------------------------------------------
# arr = [5,10,15,20,25,30,25]
# pos = 3
# for i in range(len(arr)-pos, len(arr)):
#     arr[i] = 0
# print(arr)


# o/p=[5,10,15,20,0,0,0]

# ------------------------------------------------------------------------------------------
arr=[5,10,20,25]
pos=2
insert=15
for i in range(len(arr)+1):
    arr[pos]=insert
for i in range(pos,len(arr)):
    arr[i]=arr[i-1]

print(arr)

# This is the incomplete code
