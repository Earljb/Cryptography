"""
cryptography.py
Author: Earl
Credit: Sam

Assignment:

Enter e to encrypt, d to decrypt, or q to quit: z
Did not understand command, try again.
Enter e to encrypt, d to decrypt, or q to quit: e
Message: Two plus two = Five
Key: Lorem ipsum
+KF;B(CH=NIZ}m;R\Dt
Enter e to encrypt, d to decrypt, or q to quit: d
Message: +KF;B(CH=NIZ}m;R\Dt
Key: Lorem ipsum
Two plus two = Five
Enter e to encrypt, d to decrypt, or q to quit: q
Goodbye!

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
"""

on = True
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
 # make list of numbers for message and key
 # add them while compiling a new list
 # print new string
 
 
 
while on:
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if command == 'e':
        m = input("Message: ")
        k = input("Key: ")
        mlist = []
        klist = []
        encryptionlist = []
        encryption = []
         
         
        for i in range(0,len(m)):
            mlist.append(associations.find(m[i]))# creates mlist
        for i in range(0,len(k)):
            klist.append(associations.find(k[i]))# creates klist
        for i in range(0,len(mlist)):#creates encryptionlist
            encryptionlist.append(mlist[i]+klist[i%len(klist)])
        for i in range(0,len(encryptionlist)):
            encryption.append(associations[encryptionlist[i]%len(associations)])
        print(''.join(encryption))
         
    elif command == 'd':
        m = input("Message: ")
        k = input("Key: ")
        mlist = []
        klist = []
        decryptionlist = []
        decryption = []
         
         
        for i in range(0,len(m)):
            mlist.append(associations.find(m[i]))# creates mlist
        for i in range(0,len(k)):
            klist.append(associations.find(k[i]))# creates klist
        for i in range(0,len(mlist)):#creates decryptionlist
            decryptionlist.append(mlist[i]-klist[i%len(klist)])
        for i in range(0,len(decryptionlist)):
            decryption.append(associations[decryptionlist[i]%len(associations)])
        print(''.join(decryption))
         
         
    elif command == 'q':
        print('Goodbye!')
        on = False    
    else:
        print("Did not understand command, try again.")
"""