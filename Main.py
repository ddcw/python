# -*- coding:utf-8 -*-
import time
import _thread
import json
import ATM
Shopping_cart = {}
Market = {}
USER = ''
PASSWD = ''
CHAO_E = 0
user_state = False
SPWD = './shopping/shop.json'



# -*- coding:utf-8 -*-
#expandtion.txt文件里保存了账号和密码，这里定义一个函数，以dict的形式提取数据，用于注册时候判断

# def user_menu():
#     print("1.登录用户")
#     print("2.注册新用户")
#     print("3.修改密码")
#     print("0.退出")
#     choice = input("请输入你的选择:")
#     if choice == "1":
#         Login()
#     elif choice == "2":
#         regist()
#     elif choice == "3":
#         modify_pwd()
#     elif choice == "0":
#         exit()
#     else:
#         print("输入错误，请重新选择：")
# def Login():
#     global get_user
#     # 因为刚才有注册，所以要重新调用文件读取函数获取账号信息
#     user_pass = get_user_pass('expandtion.txt')
#     # 设置i用来记录登录信息输入错误次数啊
#     i = 1
#     while i < 4:
#         print('第%s次登录,登录超过三次仍然失败，将不允许登录，请三思!' % i)
#         i += 1
#         get_user = input('请输入登录用户名：')
#         get_pass = input('请输入登录密码：')
#         # 判断账号是否存在expandtion.txt文件中
#         if get_user not in user_pass.keys():
#             print('账号或密码有误，请重新输入！')
#             continue
#         else:
#             # 根据账号获取到该账号的密码
#             password = user_pass[get_user]
#             # 判断密码是否和对应的账号匹配
#             if get_pass != password:
#                 print('账号或密码有误，请重新输入！')
#                 continue
#             else:
#                 print('欢迎%s登录！' % get_user)
#                 break
#     # 登录超过三次时给出提示
#     else:
#         print('账号或密码错误次数已超过三次，请明年再来登录！')
# def regist():
#     user_pass = get_user_pass('expandtion.txt')
#     while True:
#         username = input_data('注册账号', 'name')
#         # 判断注册账号是否存在，已存在的话持续循环
#         if username in user_pass.keys():
#             print('您输入的账号已存在，请重新输入：')
#             continue
#         else:
#             password = input_data('账号密码', 'name')
#             confirm_pass = input_data('确认密码', 'name')
#             # 判断确认密码和密码是否一致
#             if password != confirm_pass:
#                 print('您输入的确认密码与密码不一致，请重新输入:')
#                 continue
#             else:
#                 print('恭喜您注册成功，请记住您的注册信息：\n您的账号是:%s\n您的密码是:%s' % (username, password))
#                 break
#     # 将新注册的用户写入expandtion.txt保存
#     with open('expandtion.txt', 'a') as f:
#         f.write(username + ',' + password + '\n')
# def get_user_pass(file):
#     user_passwd = {}
#     with open(file, 'r') as f:
#         for d in f:
#             for kv in [d.strip().split(',')]:
#                 user_passwd[kv[0]]=kv[1]
#     return user_passwd
#     # 定义一个函数，判断输入的参数是否为空，为空的话继续输入，直到输入不为空为止
# def input_data(data_type,get_data):
#     while True:
#         get_data=input('请输入%s：'%data_type)
#         if len(get_data)==0:
#             continue
#         else:
#             break
#     return get_data


# def modify_pwd():
#     user_pass = get_user_pass('expandtion.txt')
#     i = 1
#     while i < 4:
#         print('第%s次修改,修改超过三次仍然失败，将不允许修改，请三思!' % i)
#         i += 1
#         get_user = input('请输入登录用户名：')
#         get_pass = input('请输入登录密码：')
#         # 判断账号是否存在expandtion.txt文件中
#         if get_user not in user_pass.keys():
#             print('账号或密码有误，请重新输入！')
#             continue
#         else:
#             # 根据账号获取到该账号的密码
#             password = user_pass[get_user]
#             # 判断密码是否和对应的账号匹配
#             if get_pass != password:
#                 print('账号或密码有误，请重新输入！')
#                 continue
#             else:
#                 new_pwd = input('请输入新密码：')
#                 get_pass = new_pwd
#                 with open('expandtion.txt', 'a') as f:
#                     f.write(get_user + ',' + get_pass + '\n')
#                 break
# user_menu()
def Login(logs):
    def yanzheng(*args,**kwargs):
        global user_state
        global USER
        global PASSWD
        if user_state == True:
            RET = '%s登陆成功'%USER
            logs(RET)
        while user_state == False:
            print('====欢迎来到登录界面====')
            user = input('your name:\t\t')
            password = input('your password：\t')
            Upwd = './user/%s.json'%user
            try:
                with open(Upwd, 'r') as f:
                    if password == json.load(f)['password']:
                        with open(Upwd, 'r') as f:
                            flags = json.load(f)['flag']
                            if flags == '1':
                                print('该用户已被冻结')
                                flags = '%s 用户尝试登录' % user
                                log(flags)
                                exit()
                        print('Welcome ', user)
                        print("=================================")
                        user_state = True
                        USER = user
                        PASSWD = password
                    else:
                        print('密码错误，请重新输入：')
            except FileNotFoundError:
                print('用户名错误！')
                continue
            ret = '%s登陆成功'%user
            log(ret)
            logs(ret)

    return yanzheng

