# in taklif darbare ye jamee bood . 
def sum(a,b):
    r=0
    for k in range(a,b+1):
        r += k
    print(r)
    # alan return mizanam ta r beshe khorooji .
    return(r)

# alan joori hast ke a va b migire inja too input va baad tahvil mide . 
print("a ro bego=")
a=int(input())
print("b ro bego=")
b=int(input())
print("javab shoma=")
sum(a,b)

