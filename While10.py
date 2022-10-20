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
                   ans+=int(s[i])   
        i+=1          
    return ans
print(main('3017'))