@Login
def logs(action):
    with open('./log/logs.txt','a') as f:
        f.write(action+'\t\t'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ '\n')

def log(action):
    u_log = './log/%s.txt'%USER
    with open(u_log,'a') as f:
        f.write(action+'\t\t'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+ '\n')


def Regist():
    global USER
    global PASSWD
    global user_state
    while True:
        print('-------欢迎来到注册界面--------')
        username = input('请输入用户名：')
        # UPWD = './user/%s.json' %USER
        password = input('请输入密  码:')
        Upwd = './user/%s.json'%username
        try:
            with open(Upwd, 'r') as f:
                if username == json.load(f)['username']:
                    print('用户名也存在\n\n')
                    continue
        except FileNotFoundError:
            data = {'username':username,'password':password,'money':'1000','flag':'0'}
            with open(Upwd, 'w') as f:
                json.dump(data,f)
            USER = username
            PASSWD = password
            user_state = True
            act = '%s注册成功！'%USER
            log(act)
            logs(act)
            break

def time_rate(type,minute):
    while True:
        while user_state == True:
            if type == 'zhangdan':
                while True:
                    if minute == time.strftime("%M", time.localtime()):
                        f = open('./log/logs.txt')
                        for i in f.readlines():
                            print(i)
                    else:
                        break
            elif type == 'huankuan':
                while True:
                    if minute == time.strftime("%M", time.localtime()):
                        # UPWD = './user/%s.json'%USER
                        # with open(UPWD, 'r') as f:
                        #     data = json.load(f)['money']
                        #     print(data)
                        #     print(type(data))
                        #     print(type(data['money']))
                        #     if float(data['money']) > 0:
                        #         data['money'] = data['money']*0.00005
                        #         json.dump(data,f)
                            print('请还款！，有利息的哟...')
                    else:
                        break
            else:
                print('error')
        time.sleep(5)

try:
    _thread.start_new_thread(time_rate,('zhangdan','44'))
    _thread.start_new_thread(time_rate, ('huankuan', '55'))
except:
    print('SB')

def Add_card():
    while user_state ==True:
        try:
            card_n = int(input('请输入你的卡号：'))
        except:
            print('只能是数字')
            continue
        try:
            with open('./card/%s.json'%USER, 'r') as cr:
                c_n = json.load(cr)
                c_n[card_n] = 1000
            with open('./card/%s.json'%USER, 'w') as c:
                json.dump(c_n,c)
                print('添加成功：%s'%card_n)
                break
        except:
            print('失败!,将重置你的卡包')
            with open('./card/%s.json'%USER, 'w') as c:
                da = {123:123}
                json.dump(da,c)
            break


