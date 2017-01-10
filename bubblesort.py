a = [4,3,12,54,1,2,9,5,7]
print a
for i in range(len(a)-1, 0,-1):
        print ' nilai i', i
        for j in range(i):
            print 'nilai j', j
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
print a