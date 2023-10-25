def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l=[]
    f=open(data).read().split("\n")
    for i in f:
        l.append(len(i))
        max=l[0]
        s=0
        while s<len(l):
            if max<l[s]:
                max=l[s]
            s+=1
    return max
# Read data from file
print(main("data/data10.txt"))