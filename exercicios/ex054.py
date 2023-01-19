def printa_div_3(num):
   if num == 11:
    return
   print(num // 3)
   printa_div_3(num+1)

printa_div_3(0)