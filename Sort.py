class Sort():
    def __init__(self):
        pass
    def Selection(self, list):
        i = 0
        j = 1
        r = len(list)
        while (i<r):
            j = i+1
            while(j<r):
                if (list[j] < list[i]):
                    list[i], list[j] = list[j], list[i]
                    Data().data(list)
                j+=1
            i+=1
        return list

    def Merge(self, list):
        if len(list)==1:
            Data().data(list)
            return list
        list1, list2, i = [], [], 0
        while (i<len(list)//2):
             list1.append(list[i])
             i+=1
        a = self.Merge(list1)
        while (i<len(list)):
             list2.append(list[i])
             i+=1
        b = self.Merge(list2)
        i, c = 0, []
        while (i<(len(a)+len(b))):
            if (len(a)==0):
                c+=b
                break
            elif (len(b)==0):
                c+=a
                break
            if a[0]<=b[0]:
                c.append(a[0])
                a.remove(a[0])
            else:
                c.append(b[0])
                b.remove(b[0])
        Data().data(c)
        return c

class Data(Sort):
    def data(self, list):
        var = list
        return Vision().vision(var)

class Vision(Data):
    def vision(self, list):
        print(list)

list = [9, 5, 6, 9, 8, 4, 4]
#Sort().Selection(list)
Sort().Merge(list)
