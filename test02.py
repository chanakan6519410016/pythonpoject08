# -------------- Dictionary คือ ข้อมูลหลายข้อมูล ที่เป็น key:value แก้ไขได้ ไม่มีลำดับ ซ้ำได้ -----
# key เป็น String/Integer ส่วน value เป็นอิหยังก็ได้ (number,string ,booleean,list tuple,set dictionary)
my_dict1 = {'name':'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30,]}
my_dict2 = {'data1':[10, 30, 40], 
               'data2':(2, 5, 6),
            'date3':(45, 3, 4,),
             'date4':{ 'x':111,
                        'y':222
                     }
}
# การเข้าถึงข้อมูลใดข้อมูลหนึ่ง
print(my_dict1['name'])
print(my_dict1[555])
my_dict1['age'] = 50
print(my_dict1)


# การเข้าถึงทุกข้อมูล