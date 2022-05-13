import calendar
import math
import sys
from calendar import calendar
from fractions import Fraction


def bai1():
    s = float(input("Nhap vao dien tich S: "))
    r = math.sqrt(s / (4 * math.pi))
    v = (4 / 3) * math.pi * pow(r, 3)
    print("The tich la: ", v)


# bai1()


def bai2():
    # print("Nhap toa do diem A")
    # xA = float(input("xA = "))
    # yA = float(input("yA = "))
    # print("Nhap toa do diem B")
    # xB = float(input("xB = "))
    # yB = float(input("yB = "))
    xA, yA = [float(x) for x in input("A(xA, yA)? ").split()]
    xB, yB = [float(x) for x in input("A(xB, yB)? ").split()]
    AB = math.sqrt((pow((xB - xA), 2) + pow((yB - yA), 2)))
    print("|AB| = ", AB)


# bai2()


def bai3():
    xC, yC = [float(x) for x in input("Nhap toa do tam giac C(xC, yC)? ").split()]
    R = float(input("Nhap ban kinh R? "))
    xM, yM = [float(x) for x in input("Nhap toa do M(xM, yM)? ").split()]
    d = math.sqrt((pow((xM - xC), 2) + pow((yM - yC), 2)))
    if d < R:
        print("M nam trong C()")
    elif d == R:
        print("M nam tren C()")
    else:
        print("M nam ngoai C()")


# bai3()


def bai4():
    a, b, c = [float(x) for x in input("Nhap vao 3 canh tam giac: ").split()]
    if (a + b) < c and (a + c) < b and (b + c) < a:
        print("Tam giac khong hop le!")
    else:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        if a * a + b * b == c * c or a * c + c * c == b * b or b * b + c * c == a * c:
            print("Tam giac vuong!")
        elif a == b or a == c or b == c:
            print("Tam giac can!")
        else:
            print("Tam giac thuong!")
        print("Dien tich S = ", s)


# bai4()


def bai5():
    xA, yA = [float(x) for x in input("A(xA, yA)? ").split()]
    xB, yB = [float(x) for x in input("B(xB, yB)? ").split()]
    xC, yC = [float(x) for x in input("C(xC, yC)? ").split()]
    xM, yM = [float(x) for x in input("M(xM, yM)? ").split()]
    Smab = abs(xM * yA - xA * yM + xA * yB - xB * yA + xB * yM - xM * yB) / 2
    Smbc = abs(xM * yB - xB * yM + xB * yC - xC * yB + xC * yM - xM * yC) / 2
    Smca = abs(xM * yC - xC * yM + xC * yA - xA * yC + xA * yM - xM * yA) / 2
    Sabc = abs(xA * yB - xB * yA + xB * yC - xC * yB + xC * yA - xA * yC) / 2
    S = Smbc + Smca + Smab
    if S < Sabc:
        print("M nam trong tam giac ABC!")
    elif S == Sabc:
        print("M nam tren canh tam giac ABC!")
    else:
        print("M nam ngoai tam giac ABC!")


# bai5()


def bai6():
    a, b, c = [int(x) for x in input("Nhap a, b, c: ").split()]

    # def swap(a, b):
    #     tmp = a
    #     a = b
    #     b = tmp
    if a > b:
        tmp = a
        a = b
        b = tmp
    if a > c:
        tmp = a
        a = c
        c = tmp
    if b > c:
        tmp = b
        b = c
        c = tmp
    print("Tang dan: ", a, b, c)


# bai6()


def bai7():
    a, b = [float(x) for x in input("Nhap a, b: ").split()]
    if a != 0:
        print("x = ", -b / a)
    elif a == 0 and b == 0:
        print("Phuong trinh co vo so nghiem!")
    elif a == 0 and b != 0:
        print("Phuong trinh vo nghiem!")


# bai7()


