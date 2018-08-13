import json
data = {'user':'ygs','password':'123'}
maeket = {'iphone':800,'water':10,'HuoTui':2,'MiFan':5,'Mnnkey':66,'PiJiu':45}
# data2 = {'c':2,'d':3}
with open('./shopping/shop.json','w') as f:
    json.dump(maeket,f)


# with open('./user/ygs.json','r') as f:
#     if json.load(f)['password'] == '123':
#         print('OK')
#     print(json.load(f)['password'])
#     a = json.loads(f)['password']
#     print(a)
# a = '123'
# b = '456%s'%a
# print(b)