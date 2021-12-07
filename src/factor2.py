# 多因素密码生成
# 这里的因素特指不同的序列，如字母为一因素，数字为一因素，特殊符号为一因素。
# 大写不作为单独的因素添加。
import src.jobnumber as jn
from pathlib import Path


class Factor2:
    def __init__(self, domain):
        self.domaim = domain

    # Example: jd20210101,Jd20210101,jD20210101
    def sequence1(self):
        result = []
        domian = str(self.domaim)

        for i in range(len(domian)):
            domianList1 = list(str(self.domaim))
            domianList1[i] = str(domianList1[i]).upper()
            domainStr1 = "".join(domianList1)
            for x in jn.JobNumber().jobNumber1():
                result.append(domainStr1 + x)
        # upper(),lower
        for x in jn.JobNumber().jobNumber1():
            result.append(domian.upper() + x)
        for x in jn.JobNumber().jobNumber1():
            result.append(domian.lower() + x)

        return result

    # top1000弱口令
    # Example: jd123123，Jdadmin，jDadmin
    def sequence2(self):
        result = []
        domian = str(self.domaim)
        with open(Path("./dict/top1000.txt")) as f:
            birth = f.readlines()

        for i in range(len(domian)):
            domianList1 = list(str(self.domaim))
            domianList1[i] = str(domianList1[i]).upper()
            domainStr1 = "".join(domianList1)
            for x in birth:
                x = x.replace("\n", "")
                result.append(domainStr1 + x)
        # upper(),lower
        for x in birth:
            x = x.replace("\n", "")
            result.append(domian.upper() + x)
        for x in birth:
            x = x.replace("\n", "")
            result.append(domian.lower() + x)
        return result

    # birth弱口令
    # Example: jd19820101，Jd082507,jD0011986
    def sequence3(self):
        result = []
        domian = str(self.domaim)
        with open(Path("./dict/birth.txt")) as f:
            birth = f.readlines()

        for i in range(len(domian)):
            domianList1 = list(str(self.domaim))
            domianList1[i] = str(domianList1[i]).upper()
            domainStr1 = "".join(domianList1)
            for x in birth:
                x = x.replace("\n", "")
                result.append(domainStr1 + x)
        # upper(),lower
        for x in birth:
            x = x.replace("\n", "")
            result.append(domian.upper() + x)
        for x in birth:
            x = x.replace("\n", "")
            result.append(domian.lower() + x)
        return result

    ########################公司名######################################################
    # 公司名+年份
    # Example: Jingdong2019
    def sequence4(self):
        result = []
        year = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        domian = str(self.domaim)
        # domianList1 = list(str(self.domaim))
        for x in year:
            result.append(str(domian + x))
        for x in year:
            result.append(domian.capitalize() + x)
        return result

    # 公司名+特殊字符+年份
    # Example: Jingdong@2019
    def sequence5(self):
        result = []
        year = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        str1 = ['!', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "?", "<", ">", "."]
        domian = str(self.domaim)
        # domianList1 = list(str(self.domaim))
        for i in str1:
            for x in year:
                result.append(str(domian + i + x))
            for x in year:
                result.append(domian.capitalize() + i + x)
        return result

    # 公司名+特殊字符+top1000弱口令
    # Example: Jingdong@2019
    def sequence6(self):
        result = []
        with open(Path("./dict/top1000.txt")) as f:
            pwd = f.readlines()
        str1 = ['!', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "?", "<", ">", "."]
        domian = str(self.domaim)
        # domianList1 = list(str(self.domaim))
        for i in str1:
            for x in pwd:
                x = x.replace("\n", "")
                result.append(str(domian + i + x))
            for x in pwd:
                x = x.replace("\n", "")
                result.append(domian.capitalize() + i + x)
        return result

    # 公司名称+年份+特殊字字符
    # Example: Jingdong2021@
    def sequence7(self):
        result = []
        year = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        str1 = ['!', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "?", "<", ">", "."]
        domian = str(self.domaim)
        for i in str1:
            for x in year:
                result.append(str(domian + x + i))
            for x in year:
                result.append(domian.capitalize() + x + i)
        return result

    # 淦他娘，下面的代码生成的字典2G多
    # 常见姓名简拼全拼+top1000/生日日期
    # Example: zhangsan123123 zhangsan19840615
    # def sequence8(self):
    #     result = []
    #     with open(Path('./dict/cnname.txt')) as f:
    #         name = f.read().splitlines()
    #     with open(Path('./dict/topandbirth.txt')) as f:
    #         top = f.read().splitlines()
    #
    #     for n in name:
    #         for t in top:
    #             result.append(str(n + t))
    #     for n in name:
    #         for t in top:
    #             result.append(str(n.capitalize() + t))
    #     return result
