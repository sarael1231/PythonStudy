from random import *

def PythonIO() :
    print("파이썬 연산과 여러가지 출력 방식\n")

    i, j = map(int, input("숫자 두개를 입력하세요 : ").split())

    print(i, "+", j, "=", i+j)
    print("%d - %d = %d" % (i, j, i-j))
    print("{} * {} = {}".format(i, j, i*j))
    print("{0} / {1} = {2}".format(i, j, i/j))

    print("{num1} % {num2} = {num3}".format(num1=i, num2=j, num3=i%j))
    print(f"{i} // {j} =", i//j)

    print("abs(" + str(i) + ") = " + str(abs(i)))
    print("pow(" + str(i) + ", " + str(j) + ") = " + str(pow(i, j)))
    print("max(" + str(i) + ", " + str(j) + ") = " + str(min(i, j)))
    print("min(" + str(i) + ", " + str(j) + ") = " + str(max(i, j)))
    print("round(" + str(i) + ") = " + str(round(i)))

    print("줄바꿈 없이", end=" ")
    print("출력")

    print("Python", "Java", sep=" ,", end="?\n")

    # 좌 우 정렬 ljust, rjust(정렬 글자 수)
    # 숫자 자리수 0으로 채우기 zfill(숫자 자리 수)


def PythonRandom() :
    print("\nRandom")
    print(random())
    print(int(random() * 9) + 1) # 1 ~ 10
    print(randrange(1, 11)) # 1 ~ 10
    print(randint(1, 10)) # 1 ~ 10
    print(list(range(1, 21)))

def PythonOutputFormat() :
    # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
    print("{0: >10}".format(500))

    # 양수일 땐 +로 표시, 음수일 땐 -로 표시
    print("{0: >+10}".format(500))
    print("{0: >+10}".format(-500))
    # 왼쪽 정렬하고, 빈칸으로 _로 채움
    print("{0:_<10}".format(500))
    # 3자리마다 콤마를 찍어주기
    print("{0:,}".format(1000000000))
    # 부호도 붙이기
    print("{0:+,}".format(-1000000000))
    # 자릿수도 확보하고 빈자리는 ^ 로 채우기
    print("{0:^<+30,}".format(1000000000))
    # 소수점 출력
    print("{0:f}".format(5/3))
    # 소수점 2자리만 (소수점 3째 자리에서 반올림)
    print("{0:.2f}".format(5/3))
