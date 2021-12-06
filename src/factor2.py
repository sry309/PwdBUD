# 2因素密码生成
# 密码仅由两个因素构成，如：字母+数字组合。
# 这里的因素特指几段不同的序列，如字母为一因素，数字为一因素，特殊符号为一因素。
# 大写不作为单独的因素添加。
import src.jobnumber as jn


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
        with open('.\\dict\\top1000.txt') as f:
            birth = f.readlines()

        for i in range(len(domian)):
            domianList1 = list(str(self.domaim))
            domianList1[i] = str(domianList1[i]).upper()
            domainStr1 = "".join(domianList1)
            for x in birth:
                x = x.replace("\n","")
                result.append(domainStr1 + x)
        #upper(),lower
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
        with open('.\\dict\\birth.txt') as f:
            birth = f.readlines()

        for i in range(len(domian)):
            domianList1 = list(str(self.domaim))
            domianList1[i] = str(domianList1[i]).upper()
            domainStr1 = "".join(domianList1)
            for x in birth:
                x = x.replace("\n","")
                result.append(domainStr1 + x)
        #upper(),lower
        for x in birth:
            x = x.replace("\n", "")
            result.append(domian.upper() + x)
        for x in birth:
            x = x.replace("\n", "")
            result.append(domian.lower() + x)
        return result
