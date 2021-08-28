def back(count):
    if count ==100:
        return count
    count+=1
    print(count , "1")
    back(count)

    count+=1
    print(count)

def solution():
    back(1)
solution()
