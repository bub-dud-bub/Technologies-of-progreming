class Sort():
    def Selection(list):
        i = 0
        j = 1
        r = len(list)
        while (i<r):
            j = i+1
            while(j<r):
                if (list[j] < list[i]):
                    list[i], list[j] = list[j], list[i]
                j+=1
            i+=1
        return list

    def Merge(list):
        if len(list)==1:
            return list[0]
        list1, list2, i = [], [], 0
        while (i<len(list)//2):
             list1.append(list[i])
             i+=1
        a = Sort.Merge(list1)
        while (i<len(list)):
             list2.append(list[i])
             i+=1
        b = Sort.Merge(list2)
        i, j = 0, 0
        c = [a[i]]
        while (i<(len(a)+len(b))):
            while(j<len(b)):
                if a[j]<c[i]:
                    c[i] = a[j]
                    a.remove(a[j])
                    j=0
                    break
                j+=1
            while(j<len(b)):
                if b[j]<c[i]:
                    c[i] = b[j]
                    b.remove(b[j])
                    break
                j+=1
        return c
list = [9, 5, 6, 9, 8, 4, 4]
a = Sort.Merge(list)
print(a)
