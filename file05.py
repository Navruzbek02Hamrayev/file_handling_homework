def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    l1=[]
    f=open(data).read()
    for i in f:
        if i.isdigit():
            l.append(str(i))
    for i in f:
        for a in i:
            if not i.isdigit():
                l1.append(str(i))
    return [len(l),len(l1)]
# Read data from file
print(main("data/data05.txt"))