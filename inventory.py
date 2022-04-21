while True :
    i=input("Input Data Inventory Baru (Ya/Tidak)?")
    if i == "Ya" or i == "Ya":
        file = open ("db-inventory.txt","a")
        print("*"*40)
        x = input("Input Nama Perangkat :")
        y = input("Input Lokasi :")
        print("*"*40)
        file.write("Nama Perangkat : "+x+", \t Lokasi "+y+"\n")
        file.close()
    elif i == 'Tidak' or i == 'Tidak':
        file = open("db-inventory.txt","r")
        print("*"*40)
        for item in file:
            item = item.strip()
            print(item)
        break