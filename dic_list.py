dic1={'name':'Ali','age':22 , 'av': True} 
dic2 = {'name':'ahmad','age':23 ,'li':[]}
list= [dic1,dic2]
 
print (list)

for i in list:
    if i.get('li') is not None:
        i['li'].append('newvalue')

print (list)

