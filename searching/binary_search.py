

def binary_search(arr, target):
    
    low = 0
    right = len(arr)-1
    
    while low <= right:
        mid = (right+low)//2

        if(arr[mid] == target):
            return mid

        elif(arr[mid] < target):
            low = mid + 1
        
        else: 
            right = mid - 1
    
    return -1

target = 5
arr = [1, 4, 5, 6, 8, 10, 12, 15]
print(binary_search(arr, target))
