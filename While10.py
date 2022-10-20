def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    ans=0
    while  i<len(s):
        if s[i].isdigit():
            if int(s[i])%2==1:
                   ans+=1    
        i+=1          
    sum=ans+i    
    return sum
print(main('113540'))