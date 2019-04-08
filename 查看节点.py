
# dic={
#     '植物':{
#         '草本植物':
#             ['牵牛花','瓜叶菊','葫芦','翠菊','冬小麦','甜菜'],
#         '木本植物':
#             ['乔木','灌木','半灌木','如松','杉','樟'],
#         '水生植物':
#             ['荷花','千屈菜','菖蔳','黄菖蔳','水葱','再力花','梭鱼草']},
#     '动物':
#         {'两栖动物':
#             ['山龟','山鳖','石蛙','娃娃鱼','蟾蜍','龟','鳄鱼','蜥蜴','蛇'],
#          '禽类':
#             ['雉鸡','原鸡','长鸣鸡','昌国鸡','斗鸡','长尾鸡','乌骨鸡'],
#          '哺乳类动物':
#             ['虎','狼','鼠','鹿','貂','猴','貘','树懒','斑马','狗']}
#     }
db={
    '广西':{
        '南宁':{
            '武鸣':{},
            '江南':{}
        }
    },
    '广东':{
        '深圳':{
            '宝安':{},
            '南山':{}
        }
    }
}
path=[]
while True:
    term=db
    for i in path:
        term=term[i]
    print('当前的path^^^^^^^^^^',path)
    print('当前节点的所有子节点：',list(term.keys()),'\n')

    choice=input('1:添加节点；2：查看节点（Q退出、返回上一级B） 、\n>>>')

    if choice == '1':
        k=input('请输入添加的子节点名称：')

        if k in term:
                print('该节点已经存在')
        else:
                term[k]={}
    elif choice =='2':
        k = input('请输入查看的子节点名称：')
        if k in term:
            path.append(k)
        else:
            print('子节点名称错误')
    elif choice.lower()=='b':
        if path:
            print('返上一节点path',path)
            path.pop()
            print('当前节点path', path)
    elif choice.lower()=='q':
        break
    else:
        print('输错了')