def find_pairs_of_numbers(num_list,n):
    #Remove pass and write your logic here
    count=0
    flag=0
    a=list(set(num_list))
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            b=a[i]+a[j]
            if b==n:
                count+=1
            
    return count
    
num_list=[1, 2, 4, 5, 6]
n=10
print(find_pairs_of_numbers(num_list,n))
