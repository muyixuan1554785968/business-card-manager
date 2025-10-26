from logging import exception

print('*******************************')
print('欢迎时使用【名片管理系统】')
print('1、新建名片')
print('2、显示全部')
print('3、查询名片')
print('0、退出系统')
print('*******************************')


users={'李宇豪':{'name':'李宇豪','phone':'18366160710','qq':'1554785968','mail':'1554785968@qq.com'}}
def add_info(name,phone,qq,mail):
    users.update({name:{'name':name,'phone':phone,'qq':qq,'mail':mail}})
    return True
while True:
    elect=input('请输入你要进行的操作：')
    try:
        if elect=='1':
            name=input('请输入你的姓名：')
            phone = input('请输入你的电话：')
            qq = input('请输入你的qq：')
            mail = input('请输入你的邮箱：')
            result=add_info(name,phone,qq,mail)
            if result:
               print('成功新建文件')
            else:
                print('请重试')
        elif elect=='2':
            for i in users:
                print(users.get(i))
        elif elect=='3':
            name1=input('请输入你要查询的姓名')
            for i in users:
               if name1==i:
                   print(users.get(i))
                   op2=input('输入4删除名片：')
                   if op2=='4':
                       users.pop(i)
                       print('删除成功！')
                   else:
                       print('请输入正确操作')
               else:
                   print('未找到你要找的用户')
        elif elect=='0':
            print('欢迎再次使用该系统！！！')
            break
        else :
            raise Exception ('请输入正确的操作')
    except Exception as e:
        print(e)