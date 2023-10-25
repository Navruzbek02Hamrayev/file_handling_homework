def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    f=open(data).read()
    for i in f:
        if i.isdigit():
            l.append(int(i))
    return l
# Read data from file
print(main("data/data03.txt"))