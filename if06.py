def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    z=0
    if a<0:
        z=z+1
    if b<0:
        z=z+1
    if c<0:
        z=z+1
    s=0
    if a>0:
        s=s+1
    if b>0:
        s=s+1
    if c>0:
        s=s+1
    if z>s: 
        return "there are a lot of negative numbers"
    if z<s:
        return "there are a lot of positive numbers"
print(main(2,3,-5))