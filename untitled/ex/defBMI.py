#BMI <18.5, 마른체형
#18.5 <= BMI < 25.0, 표준
#25.0 <= BMI < 30.0, 비만
#BMI >= 30.0, 고도 비만


def debmi(a,b):
    bmi = a/b*b
    if bmi<18.5:
        print("마른체형")
    elif bmi<25.0:
        print("표준")
    elif bmi<30:
        print("비만")
    elif bmi>=30:
        print("고도비만")

debmi(34,168)
