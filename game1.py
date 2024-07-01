import random


random_number = random.randint(1,10)

try:
    while number != random_number:
        print("숫자를 입력하세요")
        number = int(input())
        
        if number == random_number:
            print(f"컴퓨터 숫자 : {random_number} / 플레이어 숫자 : {number}")
            print(f"컴퓨터의 숫자를 맞추셨습니다! 통과!")
            print(f"게임종료")

        else:
            print("컴퓨터의 숫자와 다릅니다. 다시 시도해하시겠습니까? (Y/N)")
            answer = str(input())
            if answer == "y" or "Y":
                number = int(input())
            else:
                break


except TypeError:
    print(f"잘못된 형식으로 입력하셨습니다. 다시 입력해주세요")

except ValueError:
    print(f"{number}는 숫자가 아닙니다. 다시 입력해주세요")

except Exception as e:
    print(f"예상치 못한 에러가 발생했습니다. error : {e}")

"게임을 종료합니다. 감사합니다"