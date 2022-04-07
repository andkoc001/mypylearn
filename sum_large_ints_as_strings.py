str1 = '112314342545645757'
str2 = '131234455'

print('Check:', int(str1) + int(str2))
# print('Last digit:', (int(str1) % 10))


def add2str(s1, s2):

    res = 0
    carry_over = 0
    result = ''

    tmp1 = s1
    tmp2 = s2

    if len(s2) < len(s1):
        for k in range(len(s1)-len(s2)):
            tmp2 = "0" + tmp2

    print('str1: ', tmp1)
    print('str2: ', tmp2)

    for i in range(len(s1)):

        if carry_over == 0:

            last1 = tmp1[-1]
            tmp1 = tmp1[:-1]

            last2 = tmp2[-1]
            tmp2 = tmp2[:-1]

            if (int(last1) + int(last2)) < 10:
                res = int(last1) + int(last2)
                result = str(res) + str(result)
                # print('here!!!', result)

            else:
                res = (int(last1) + int(last2)) % 10
                carry_over = 1
                result = str(res) + str(result)

        elif carry_over == 1:

            last1 = tmp1[-1]
            tmp1 = tmp1[:-1]

            last2 = tmp2[-1]
            tmp2 = tmp2[:-1]

            if (last1 + last2) >= 10:
                res = last1 + last2 + 1
                result = str(res) + str(result)

            else:
                res = (last1 + last2) % 10
                carry_over = 1
                result = int(res) + 1 + int(result[1:])

        carry_over = 0

    return print("END:  ", result)


add2str(str1, str2)