def bai8():
    a, b, c = [float(x) for x in input("Nhap a, b, c: ").split()]
    d = b * b - 4 * a * c
    if d < 0:
        print("Phuong trinh vo nghiem!")
    elif d == 0:
        print("x = ", -b / (2 * a))
    else:
        print("x1 = ", (-b - math.sqrt(d)) / (2 * a))
        print("x2 = ", (-b + math.sqrt(d)) / (2 * a))


# bai8()


def bai9():
    x = int(input("Nhap so do x cua goc (phut): "))
    d = x / 60
    r = d * (math.pi / 180)
    if 0 < d < 90:
        print("x thuoc goc vuong thu nhat!")
    elif 90 < d < 180:
        print("x thuoc goc vuong thu hai!")
    elif 180 < d < 270:
        print("x thuoc goc vuong thu ba!")
    elif 270 < d < 360:
        print("x thuoc goc vuong thu tu!")
    print("cos(x) = ", math.cos(r))
    pass


# bai9()


def bai10():
    while True:
        sin = input("SIN (0 de thoat): ")
        if sin == "0":
            break
        if len(sin) != 9:
            print("SIN khong hop le!")
            continue
        s1 = 0
        s2 = 0
        s = ''
        for i in range(0, len(sin) - 1):
            if i % 2 == 0:
                s1 = s1 + int(sin[i])
            else:
                s = s + str(int(sin[i]) * 2)
        for i in s:
            s2 = s2 + int(i)
        if (s1 + s2 + int(sin[-1])) % 10 == 0:
            # print(s1)
            # print(s2)
            # print(sin[-1])
            # print(s1 + s2 + int(sin[-1]))
            print("SIN hợp lệ !")
        else:
            print('SIN không hơp lệ !')


# bai10()

import random


def bai11():
    tiSoNguoi = 0
    tiSoMay = 0
    while True:
        list = ["b", "d", "k"]
        x = input("Nhap ky tu (b-d-k), ky tu khac de thoat: ")
        y = random.choice(list)
        print('Computer: ', y)

        if x == "b":
            if y == "b":
                pass
            elif y == 'd':
                tiSoNguoi = tiSoNguoi + 1
            elif y == 'k':
                tiSoMay = tiSoMay + 1
        elif x == 'd':
            if y == 'b':
                tiSoMay = tiSoMay + 1
            elif y == 'k':
                tiSoNguoi = tiSoNguoi + 1
        elif x == 'k':
            if y == 'b':
                tiSoNguoi = tiSoNguoi + 1
            elif y == 'd':
                tiSoMay = tiSoMay + 1
        else:
            break

        print('Ty so human - computer: ', tiSoNguoi, '-', tiSoMay)


# bai11()

def bai12():
    a1, b1, c1 = [int(x) for x in input('Nhap a1, b1, c1: ').split()]
    a2, b2, c2 = [int(x) for x in input('Nhap a2, b2, c2: ').split()]

    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    if D == 0:
        if Dx + Dy == 0:
            print('He phuong trinh vo so nghiem!')
        else:
            print('He phuong trinh vo nghiem!')
    else:
        x = int(Dx / D)
        y = int(Dy / D)
        print('x = ', x)
        print('y = ', y)


# bai12()

