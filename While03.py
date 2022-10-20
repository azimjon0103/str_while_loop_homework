def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0  
    ans1=0
    ans2=0
    while i<len(s):
        if s[i].isdigit():
            ans1+=1   
        if s[i].isalpha():
            ans2+=1    
        i+=1
    return len(s)-ans1-ans2
print(main('#hash52t&^%$#@!ag@$'))