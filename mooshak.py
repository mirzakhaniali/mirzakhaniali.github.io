# int hast hamoon adad sahih
# input yaani vared konid
# agar yek harf dar adad zarb shavad angah an harf ra python be tedade adad tekrar mikonad



 
# head mooshak inja vared mishe . 

x=int(input("abaad raas ra vared konid :",))

z=int(x/2)

j=(input("jahat ra begoo :",))

a=int(input("tool har joze az line ra vared konid :",))

b=int(input("tedade badane ra vared konid :",))



def head(x):
    s=" "
    if j=="up":
        s+=(" "*x)
        s+=("^")
        s+=("\n")
        for i in range(x+1):
            s+= " "*(x-i+1)
            s+= "/"*i
            s+= "|"
            s+= "\\"*i + "\n"
        return s
    else:
        for i in range(x+1):
            s+= " "*(i) + ("\\")*(x-i) + ("|") + ("/")*(x-i) + "\n" + " "
        s+=" "*(x) + "v" + "\n"
        return s



# linehe mooshak shamele mahal sookht va yek joda konande dar har sar an .
# in yek tak bakhsh az line ast. 
def tane(a,x,z):
    s= ""
    for _ in range(a):
        s+= "|" + "*"*(x*2+1) + "|" +"\n" 
    s+= "-"*(2*x+3) 
    return s


def line(x,z):
    s= "-"*(2*x+3)
    return s 

    


# tedad line in ast
#deghat konid ke in yeki esmesh lineh va ghabli line bood . h nadasht . 


def mooshak(a,b,x,z):
    k= head(x) 
    k+= line(x,z) + "\n"
    for _ in range (b) :
        k+= tane(a,x,z)+"\n"
    k+= head(x)
    return k

print(mooshak(a,b,x,z))

# bakhsh tahtani ke dige hamoon raase neminevisim . 

# hal ke dade hara darim . miravim soraghe rasm.

