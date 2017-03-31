"""
cryptography.py
Author: Earl
Credit: Sam

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
it = True
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"



while it:
    en=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if en=='e':
        m=input("Message: ")
        k=input("Key: ")
        mlist=[]
        klist=[]
        elist=[]
        e=[]
        
        for x in range(0,len(m)):
            mlist.append(associations.find(m[x]))
        for x in range(0,len(k)):
            klist.append(associations.find(k[x]))
        for x in range(0,len(mlist)):
            elist.append(mlist[x]+klist[x%len(klist)])
        for x in range(0,len(elist)):
            e.append(associations[elist[x]%len(associations)])
        print(''.join(e))
        
    elif en == 'd':
        m=input("Message: ")
        k=input("Key: ")
        list=[]
        klist=[]
        dlist=[]
        d=[]
        
        for x in range(0,len(m)):
            mlist.append(associations.find(m[x]))
        for x in range(0,len(k)):
            klist.append(associations.find(k[x]))
        for x in range(0,len(mlist)):
            dlist.append(mlist[x]-klist[x%len(klist)])
        for x in range(0,len(dlist)):
            d.append(associations[dlist[x]%len(associations)])
        print(''.join(d))
        
    elif en == 'q':
        print('Goodbye!')
        it = False    
    else:
        print("Did not understand command, try again.")