import re
result4_3 = []
result13_9 = []
sum = 0
level = ['level : 1','level : 2','level : 3','level : 4','level : 5','level : 6','level : 7',"threshold"]
threshold = ['threshold : [(]22,15[)]','threshold : [(]31,21[)]',"threshold"]
# with open('latency.txt', encoding='UTF-8') as fin, open('c.txt', 'w', encoding='UTF-8') as fout:
#     text = fin.read()
empty = open("result.txt","w",encoding="UTF-8")
empty.write("")

    #print(matches_1)
for i in range(0, len(level)-1):
# with open('latency.txt', encoding='UTF-8') as fin, open('c.txt', 'w', encoding='UTF-8') as fout:
#     text = fin.read()
#
#     #print("-----------------")
#     matches_1 = re.search('threshold : [(]4,3[)](.*?)threshold : [(]13,9[)]', text, re.DOTALL).group()
#     #print(matches_1)
    with open('latency.txt', encoding='UTF-8') as fin, open('c.txt', 'w', encoding='UTF-8') as fout:
        text = fin.read()


        matches_1 = re.search('threshold : [(]4,3[)](.*?)threshold : [(]13,9[)]', text, re.DOTALL).group()
        matches_2 = re.findall(level[i]+'(.*?)'+level[i+1]+'.+'+level[i]+'(.*?)'+level[i+1]+'.+'+level[i]+'(.*?)'+level[i+1], matches_1, re.DOTALL)
        #print(matches_2)
        for i in matches_2:
            fout.write(repr(i))
            fout.close()
            fin.close()
        with open('c.txt', encoding='UTF-8') as f:
            text2 = f.read()
            #print("aaa"+text2)
            #text2 = text2.split("\n")
            str = r'(?<=written_time : )\d+\.?\d*'
            pattern = re.compile(str)
            a = pattern.findall(text2)
            #print(a)
            num_a = list(map(float, a))
            print(num_a)
            for j in num_a:
                sum = sum+j
            if (len(num_a) != 0):
                average = sum / len(num_a)
                result4_3.append(average)
                sum = 0
            else:
                print("无可用数值！")
                result4_3.append(0)
                sum = 0
        f.close()
print("(4,3) leve1~level7:",result4_3)
with open('result.txt','a', encoding='UTF-8') as temp:
    k=0
    for str in result4_3:
        k = k+1
        if k!=7:
            str = repr(str)+","
            temp.write(str)
        else:
            str = repr(str)+"\n"
            temp.write(str)
            temp.close()
for i in range(0, len(level)-1):
# with open('latency.txt', encoding='UTF-8') as fin, open('c.txt', 'w', encoding='UTF-8') as fout:
#     text = fin.read()
#
#     #print("-----------------")
#     matches_1 = re.search('threshold : [(]4,3[)](.*?)threshold : [(]13,9[)]', text, re.DOTALL).group()
#     #print(matches_1)
    with open('latency.txt', encoding='UTF-8') as fin, open('c.txt', 'w', encoding='UTF-8') as fout:
        text = fin.read()


        matches_1 = re.search('threshold : [(]13,9[)](.*?)threshold : [(]22,15[)]', text, re.DOTALL).group()
        matches_2 = re.findall(level[i]+'(.*?)'+level[i+1]+'.+'+level[i]+'(.*?)'+level[i+1], matches_1, re.DOTALL)
        #print(matches_2)
        for i in matches_2:
            fout.write(repr(i))
            fout.close()
            fin.close()
        with open('c.txt', encoding='UTF-8') as f:
            text2 = f.read()
            #print("aaa"+text2)
            #text2 = text2.split("\n")
            str = r'(?<=written_time : )\d+\.?\d*'
            pattern = re.compile(str)
            a = pattern.findall(text2)
            #print(a)
            num_a = list(map(float, a))
            print(num_a)
            for j in num_a:
                sum = sum+j
            if (len(num_a) != 0):
                average = sum / len(num_a)
                result13_9.append(average)
                sum = 0
            else:
                print("无可用数值！")
                result13_9.append(0)
                sum = 0
        f.close()
print("(13,9) leve1~level7:",result13_9)
with open('result.txt','a', encoding='UTF-8') as temp:
    k=0
    for str in result13_9:
        k = k+1
        if k!=7:
            str = repr(str)+","
            temp.write(str)
        else:
            str = repr(str)+"\n"
            temp.write(str)
            temp.close()
result13_9 = []
print("-------------------------------------------")


for j in range(0,len(threshold)-1):
    for i in range(0, len(level) - 1):
        with open('latency.txt', encoding='UTF-8') as fin, open('c.txt', 'w', encoding='UTF-8') as fout:
            text = fin.read()
            matches_1 = re.search(threshold[j]+'(.*?)'+threshold[j+1], text, re.DOTALL).group()
            matches_2 = re.findall(level[i]+'(.*?)'+level[i+1], matches_1, re.DOTALL)
            for i in matches_2:
                fout.write(repr(i))
                fout.close()
                fin.close()
            with open('c.txt', encoding='UTF-8') as f:
                text2 = f.read()
                # print("aaa"+text2)
                # text2 = text2.split("\n")
                str = r'(?<=written_time : )\d+\.?\d*'
                pattern = re.compile(str)
                a = pattern.findall(text2)
                # print(a)
                num_a = list(map(float, a))
                print(num_a)
                for t in num_a:
                    sum = sum + t
                if (len(num_a) != 0):
                    average = sum / len(num_a)
                    result13_9.append(average)
                    sum = 0
                else:
                    print("无可用数值！")
                    result13_9.append(0)
                    sum = 0
    with open('result.txt', 'a', encoding='UTF-8') as temp:
        k = 0
        for str in result13_9:
            k = k + 1
            if k != 7:
                str = repr(str) + ","
                temp.write(str)
            else:
                str = repr(str) + "\n"
                temp.write(str)
        f.close()
    print(threshold[j]," leve1~level7:", result13_9)
    result13_9 = []
