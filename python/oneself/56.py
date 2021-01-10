# 혼자 공부하는 파이썬 56강 - 데코레이터, 상속, 최대값 최소값

# 데코레이터: 어떤 함수에 "미리 만든 규격화된 처리"를 적용할 때 사용하는 것.

# 데코레이터라는 함수는 기본적으로 매개변수로 함수를 받고 내부에서 어떠한 함수를 리턴해주기만 하면 된다.

def 외부데코레이터(number):
    def 데코레이터(함수):
        print("미리 어떤 처리를 진행합니다.", number)
        return 함수
    return 데코레이터

@외부데코레이터(number=100)
def 테스트():
    print("안녕하세요")

테스트()

