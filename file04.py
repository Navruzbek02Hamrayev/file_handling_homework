def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    f=open(data).read()
    for i in f:
        for a in i:
            if not i.isdigit():
                l.append(str(i))
    return l
# Read data from file
print(main("data/data04.txt"))