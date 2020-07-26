import os

count = 1

files = os.listdir()
with open(str("总目录带序号.txt"), 'w') as fout:
    for file in files:
        if file == "生成序号.py" and "带序号总目录.txt"and"总目录.txt" and "带序号":
            continue
            # with open(str("带序号") + str(file), 'w') as fout:
            #     count = 1
            #     for line in open(file).readlines():
            #         fout.writelines(str(count) + "：" + str(line))
            #         count = count + 1
        print(file)
        for line in open(file).readlines():
            fout.writelines(str(count) + "：" + str(line))
            # fout.writelines(line)
            count = count + 1
