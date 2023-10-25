def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l=[]
    f=open(data).read()
    for i in f:
        l.append(str(i))
    return len(l)
# Read data from file
print(main("data/data02.txt"))
 