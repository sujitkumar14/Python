def binarySearch(ordered_list,find_number,l,r):
    if l>r:
        return False
    middle = (r-l)/2
    if find_number==ordered_list[middle]:
        return True
    elif find_number<ordered_list[middle]:
        return binarySearch(ordered_list,find_number,l,middle-1)
    elif find_number>ordered_list[middle]:
        return binarySearch(ordered_list,find_number,middle+1,r)
    return False


if __name__=="__main__":
    ordered_list = map(int,raw_input().split());
    find_number = int(raw_input("Enter which number you have to find"))
    print binarySearch(ordered_list,find_number,0,len(ordered_list)-1)
    print ordered_list
