def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
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
            max=l[0]
            s=0
            while s<len(l):
                if max<l[s]:
                    max=l[s]
                s+=1
    return max
# Read data from file
print(main("data/data08.txt"))