def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    ans1=0
    ans2=0
    while  i<len(s):
        if s[i].isdigit():
            if int(s[i])%2==0:
                   ans1+=int(s[i])

        if s[i].isdigit():                  
            if int(s[i])%2==1:
                   ans2+=int(s[i])
        i+=1  
    sum=ans1+ans2
    return sum
print(main('124'))     