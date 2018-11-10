# 该代码适用于分析cif晶体数据库文件，并且从中获得配合物的信息（仍在开发中）
# 定义原子类
class Atom:
    def __init__(self,name,state):
        self.isValid = False
        self.names = ('H','He',"Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc",
                      'Ti',"V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","La",
                      "Ce",'Pr',"Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",'Lu',"Nb","Mo","Tc","Ru","Rh",
                      "Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
                      "Tl","Pb","Bi","Po","At","Rn","Fr","Ba","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es",
                      "Fm","Md","No","Lr","Rg","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"
                      )
        self.transit = ("Sc", 'Ti',"V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Y","Zr","La",
                        "Ce",'Pr',"Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",
                        'Lu',"Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","Hf","Ta","W","Re",
                        "Os","Ir","Pt","Au","Hg","Ac","Th","Pa","U","Np","Pu","Am","Cm",
                        "Bk","Cf","Es","Fm","Md","No","Lr")
        self.name = self.checkName(name)
        self.state = state
        self.connection = []
        self.complex_number = len(self.connection)

    # 定义计算化合价类
    def calcState(self):
        print('The function si not yet complete')

    # 定义元素名称检查函数
    def checkName(self, name):
        while not self.isValid:
            for n in self.names:
                if n == name:
                    self.isValid = True
        return name

    def isTransit(self):
        if self.name in self.transit:
            return True

    def isLigand(self, a, b):
        if self.name == a:
            return b
        if self.name == b:
            return a


# 定义化学键类
class Bond:
    def __init__(self, atom_1, atom_2, length, type):
        self.atoms = [atom_1, atom_2]
        self.length = length
        self.type = type
        self.name = atom_1 + atom_2 + ' bond'


# 定义配合物类
class Complex:

    def __init__(self, name, center_atom):
        self.name = name
        self.center_atom = center_atom

    # 定义切片函数，搜索特定范围内的内容，返回一个切片
    def findContent(self, ls, ini_num, fnl_num, content):
        need = []
        for numd in ls[ini_num:fnl_num]:
            if content in numd:
                need.append(numd.strip())
        return need

    # 定义索引确定函数，搜索特定起始、终止条件，返回起始、终止索引
    def findIndex(self, ls, ini_cont, fnl_cont):
        ini_num, fnl_num = 0, 0
        for thing in ls:
            if thing.strip() == ini_cont:
                ini_num = ls.index(thing)
            if thing == fnl_cont:
                fnl_num = ls.index(thing)
        return ini_num, fnl_num


# 定义配体类
class Ligand:
    def __init__(self, name):
        self.name = name

    def checkOrganic(self):
        # 判定该配体是否为有机物
        pass

    def checkAtom(self):
        # 寻找配位原子
        pass


def startInput():
    print('Witch Work Studios',end='\n')
    print('Crystal Information File Checking System',end='\n')
    print('beta V0.0.1',end='\n')
    print('#'*70)
    isCorrect = False
    while not isCorrect:
        try:
            global file
            file = input('Enter the file name of the CIF data.\n')
            global savedir
            savedir = input('Where you want to save these data?')
            with open(file) as f_obj:
                print('Loading......')
                nums = f_obj.read().split()
                print('The file is successfully loaded.', end='\n')
                print("There are "+str(len(nums))+" words in the cif file.",end='\n')
                isCorrect = True
        except FileNotFoundError:
            print("The file doesn't exist!", end='\n')
    while isCorrect:
            atom_name = input('Enter the Atom Sign of the file\n(In English Letter with standard expressions)\n')
            atom_state = input('Enter the Highest Atom State of the file\n')
            global atom1
            atom1 = Atom(atom_name, atom_state)
            if atom1.isValid:
                isCorrect = False
                print('Element Info added successfully!', end='\n')
            else:
                print('Invalid Element Info!', end='\n')

def deNumber(chars):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    end_n = 0
    for char in chars:
        for num in numbers:
            if char == num:
                end_n = chars.index(num)
                break
        break
    result = chars[:(end_n -1)]
    return result


# 主函数程序
# 初始化、获得基本信息
startInput()
# 初始化完毕后进行数据处理
print('Opening File and Processing......')
# 打开文件
with open(file) as f_obj:
    global complexes
    complexes = []
    lines = f_obj.readlines()
    total = len(lines)
    print('There are '+str(total)+' lines in the file')
    # 搜索特定内容
    i = 0
    for line in lines:
        # 寻找初始分节点：
        if line[0:5] == 'data_':
            j = 0
            num_f = 0
            # 寻找初始分节结束点：
            for line2 in lines[i + 1:]:
                if line[0:5] == 'data_':
                    num_f = i + j
                j += 1
            # 处理该节数据
            ligandls = []
            line_new = line[5:].strip()
            complexes.append(line_new)
            names = locals()
            current_complex = Complex(line_new, atom1.name)
            # 查找配位原子
            ini0, fnl0 = current_complex.findIndex(lines[i+1:num_f], '_geom_bond_atom_site_label_1', '\n')
            ini = ini0 + 1 + i
            fnl = fnl0 + 1 + i
            atoms_need = current_complex.findContent(lines, ini, fnl, atom1.name)
            for atom in atoms_need:
                sequence = atom.split()
                ligandls.append(atom1.isLigand(sequence[0], sequence[1]))
            atom1.connection.append(ligandls)
            # 八隅律统计配位结构化合价

        i += 1
        ratio = i/total*100
        print('\r'+'Searching the '+str(i)+'th line. '+str('%.1f' % ratio)+'%', end='', flush=True)
print('\nProcess Complete!', end='\n')
print('There are '+str(len(complexes))+' complex in the file.', end='\n')
for thing in complexes:
    print('Complex Name: ' + thing, end='\n')
    indexNum = complexes.index(thing)
    lists = atom1.connection[indexNum]
    print('This complex have ' + str(len(lists)) + ' coordinating atoms.', end='\n')
    print('And respectively they are: ', end='\n')
    for num in lists:
        print(deNumber(num), end='\n')
print(atom1.connection)
