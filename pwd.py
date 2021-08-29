password= 'a123456'
chance = 3 

while chance > 0:
    pwd = input('輸入密碼:')
    if pwd == password:
        print('登入成功')
        break
    
    else:
        chance = chance - 1 
        print('密碼錯誤!')
        if chance > 0:
            print('還有',chance,'機會')
        else:
            print('請重設密碼')