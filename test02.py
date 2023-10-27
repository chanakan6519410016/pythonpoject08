# -------------- Dictionary คือ ข้อมูลหลายข้อมูล ที่เป็น key:value แก้ไขได้ ไม่มีลำดับ ซ้ำได้ -----
# key เป็น String/Integer ส่วน value เป็นอิหยังก็ได้ (number,string ,booleean,list tuple,set dictionary)
my_dict1 = {'name':'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30,]}
my_dict2 = {'data1':[10, 30, 40], 
            'data2':(2, 5, 6),
            'data3':(45, 3, 4,),
            'data4':{ 'x':111,
                        'y':222
                     }
}
# การเข้าถึงข้อมูลใดข้อมูลหนึ่ง
print(my_dict1['name'])
print(my_dict1[555])
my_dict1['age'] = 50
print(my_dict1)
# อยากแสดงผล 20 ออกมาทำไง
print(my_dict1['wow'][1])
# อยากแสดงผล 222 ออกมาทำไง
print(my_dict2['data4']['y'])
print(my_dict2)
my_dict2['data5'] = 888
print(my_dict2)

# การเข้าถึงทุกข้อมูล
# อยากได้ key ไม่ต้อง .key ก็ได้
for xx in my_dict1 :
    print(xx)

# อยากได้ข้อมูลให้มี .values
print('------------------')
for xx in my_dict1.values() :
    print(xx)

# อยากได้ทั้ง Key และ values ให้ใช้ .items สร้าง 2 ตัวแปร
print('------------------')
for xx,yy in my_dict1.items() :
    print(xx, '-', yy)

# Dictionary method
my_dict1.popitem()
my_dict1.popitem()
my_dict1.popitem()
print(my_dict1)
my_dict2.pop('data3')
print(my_dict2)
print('-----------------')
print(my_dict2['data2'])
print(my_dict2.get('data2'))
