class Sort():
    def __init__(self):
        pass
    def Selection(self, list):
        i = 0
        j = 1
        r = len(list)
        list_of_lists = []
        while (i<r):
            j = i+1
            while(j<r):
                if (list[j] < list[i]):
                    list[i], list[j] = list[j], list[i]
                    list_of_lists.append(str(list))
                j+=1
            i+=1
        return list_of_lists

    def Merge(self, list, lol):
        if len(list)==1:
            return list, lol
        list1, list2, i = [], [], 0
        while (i<len(list)//2):
             list1.append(list[i])
             i+=1
        while (i<len(list)):
             list2.append(list[i])
             i+=1
        #lol[n[m]] = str(list2)
        lol.append(str(list1))
        a, lol = self.Merge(list1, lol)
        lol.append(str(list2))
        b, lol = self.Merge(list2, lol)
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
        #lol[n[m]] = str(c)
        lol.append(str(c))
        return c, lol

class Data(Sort):
    def Selection2(self, list):
        return self.Selection(list)
    def Merge2(self, list, lol):
        return self.Merge(list, lol)

class Vision(Data):
    def Selection1(self, list):
        print(list)
        list_of_lists = self.Selection2(list)
        for i in range(0, len(list_of_lists)):
            print(list_of_lists[i])
    def Merge1(self, list):
        print(list)
        lol = []
        list, lol = self.Merge2(list, lol)
        for i in range(0, len(lol)):
            print(lol[i])
list = [9, 5, 6, 9, 8, 4, 4]
#list = [9, 5, 4, 3]

#Vision().Selection1(list)
Vision().Merge1(list)