def bai13():
    # day, month, year = [int(x) for x in input('Nhap ngay, thang va nam: ').split()]
    # if year < 1582:
    #     sys.exit('Lich bat dau tu nam 1582')
    # if month < 0 or month > 12:
    #     sys.exit('Thang khong hop le')
    # dayOfMonth = 0
    # if month == 4 or month == 6 or month == 9 or month == 11:
    #     dayOfMonth = 30
    # elif month == 2:
    #     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    #         dayOfMonth = 29
    #     else:
    #         dayOfMonth = 28
    # else:
    #     dayOfMonth = 31

    # if day < dayOfMonth or day > dayOfMonth:
    #     sys.exit('Ngay khong hop le')
    # def week(i):
    #     switcher={
    #             0:'Chu nhat',
    #             1:'Thu hai',
    #             2:'Thu ba',
    #             3:'Thu tu',
    #             4:'Thu nam',
    #             5:'Thu sau',
    #             6:'Thu bay'
    #          }
    #     return switcher.get(i,"Invalid day of week")

    # d = (14 - month) // 12
    # y = year - d
    # m = month + 12 * d - 2
    # dayOfWeek = (day + y + y//4 - y//100 + y//400 + (31 * m)//12) % 7
    # # print((d + y + y//4 - y//100 + y//400 + (31 * m)//12))
    # # print(dayOfWeek)
    # print(week(dayOfWeek))
    # pass
    # day = int(input("Nhap ngay: "))
    # month = int(input("Nhap thang: "))
    # year = int(input("Nhap nam: "))
    day, month, year = [int(x) for x in input('Nhap ngay, thang va nam: ').split()]
    if year < 1582:
        sys.exit("Lich bat dau tu nam 1582")
    if month < 1 or month > 12:
        sys.exit("Thang khong hop le")
    maxDay = 0
    if month == 4 or month == 6 or month == 9 or month == 11:
        maxDay = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            maxDay = 29
        else:
            maxDay = 28
    else:
        maxDay = 31
    if day < 1 or day > maxDay:
        sys.exit("Ngay khong hop le")
    print("Hop le")

    a = (14 - month) // 12
    y1 = year - a
    m1 = month + 12 * a - 2
    dayofweek = (day + y1 + y1 // 4 - y1 // 100 + y1 // 400 + (31 * m1) // 12) % 7
    if (dayofweek == 0):
        print("Chu nhat")
    else:
        print("Thu", dayofweek + 1)


# bai13()

def bai14():
    day, month, year = [int(x) for x in input('Nhap ngay, thang va nam: ').split()]
    maxDay = 0
    if month == 4 or month == 6 or month == 9 or month == 11:
        maxDay = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            maxDay = 29
        else:
            maxDay = 28
    else:
        maxDay = 31

    # if day < maxDay:
    #     day += 1
    # else:
    #     day = 1
    #     month += 1
    # if day == 31 and month == 12:
    #     day = 1
    #     month = 1
    #     year += 1
    # print('Ngay mai: ', day, '/', month, '/', year)

    nDay = day % maxDay + 1
    nMonth = month
    nYear = year
    if nDay == 1:
        nMonth = month % 12 + 1
        if nMonth == 1:
            nYear += 1
    print('Ngay mai:', nDay, '/', nMonth, '/', nYear)
    Month = month
    month -= 1
    if day == 1:
        yDay = maxDay
        if Month == 1:
            yMonth = 12
            yYear = year - 1
        else:
            yMonth = month - 1
            yYear = year
    else:
        yDay = day - 1
        yMonth = Month
        yYear = year
    print('Hom qua:', yDay, '/', yMonth, '/', yYear)
    # pass


# bai14()

def bai15():
    day, month, year = [int(x) for x in input('Nhap ngay, thang va nam: ').split()]
    sum = (int)(30.42 * (month - 1)) + day
    if month == 2 or (((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) and month > 2):
        sum += 1
    if 2 < month < 8:
        sum -= 1
    print('Ngay thu:', sum)


# bai15()

def Bai16():
    c = calendar.TextCalendar(calendar.MONDAY)
    y = int(input('Nhap nam: '))
    for i in range(1, 13):
        str = c.formatmonth(y, i)
        print(str)
    # pass


# Bai16()

def bai17():
    pass


def Bai18():
    h = int(input('Nhap so gio: '))
    w = h // 168
    h %= w * 168
    d = h // 24
    hour = h % (d * 24)
    print(w, 'tuan', d, 'ngay', hour, 'gio')


# Bai18()

def Bai19():
    h1, m1, s1 = [int(x) for x in input('Nhap gio, phut, giay: ').split()]
    h2, m2, s2 = [int(x) for x in input('Nhap gio, phut, giay: ').split()]
    s = (s2 - s1) % 60
    m = (m2 - m1) % 60
    h = (h2 - h1)
    if s2 < s1:
        m -= 1
    if m2 < m1:
        h -= 1
    print('Hieu thoi gian:', h, 'gio', m, 'phut', s, 'giay')


# Bai19()

def Bai20():
    x = int(input('Nhap so kW tieu thu: '))
    c1 = c2 = c3 = c4 = 0
    if 0 < x <= 100:
        c = 500 * x
    elif 100 < x <= 250:
        c = 50000 + (x - 100) * 800
    elif x <= 350:
        c = 170000 + (x - 250) * 1000
    else:
        c = 270000 + (x - 350) * 1500
    print('Chi phi:', c)


# Bai20()

def Bai21():
    diemChuan = float(input('Nhap diem chuan: '))
    mon1, mon2, mon3 = [float(x) for x in input("Nhap diem 3 mon thi: ").split()]
    khuVuc = input('Nhap khu vuc (A, B, C, X):')
    doiTuong = int(input('Nhap doi tuong (1, 2, 3, 0): '))
    diemUT = 0
    if khuVuc == "A":
        diemUT += 2
    elif khuVuc == "B":
        diemUT += 1
    elif khuVuc == "C":
        diemUT += 0.5

    if doiTuong == 1:
        diemUT += 2.5
    elif doiTuong == 2:
        diemUT += 1.5
    elif doiTuong == 3:
        diemUT += 1

    tongDiem = mon1 + mon2 + mon3 + diemUT
    if tongDiem >= diemChuan:
        print('Do', [tongDiem])
    else:
        print('Rot', [tongDiem])


# Bai21()

def Bai22():
    n = int(input('Nhap n: '))
    s = 0
    c = 0
    print('Cac uoc so: ', end='')
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')
            s += i
            c += 1
    print('')
    print('Co', c, 'uoc so, tong la:', s)


# Bai22()

def Bai23():
    def per_NUM(n):
        s = 0
        for i in range(1, int(n / 2 + 1)):
            if n % i == 0:
                s += i
        if s == n:
            return True
        else:
            return False

    n = int(input('Nhap n: '))
    print('Cac so hoan hao nho hon', n, ': ', end=' ')
    for i in range(1, n):
        if per_NUM(i):
            print(i, end=' ')


# Bai23()

def Bai24():
    n = input('Nhap n:')
    print(n, 'co', len(n), 'chu so')
    print('Chu so cuoi cung la: ', n[len(n) - 1])
    print('Chu so dau tien la: ', n[0])
    n = int(n)
    s = 0
    s1 = 0
    while n > 0:
        s += n % 10
        s1 = s1 * 10 + (n % 10)
        n //= 10
    print('Tong cac chu so là: ', s)
    print('So dao nguoc la: ', s1)


# Bai24()

def Bai25():
    a, b = [int(x) for x in input('Nhap cap (a, b): ').split()]
    print('USCLN (a, b): ', math.gcd(a, b))
    print('BSCNN (a, b): ', math.lcm(a, b))


# Bai25()

def Bai26():
    tu, mau = [int(x) for x in input('Nhap tu so, mau so: ').split()]
    ps = Fraction(tu, mau)
    # print(math.gcd(tu, mau))
    # tu = int(tu / math.gcd(tu, mau))
    # mau = int(mau / math.gcd(tu, mau))
    # print(tu, '/', mau)
    print(ps)


# Bai26()

def Bai27():
    n = int(input('Nhap n: '))
    for i in range(2, n + 1):
        if n % i == 0:
            print(i, end=' * ')
        while n % i == 0:
            n //= i


# Bai27()

def Bai28():
    n = float(input('Nhap so thuc n: '))
    e = int(input('Do chinh xac: '))
    print(round(n, e))


# Bai28()

def Bai29():
    print('Celsius\tFahrenheit\tFahrenheit\tCelsius')
    for i in range(11):
        print(i, '\t', round(9 * i / 5 + 32, 2), '\t\t', i + 32, '\t\t', round(5 * i / 9, 2))


# Bai29()

def Bai30():
    r, p, n = [float(x) for x in input('Nhap lai suat, tien von, thoi han: ').split(',')]
    print('Lai suat: ', r * 100, '%')
    print('Von ban dau: ', p)
    print('Thoi han: ', n, 'nam')
    n = int(n)
    for i in range(1, n + 1):
        a = (p * (1 + r) ** i)
        print(i, '\t', round(a, 1))


# Bai30()

def Bai31():
    print("Bang cuu chuong")
    for i in range(1, 11):
        print("|", end=' ')
        for j in range(2, 10):
            print(j, "x", i, "=", j * i, sep='', end='|')
        print("\n")
    pass


# Bai31()

def Bai32():
    while True:
        n = int(input('Nhap n: '))
        d = 0
        while True:
            print(n, end='\t')
            if n == 1 and d > 0:
                d += 1
                break
            if n % 2 != 0:
                n = 3 * n + 1
            else:
                n = n // 2
            d += 1
            if d % 6 == 0:
                print('')
        print('\nHailstones sinh duoc: ', d)
        while True:
            x = input('Tiep (y/n)? ')
            if x == 'y' or x == 'n':
                break
            else:
                print('NHap sai hay nhap lai!')
        if x == 'y':
            continue
        elif x == 'n':
            break


# Bai32()

def Bai33():
    def arm(n, i):
        s = 0
        n1 = n
        while n1 > 0:
            s += (n1 % 10) ** i
            n1 //= 10
        if s == n:
            return True
        else:
            return False

    print('So Armstrong co 3, 4 chu so:')
    for i in range(100, 10000):
        if (i < 1000):
            if arm(i, 3):
                print(i, end=' ')
        else:
            if arm(i, 4):
                print(i, end=' ')


# Bai33()

def Bai34():
    pass


def Bai35():
    def isPrime(x):
        d = 0
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                d += 1
                break
        if d == 0:
            return True
        else:
            return False

    n = int(input('Nhap n: '))
    if isPrime(n):
        print(n, 'la so nguyen to')
    else:
        while isPrime(n) == False and n > 1:
            n -= 1
        if n != 1:
            print('So nguyen to nho hon gan nhat:', n)


# Bai35()

def Bai36():
    def isPrime(x):
        d = 0
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                d += 1
                break
        if d == 0:
            return True
        else:
            return False

    n = int(input('Nhap n: '))
    i = 2
    d = 0
    while True:
        if isPrime(i):
            print(i, end=' ')
            d += 1
            if d == n:
                break
        i += 1


# Bai36()

def Bai37():
    n = int(input('Nhap n: '))
    s = 0
    m = 1
    a = []
    while s < n:
        s += m
        if s >= n:
            m -= 1
            break
        a.append(m)
        m += 1
    for i in a:
        if i == m:
            print(i, '=', sum(a), '<', n)
        else:
            print(i, end=' + ')
    print("m =", m)


# Bai37()

def Bai38():
    n = int(input("Nhap n: "))
    x = y = z = x1 = y1 = z1 = 0
    min = n
    for y in range(n // 2, 0, -1):
        for z in range(n // 5):
            x = n - (2 * y + 5 * z)
            if (y > (x + z)) and ((x + y + z)) < min and x >= 0:
                min = x + y + z
                x1 = x
                y1 = y
                z1 = z
    print('(', x1, ',', y1, ',', z1, '):', min)


# Bai38()

def Bai39():
    for x in range(1, 100):
        for y in range(x, 100):
            for z in range(y, 100):
                if x ** 2 + y ** 2 == z ** 2:
                    if y - x == 1 and z - y == 1:
                        print('(', x, ',', y, ',', z, '): 3 so nguyen lien tiep')
                    elif y % 2 == 0 and y - x == 2 and z - y == 2:
                        print("(", x, ",", y, ",", z, "): 3 so chan lien tiep")


# Bai39()

def Bai40():
    for x in range(1, 21):
        for y in range(100 // 3):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('(', x, ',', y, ',', z, ')')


Bai40()
