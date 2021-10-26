#Ferry / 280
#Mengetahui dan menentukan Kuadran dari koordinat (x,y)

X = int (input("Masukan nilai X ="))
y = int (input("Masukan nilai y ="))

if (X > 0 and y > 0):
    print ("Kuadran 1")
elif (X > 0 and y < 0):
    print ("Kuadran 2")
elif (X < 0 and y < 0):
    print ("Kuadran 3")
elif (X > 0 and y < 0):
    print("Kuadran 4")
elif (X==0 and y==o):
    print ("Titik Pusat")
print("Hasil", X and y)
