sal_info=dict()
print(sal_info)

sal_info={'Austin':911985, 'Dallas':89999, 'San Jose': 1000989, 'Atlanta': 1023}
print(sal_info)

if ('Dallas' in sal_info):
    print(sal_info['Dallas'])
else:
    print('Not found!')

if('Sacramento' in sal_info):
    print(sal_info['Sacramento'])
else:
    print('Not found!')

for location in sal_info:
    print(sal_info[location])
for location in sal_info:
    print(location)

#sal_info.clear()
#print(sal_info)

if('Seattle' not in sal_info):
    sal_info['Seattle']=110666
else:
    print('key exists')

print(sal_info)

if('Dallas' not in sal_info):
    sal_info['Dallas']=110666
else:
    print('key exists')
