# harry-s-string
#Harry was studying a magic book that categorizes the magic spells into 3 categories - Good , Worst and Bad. If any spell contains all the vowels in alphabetical order then that spell is categorized as Good. If it contains the vowels in reverse alphabetical order , then that spell is categorized as Worst. All the other spells that do not fall in any of the categories before are categorized as Bad. 

#Now Harry tries to evaluate himslef by solving a spell categorization exercise at the end of the book , but since he is confused can you help him by solving the problems.

#Note: The spell is a word of lower case English alphabets only. If there are no vowels in the string, then the spell is classified as "Good".


t=int(input())
while t!=0:
    s=input()
    l=[]
    for i in s:
        if i in 'aeiou':
            l.append(i)
    s1=sorted(l)
    s2=sorted(l,reverse=True)
    if s1==l:
        print("Good")
    elif s2==l:
        print("Worst")
    else:
        print("Bad")
    t=t-1>
