# 若需要改变输入的光谱值，请将前两行代码和第6、7行代码解注释，并注释掉第3、4行
#charin = input('Please input the spectroscopy data\n').split()
#floatout = []
floatout = [312.9, 315.4, 316.6, 324.2, 340.6, 344.3, 344.9, 346.1, 346.7, 348.6, 351.1, 352.2, 357.7, 360.1, 361.2,
            362.3, 371.5, 373, 386.3, 416.9, 426.2, 427.3, 429.4]
#for char in charin:
#    floatout.append(float(char.strip()))

metals = {"V": [306.64, 309.31, 318.40, 318.54, 327.11, 437.92, 438.47, 439],
          "Cr": [357.87, 359.35, 360.53, 361.56, 425.44, 427.48, 428.97, 520.45],
          "Mn": [257.61, 259.37, 279.48, 279.83, 403.08, 403.31, 403.45],
          "Fe": [344.06, 368.12, 372.00, 373.49, 385.99],
          "Ni": [341.48, 344.63, 345.85, 346.17, 349.30, 351.51, 352.45, 361.94]}
result = {"V": 0, "Cr": 0, "Mn": 0, "Fe": 0, "Ni": 0}
print('Analyzing spectroscopy data......')
errors = [0.2, 0.8, 1.4, 2, 3.5, 6, 10]
# 打印表头
for metal in metals:
    print(metal, end='\t'*2)
print('\n', end='')
# 遍历所有误差
for error in errors:
    # 遍历光谱的每一条谱线
    for spectra in floatout:
        # 对于该谱线对每一个金属的标准光谱进行遍历
        for metal, ls in metals.items():
            # 对金属的每一条特征谱线进行遍历
            for key in ls:
                # 当误差小于标准误差时储存结果
                if abs(key - spectra) <= error:
                    accuracy = (spectra - key)/spectra
                    #result[metal] += round((1-abs(accuracy)), 4)
                    result[metal] += 1
                    break
    # 输出结果
    for metal in result:
        print(result[metal], end='\t'*2)
        result[metal] = 0
    print('', end='\n')
