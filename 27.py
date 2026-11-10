
'''
데코레이터 (Decorator)

    오늘 배운 내용

이번에는 파이썬에서 함수의 기능을 확장할 수 있는
데코레이터(Decorator)에 대해 배웠다.

데코레이터는 기존 함수의 코드를 직접 수정하지 않고
새로운 기능을 추가할 수 있도록 도와준다.

함수를 매개변수로 전달하는 방법과
@ 기호를 사용해 데코레이터를 적용하는 방법을 학습했다.

    정의

1) 데코레이터(Decorator)

데코레이터는 다른 함수를 매개변수로 전달받아
기존 함수의 기능을 확장하거나 변경하는 함수이다.

2) 함수의 매개변수 전달

파이썬에서는 함수를 다른 함수의 매개변수로 전달할 수 있다.
이를 활용하면 함수의 실행 전후에 새로운 기능을 추가할 수 있다.

3) @ 기호

@ 기호는 데코레이터를 함수에 적용할 때 사용한다.
데코레이터를 적용하면 해당 함수가 데코레이터를 통해 실행된다.

    사용 방법

1) 기본적인 데코레이터 만들기

def decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")

    return wrapper

@decorator
def hello():
    print("안녕하세요!")

hello()

실행 결과
함수 실행 전
안녕하세요!
함수 실행 후

2) @ 기호 없이 데코레이터 사용하기

def decorator(func):
    def wrapper():
        print("실행 전")
        func()
        print("실행 후")

    return wrapper

def hello():
    print("안녕하세요!")

hello = decorator(hello)
hello()

실행 결과
실행 전
안녕하세요!
실행 후

3) 매개변수가 있는 함수에 데코레이터 사용하기

def decorator(func):
    def wrapper(name):
        print("이름을 출력합니다.")
        func(name)

    return wrapper

@decorator
def hello(name):
    print(name + "님 안녕하세요!")

hello("철수")

실행 결과
이름을 출력합니다.
철수님 안녕하세요!

4) 여러 매개변수를 처리하는 데코레이터

def decorator(func):
    def wrapper(*args, **kwargs):
        print("함수를 실행합니다.")
        result = func(*args, **kwargs)
        print("함수 실행이 끝났습니다.")
        return result

    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(10, 20))

실행 결과
함수를 실행합니다.
함수 실행이 끝났습니다.
30

    코드 분석

1) decorator(func)

데코레이터는 꾸며 줄 함수 자체를 매개변수로 전달받는다.

2) wrapper()

기존 함수의 실행 전후에 추가할 기능을 작성하는 내부 함수이다.

3) func()

전달받은 기존 함수를 실행한다.

4) return wrapper

새롭게 만든 wrapper 함수를 반환한다.
이후 데코레이터가 적용된 함수는 wrapper를 통해 실행된다.

5) *args와 **kwargs

*args는 여러 개의 위치 인자를 전달받고,
**kwargs는 여러 개의 키워드 인자를 전달받는다.

따라서 다양한 매개변수를 가진 함수에도
같은 데코레이터를 사용할 수 있다.

    복습하면서 알게 된 점

데코레이터는 기존 함수의 코드를 직접 수정하지 않고도
실행 전후에 새로운 기능을 추가할 수 있다는 것을 알게 되었다.

또한 함수를 다른 함수에 전달할 수 있다는 점과
내부 함수를 만들어 기존 함수의 실행을 감싸는 구조가 중요하다는 것을 이해했다.

📌 AI 활용 복습 문제

1) 데코레이터란 무엇인가?

정답: 기존 함수의 코드를 직접 수정하지 않고
새로운 기능을 추가하거나 확장하는 기능이다.

2) 데코레이터를 적용할 때 사용하는 기호는?

정답: @

3) 데코레이터 내부에서 기존 함수를 실행하는 부분은?

정답: func()

4) wrapper 함수의 역할은?

정답: 기존 함수의 실행 전후에 추가 기능을 수행하고
기존 함수를 실행하는 역할을 한다.

5) *args와 **kwargs를 사용하는 이유는?

정답: 다양한 개수와 형태의 매개변수를 전달받기 위해 사용한다.

6) @decorator를 사용하지 않고 데코레이터를 적용하는 방법은?

정답:
hello = decorator(hello)
'''
