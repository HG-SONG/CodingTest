arr = [1,2,3]
arr2 = set([1,2,3,2,3,2])
arr.insert(0,0)
print(arr2)

dic = {"asd":111 , "zxc":4233, "zxccc": 4}
dic = sorted(dic.items(), key= lambda item: item[1], reverse= True)
