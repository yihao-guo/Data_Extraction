import re
import fileinput
'''
string = open('latency.txt','r', encoding='UTF-8').read()

pattern = re.compile(r'(?<=written_time=)\d+\.?\d*')
print(pattern.findall(string))
'''
arr_str = ["threshold [(]4,3[)]", "threshold [(]13,9[)]", "threshold [(]22,15[)]", "threshold [(]31,21[)]",
           "threshold [(]40,27[)]", "threshold [(]49,33[)]", "threshold [(]58,39[)]",""]
speed = ["speed : 180", "speed : 140", "speed : 140", "speed : 80", "speed : 100",
         "speed : 60", "speed : 20"]
result = []
for i in range(0,len(arr_str)-1):

    with open('tps1.txt', encoding='UTF-8') as fin, open('c.txt', 'w', encoding='UTF-8') as fout:
        text = fin.read()

        print("-----------------")

        matches_1 = re.search(arr_str[i]+'(.*)'+arr_str[i+1], text, re.DOTALL).group()


        matches_2 = re.search(speed[i]+'(.*)'+arr_str[i+1], matches_1, re.DOTALL).group()
        print(matches_2)
        valid_keys_str = r'(?<=valid keys : )\d+\.?\d*'
        b = re.compile(valid_keys_str)
        valid_keys = b.findall(matches_2)
        valid_keys_num = list(map(int, valid_keys))
        matches_3 =[]
        #print("aaa",valid_keys_num)
        fout.write(matches_2)
        fout.close()
        tt = ["tx_sum : "]#不用改
        fin.close()
    with open('c.txt', 'r',encoding='UTF-8') as f:

        #print(valid_keys_num)
        for line in f.readlines():
            if re.search(tt[0]+valid_keys[0], line):
                matches_3.append(line)
        f.close()
        f = open('c.txt', 'w',encoding="UTF-8")
        f.writelines(matches_3)
        f.close()
    #获取tps的值计算平均值
    with open('c.txt', 'r',encoding='UTF-8') as ff:
        f = ff.read()
        #print(f)
        str = r'(?<=tps : )\d+\.?\d*'
        pattern = re.compile(str)
        a = pattern.findall(f)
        print(a)
        num_a = list(map(float, a))
        print(num_a)
        sum = 0
        ff.close()
        for i in num_a:
            sum+=i
        if(len(num_a)!= 0):
            average = sum/len(num_a)
            result.append(average)
            sum = 0
        else:
            print("无可用数值！")
            result.append(0)
            sum = 0
        #print(average)

print(result)
f = open('result.txt', 'w',encoding = "UTF-8")
for i in result:
    f.write(repr(i))
    f.write(", ")
f.close()

















# string1 = open('latency.txt',encoding='utf-8')
# a = string1.read()
# print(type(a))
# pattern = re.compile(r'(?<=written_time=)\d+\.?\d*')
# print(type(pattern))
# pattern.findall(string1)
'''
line = "hello this is gyh !"
pattern = "is i"
matchObj = re.match(pattern,line)#首字符匹配
print(matchObj)
m = re.search(pattern, line)#整个匹配返回第一个
print(m)
patt = 'ell'
name = re.sub(patt,"hehe",line)#替换
print(name)
line2 = "hahayihahjuhghahahhh211"
pa = 'haha'
p = re.compile(pa)
res = p.findall(line2)
print(res)
it = re.finditer(r'3',"12a32bc43fj3")
for match in it:
    print(match.group())
'''