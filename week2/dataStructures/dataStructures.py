Data1 = (7, False, "Apple", True, 7, 98.6) 
print( len(Data1) )
print(Data1[3])
print( Data1.count(7) )

Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}
Data2.pop()
Data2.add("Alpha")
print( Data2 )

Data3 = ["A", 7, -1, 3.14, True, 7]  
Data3.reverse()
Data3[1] = 'B'
Data3.pop()
print(Data3)

Data4 =  { "name":"Joe",  "age" : 26,   "active" : True,  "hourly_wage" : 14.75 }
Data4["active"] = False
Data4["address"] = '123 West Main Street'
pay = Data4["hourly_wage"] * 40
print( pay )
print(Data4)