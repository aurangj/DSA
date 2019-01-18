
p = [ 4,6,7,6]
d = [ 4,5,9,5]
length = len(p)
s = 0
e = 0
total_p = p[0]
i=0
while True:
    if total_p >= d[e]:
        total_p = total_p - d[e] + p[(e+1)% length]

        print((e+1)% length)

        e = (e + 1) % (length)
        if s == e:
            print 'path exists'
            break

        print (total_p, d[e])

    if total_p < d[e]:
        print('in less than')
        s = e + 1
        e = e + 1
        print(s,e)
        i = i + 1
        total_p = p[e]
        if i == len(p):
            print 'no path exists'
            break






