def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x=[]
    f=open(data).read().split("\n")
    for i in f:
        x.append(len(i))
    return x
# Read data from file
print(main("data/data06.txt"))