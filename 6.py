
#dict={"k1":"v1","k2":"v2","k3":"v3""}
#请循环遍历出所有的key
#请循环遍历所有的value
#请在字典中增加一个键值对，”k4“：”v4“

dict={"k1":"v1","k2":"v2","k3":"v3"}
for key in dict:
    print("key")
for vaiue in dict:
    print("vaiue")
dict["k4"]="v4"
print(dict)

#小明，小刚去超市里购买水果
#小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。以姓名做key，value仍然是字典


#
Friuts = {"苹果":12.3,  # 水果和单价
                 "草莓":4.5,
                 "香蕉":6.3,
                 "葡萄":5.8,
                  "橘子":6.4,
                 "樱桃":15.8
}
info = {
    "小明":{ "fruits": {"苹果":4, "草莓":13, '香蕉':10}, 'money: ?? }, "小刚": { "fruits': {"葡萄":19, "橘子":12,"樱桃":30},  "money":??}}

str1="money"
for k1 in info:
     for k2 in info[k1]:
              money=0
              for k3 in info[k1][k2]:
                  money +=  friuts[k3]*info[k1][k2][k3]
                  info[k1][k2][str1]=money
            print(info)

   #  编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
def numcount(list=[]):
    result={}
    for i in range(len(list)):
        result[list[i]]=list.count(list[i])
        return result
    list=list(input("请输入数字"))
    for i in range(len(list)):
        list[i]=int(list[i])
        print(numcount(list))

#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
name=[
         ["刘备","56","男","106","IBM",500,"50"],
            ["大乔","19","女","230","微软",501,"60"],
             ["小乔","19","女","210","Oracle",600,"60"],
             ["张飞","45","男","230","Tencent",700,"10"]
]
employee=()
for i in name:
    employee[i[0]]=dict({"年龄":[1],
                                        "性别":[2],
                                        "编号":[3],
                                        "任职公司":[4],
                                         "薪资":[5],
                                          "部门编号":[6]})
    print(employee)

