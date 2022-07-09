str=input("Enter any String :")
str1=""
for i in str:
      if i.isspace():
          str1=str1+'$'
      else:
          str1=str1+i
print("Output String is :",str1)
