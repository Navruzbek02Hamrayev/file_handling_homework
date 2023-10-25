def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l=[]
    f=open(data).read()
    for i in f:
        if i.isdigit():
            l.append(int(i))
            s=0
            sum=l[0]
            while s<len(l):
                sum+=l[s]
                s+=1
    return sum
# Read data from file
print(main("data/data07.txt"))