#user login application. 

kullanıcıadı=str("özgün")
şifre=(123456)
a=str(input("kullanıcı adınızı giriniz:"))
if kullanıcıadı==a:
    b=int(input("şifrenizi giriniz:"))
    if b==şifre:
        print("Doğru.")
    else:
        print("şifre yanlış")
else:
    print("kullanıcı adı yanlış.")

    
    
    
#EKSTRA (Dictionary kullanarak)

d={"özgün":123456}
d2={}
a=str(input("Kullanıcı adınızı giriniz:"))
b=int(input("Şifrenizi giriniz:"))
d2[a]= b
if d2==d:
    print("doğru.")
else:
    print("hatalı şifre veya kullanıcı adı.")
    
    
