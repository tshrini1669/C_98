def swappingData():
    getfilename = input("Enter The File Name here - ")
    getfilename2 = input("Enter the second file name here  - ")

    with open(getfilename, 'r') as a:
        data_a = a.read()
    with open(getfilename2, 'r') as b:
        data_b = b.read()
    with open(getfilename, 'w')  as a:
        a.write(data_b)
    with open(getfilename2 , 'w') as b:
        b.write(data_a)  
    print("Swapping Is Done, Check your files")      
swappingData()        