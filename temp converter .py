print("="*10 ,"Smart temperature converter", "="*10 )
temp = float(input("Enter surrounding temperature in celcius : "))
f_temp = (temp*9/5) + 35
f_temp=round(f_temp,2)
print("Surrounding temperature in foreinheight is :",f_temp)
if f_temp < 32:
    print("it's freezing 🥶🥶")
elif f_temp >32 and f_temp <92  :
    print("it's normal 😀 😀 ")
elif f_temp >92 and f_temp<212:
    print("it's hot 🥵 🥵 ")
else:
    print("invalid temperature enterd,in this temperature either you would be burnt or you would freeze ")