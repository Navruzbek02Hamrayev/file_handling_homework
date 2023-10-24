def main(d:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    f=open(d).read().split(",")
    for i in f:
        l.append(int(i))
    return l
# Read data from file
print(main("data/data01.txt"))