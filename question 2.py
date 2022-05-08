#question 2
binary=[]
decimal=int(input('enter a decimal number: '))
while True:
    #سي نحسب باقي القسمة
    temp=decimal%2
    # نضيف الأصفار والواحدات
    binary.append(str(temp))
    #قسمة صحيحة
    decimal//=2
    if decimal==0:
        break
binary.reverse()
binary2=''.join(binary)
print(binary2)