def Person():
    try:
        with open('./card/%s.json'%USER, 'r') as cr:
            print('====================')
    except:
        with open('./card/%s.json'%USER, 'w') as c:
            da = {}
            json.dump(da, c)
    while user_state == True:
        UPWD = './user/%s.json'%USER
        with open(UPWD,'r') as f:
            user_info = json.load(f)
        print('--------%s---------\n'%USER)
        print('1.我的余额')
        print('2.我的卡包')
        print('3.添加信用卡')
        print('4.修改密码')
        print('5.转账')
        print('6.提现')
        print('0.退出')
        choose = int(input('你的操作：'))
        if choose == 1:
            print('你的余额为：',user_info['money'])
        elif choose == 2:
            print('')
            try:
                with open('./card/%s.json'%USER,'r') as c:
                    print(json.load(c))
                #     c_o = json.load(c)['test']
                #     print(c_o)
                # for i in c_o:
                #     print(i,)
            except:
                print('你还没有没有卡....')
                with open('./card/%s.json'%USER,'w') as c:
                    da = {123:123}
                    json.dump(da,c)
                continue
        elif choose == 3:
            Add_card()
        elif choose == 4:
            user_info['password'] = input('请输入你的新密码：')
            data = user_info
            with open(UPWD, 'w') as f:
                json.dump(data,f)
        elif choose == 5:
            ATM.zhuanzhang(USER,PASSWD,user_state)
        elif choose == 6:
            try:
                with open(UPWD,'w') as f:
                    user_info['money'] = 0
                    json.dump(user_info,f)
                    print('提现成功！')
            except:
                print('提现失败!')
        elif choose == 0:
            break
        else:
            print("输入错误")

def Shop():
    # with open('./shopping/shop.json', 'r') as f:
    #     Shopping_cart = json.load(f)
    # global Shopping_cart,Market
    SPWD = './shopping/shop.json'
    try:
        with open(SPWD,'r') as f:
            Market = json.load(f)
    except:
        print('./shopping/shop.json 为空')
    while True:
        print("welcome to SHOP!")
        print("商品\t价格")
        for i in Market.keys():
            print(i,'\t',Market[i])
        print("------0.退出------")
        Shop_n = input('请选择你需要购买的商品：')
        if Shop_n == '0':
            break
        try:
            Market[Shop_n]
            print('正在加入购物车: ',Shop_n,'单价：',Market[Shop_n],' 元')
        except KeyError:
            print('输入非法，请重新输入.....')
            continue
        try:
            Shopping_cart[Shop_n] += 1
            print(Shop_n,'  加入购物车成功!!!',)
        except KeyError:
            Shopping_cart[Shop_n] = 1
            print(Shop_n, '  加入购物车成功!!!', )
        act = '购买了%s'%Shop_n
        log(act)
    return

def Shopping_car():
    global Shopping_cart
    for i in Shopping_cart.keys():
        print(i,'\t',Shopping_cart[i])
    while True:
        print('-----------------------')
        print('1.全部购买')
        print('2.全部删除')
        print('3.显示购物车物品')
        print('4.充值')
        print('0.退出')
        print('-----------------------')
        choose_s_c = input('请输入你的选择：')
        if choose_s_c == '1':
            sum = 0
            for i in Shopping_cart.keys():
                with open(SPWD,'r') as f:
                    danjia = int(json.load(f)[i])
                shuliang = int(Shopping_cart[i])
                sum += danjia*shuliang

            print('总共：',sum," 元")
            with open('./user/%s.json'%USER,'r') as f:
                money = json.load(f)['money']
                if sum - float(money) > CHAO_E:
                    print('余额不足')
                    continue
            with open('./user/%s.json'%USER,'w') as f:
                yu_e = float(money) - float(sum)
                json.dump(yu_e,f)
                print('全部购买成功！')
            act = '付款了 %s'%sum
            log(act)
            Shopping_cart = {}
        elif choose_s_c == '2':
            try:
                Shopping_cart = {}
                logs('清空购物车成功！')
                print('清除购物车成功！')
            except:
                print('清除购物车失败！！')
        elif choose_s_c == '3':
            print('商品\t','数量')
            for i in Shopping_cart.keys():
                print(i, '\t', Shopping_cart[i])
        elif choose_s_c == '4':
            ATM.cz(USER,PASSWD,user_state)
        elif choose_s_c == '0':
            break
        else:
            print('输入有误！')


    return

if user_state == False:
    print('----------------')
    print('-----1.登录-----')
    print('-----2.注册-----')
    print('----------------')
    act = input('请输入你的操作：')
    if act == '2':
        Regist()
    else:
        logs()

while user_state == True:
    print('------Welcome < %s > to Main Menu----- '%USER)
    print('1.商场')
    print('2.注册')
    print('3.购物车')
    print('4.个人中心')
    print('5.ATM')
    print('0.退出')
    choose = int(input('你的操作：'))
    if choose == 1:
        Shop()
    elif choose == 2:
        Regist()
    elif choose == 3:
        Shopping_car()
    elif choose == 4:
        Person()
    elif choose == 5:
        if ATM.run(USER,PASSWD,user_state) == True:
            exit()
    elif choose == 0:
        exit()
    else:
        print("输入错误")






