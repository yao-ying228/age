driving = input('請問你有沒有開過汽車?')
if driving !='有' and driving !='沒有' :
    print('只能輸入有或沒有')
    raise systemexit

age = input('請問你的年齡?')
age = int(age)
if driving == '有' :
    if age >= 18 :
        print('你可以開車上路了')
    else :
        print('未成年怎麼可以開車上路呢')
elif driving == '沒有' :
    if age >= 18 :
        print('你已經可以考照開車上路了')
    else :
        print('再過幾年就可以去考駕照了')

