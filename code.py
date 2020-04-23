# --------------
def palindrome(num):
    k=num
    length=len(str(k))
    if length%2==1:
        new=str(k)[:(length//2)]+str(int(str(k)[length//2])+1)+str(k)[:length//2][::-1]
    else:
        new=str(k)[:(length//2)-1]+str(int(str(k)[(length//2)-1])+1)*2+str(k)[:(length//2)-1][::-1]
    return int(new)






# --------------
def a_scramble(str_1, str_2):
    set2=list(set(str_2))
    for i in set2:
        if (str_2.casefold()).count(i.lower())<=(str_1.casefold()).count(i.lower()):
            continue
        else:
            return False
    return True 



# --------------
def check_fib(num):
    k1=5*(num*num)+4
    k2=5*(num*num)-4
    
    if k1==int(k1**(1/2))*int(k1**(1/2)) or k2==int(k2**(1/2))*int(k2**(1/2)):
        return True
    return False



# --------------
#Code starts here
def compress(word):
    s=word.lower()
    b=" "
    i=0
    while(i<len(s)):
        if b[-1]!=s[i]:
            cnt=0
            b+=s[i]
        while(i<len(s) and b[-1]==s[i]):
            cnt+=1
            i+=1
        b+=str(cnt)
    return b[1:]




# --------------
#Code starts here
def k_distinct(string,k):
    string=string.lower()
    if len(list(set(string)))==k:
        return True
    return False


