def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
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
            min=l[0]
            while s<len(l):
                if min>l[s]:
                    min=l[s]
                s+=1
    return min
# Read data from file
print(main("data/data09.txt"))