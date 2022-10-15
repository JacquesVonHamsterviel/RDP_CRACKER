import itertools
    
char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num={"0","1","2","3","4","5","6","7","8","9"}



a=itertools.product(char,repeat=9)

for i in a:
    pwd=""
    for j in i:
        pwd+=j
    print(pwd)
