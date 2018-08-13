# -*- coding:utf-8 -*-
import json
def cz(USER,PASSWD,user_state):
    while user_state == True:
        with open('./user/%s.json'%USER,'r') as r:
            user_o = json.load(r)
        try:
            money_n = int(input('请输入充值金额（元）：'))
        except:
            print('只能是整型')
        try:
            user_o['money'] = int(user_o['money'])+int(money_n)
        except:
            print('充值失败')
            continue
        try:
            with open('./user/%s.json'%USER,'w') as O_W:
                json.dump(user_o,O_W)
                break
        except:
            print('充值失败！')
            break

def zhuanzhang(USER,PASSWD,user_state):
    while user_state == True:
        try:
            UPWD = './user/%s.json' % USER
            with open(UPWD, 'r') as f:
                user_info = json.load(f)
                print('您当前的余额为：',user_info['money'])
        except:
            print('账号有问题！')
            break
        try:
            user = input('请输入对方的用户名:')
            mon = int(input('请输入需要转账的金额：'))
            if mon > user_info['money']:
                print('你没有那么多的钱')
                break
            else:
                with open('./user/%s.json'%USER, 'w') as f:
                    yu_e = float(user_info['money']) - float(mon)
                    json.dump(yu_e, f)
                with open('./user/%s.json'%user,'r') as f:
                    jieshou = float(json.load(f)['money'])
                with open('./user/%s.json'%user, 'w') as f:
                    yu_e = float(jieshou) + float(mon)
                    json.dump(yu_e, f)
        except:
            print('账号或金额有问题（必须是整型）')
            break

def run(USER,PASSWD,user_state):
    while user_state == True:
        UPWD = './user/%s.json' % USER
        with open(UPWD, 'r') as f:
            user_info = json.load(f)
        print('------Welcome < %s > de ATM----- ' % USER)
        print('1.提现')
        print('2.转账')
        print('3.注销')
        print('4.冻结')
        print('5.充值')
        print('0.退出')
        choose = int(input('你的操作：'))
        if choose == 1:
            try:
                with open(UPWD,'w') as f:
                    user_info['money'] = 0
                    json.dump(user_info,f)
                    print('提现成功！')
            except:
                print('提现失败!')
        elif choose == 2:
            zhuanzhang(USER,PASSWD,user_state)
        elif choose == 3:
            print('欢迎下次再来！')
            exit()
        elif choose == 4:
            try:
                with open(UPWD, 'w') as f:
                    user_info['flag'] = '1'
                    json.dump(user_info, f)
                    print('冻结账号成功！')
                    return True
            except:
                print('冻结失败！')
        elif choose == 5:
            cz(USER,PASSWD,user_state)
        elif choose == 0:
            break
        else:
            print("输入错误,即将返回")
            break


