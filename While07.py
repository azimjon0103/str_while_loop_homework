from re import S


def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    ans=0
    while  i<len(s):
        if s[i].isdigit():
            if int(s[i])%2==0:
                   ans+=1    
        i+=1          
    return ans
print(main('1026503'))    