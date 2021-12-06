# 工号生成方式
class JobNumber:
    def __init__(self):
        self.a = 1

    # 20170101~20221231
    def jobNumber1(self):
        result = []
        for a in range(2017, 2023):
            for b in range(1, 13):
                for c in range(1, 32):
                    result.append(str(a) + str(b).zfill(2) + str(c).zfill(2))
        return result
