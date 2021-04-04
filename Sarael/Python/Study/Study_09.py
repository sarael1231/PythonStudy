class Study_09_Package :
    def Study1002(self) :
        # 문제
        # 조규현과 백승환은 터렛에 근무하는 직원이다. 
        # 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 
        # 다음은 조규현과 백승환의 사진이다.
        # 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 
        # 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
        # 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
        # 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
        # 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

        # 입력
        # 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
        # 각 테스트 케이스는 다음과 같이 이루어져 있다.
        # 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. 
        # x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, 
        # r1, r2는 10,000보다 작거나 같은 자연수이다.

        # 출력
        # 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 
        # 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

        import math

        x1, y1, r1, x2, y2, r2 = map(int, input("숫자 입력하세요 : ").split())
        
        dist = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

        min_r = min(r1, r2)
        max_r = max(r1, r2)

        if dist == 0 :
            if min_r == max_r :
                print("-1")
            else :
                print("0")
        else :
            if min_r + max_r == dist :
                print("1")
            elif (max_r - min_r < dist) & (max_r + min_r > dist) :
                print("2")
            else :
                print("0")

    def Study1085(self) :
        # 문제
        # 한수는 지금 (x, y)에 있다. 
        # 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고, 오른쪽 위 꼭짓점은 (w, h)에 있다. 
        # 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

        # 입력
        # 첫째 줄에 x, y, w, h가 주어진다.

        # 제한
        # 1 ≤ w, h ≤ 1,000
        # 1 ≤ x ≤ w-1
        # 1 ≤ y ≤ h-1
        # x, y, w, h는 정수

        x, y, w, h = map(int, input("숫자 입력하세요 : ").split())

        print(min(x, y, h-y, w-x))

    def Study1978(self) :
        # 문제
        # 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

        # 입력
        # 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 
        # 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

        data = [int(i) for i in input().split()]

        max_num = max(data)
        decimal = self.__GetDecimalList(max_num)
        
        count = 0
        for i in data :
            if i in decimal :
                count += 1

        print(count)

    def __GetDecimalList(self, max_num) :
        numbers = list(range(2, max_num+1))
        decimal = []

        for i in numbers :
            if i == 2 :
                decimal.append(i)
            else :
                is_decimal = True
                for j in decimal :
                    if i % j == 0 :
                        is_decimal = False
                        break;

                if is_decimal :
                    decimal.append(i)

        decimal.insert(0, 1)

        return decimal

    def Study2581(self) :
        # 문제
        # 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 
        # 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
        # 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 
        # 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 
        # 이들 소수의 합은 620이고, 최솟값은 61이 된다.

        # 입력
        # 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
        # M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

        start, end = map(int, input("숫자 입력하세요 : ").split())

        decimal = self.__GetDecimalList(end)
        
        sum = 0
        first_decimal = -1
        for i in range(start, end + 1) :
            if i in decimal :
                sum += i
                if first_decimal == -1 :
                    first_decimal = i

        print(sum)
        print(first_decimal)