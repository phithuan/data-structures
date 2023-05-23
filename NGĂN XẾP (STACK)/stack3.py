def xaudoixung():
    xdx= 1
    while xdx :
        S=input("Nhap xau S :")
        x =''
        for i in S :
            x= i+x
        if x==S :
            print("Là sâu đối xứng")
        else :
            print("Là xâu không đối xứng")
        print("Ban muon tiep tuc khong? Nhap 1 de tiep tuc, 0 de ket thuc")
        xdx = int(input())
xaudoixung()