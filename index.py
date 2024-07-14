#Python Programs
print("Assalam-oAlikum")
print("Walikum Aslam")




name = "SANIA"
age = 24
is_present = True
weight = 50.5

nAme = "FARAH"
age = 45
weight = 70
is_present = False

print(nAme)
print(age)
print(weight)
print(is_present)

age = 90

print(age)



#variables ko kis kis trha define kr skty hai
#1st varibale case-sensitive hai like es trha
name = "Sania"
Name = "Gulzar"
NAME = "Farha"
nAme = "Adnan"
naME = "jkksncadafhhaikhf"
#ya es trha ya sb ky sb different variables hai inko print karen    GG khud kr ky dako nichy

print(Name)
print(name)
print(nAme)






#ab jb ya  chly gi tw value jo hai wo run time sy ay gi nicjy jaha hum ko sb print statment show hoti
# kasy abi dakty abi kya hoga jb koi bi vlaue enter kry gy wo value es name mai aa jy gi par hamy show nai
# hogi kyu nai hogi jb tk hum print na kr dy phly asy riun krty hai kuch bi show nai hua
name = input("Enter your name: ")
EnterAge = int(input("Enter your age: "))
gender = input("Enter your gender Male/Female : ")
# es gender ko ap khud print kry individual or phr concatenate kr ky aik hi line mai jasi
# name and ENterAge ko kiya okk

# ab kya hua jo value hum ny input mai di nichy run time mai wo us name mai ja kr save ho gai phr
# print sy wo value show krwa di esi trha hum age mai bi kr sktyhai jis trha ki mrzi input ly lo run time sy
# another example
print(name)
print(EnterAge)
# hum aik sth bi sb show krwa skty hai asy ab kya hoga wo aik sth show hoga

# or aik or tarika ky aik hi line mai show krna ho jo name hai usky samny hi age ay to kasy
#upper wali bi asy hi rko ga  or nuichy new kro ga difference pta chal sky
# jb hum string ky andr variable use krty hai tw or easy way krty hai phly srf plus use krty huy +
# wo ya error dy raha ky ap srf string ko hi add kr skty hai concatenate kr ky
print("Your name is: " + name + " Your age is: " + str(EnterAge))
# ab kya ho raha hai ky  name jo hai wo tw string hi tha par jo age thi wo integer the mean int
#hum ny kya kiya name ko same asy hi likh diya kyu ky wo already sting tha or phr hum ny age ko bi 
# string mai change kr diya KASY str() ya wala methid use kiya or bracket ky andr wo age wala variable 
# dy diya tw usny age int ko string mai cahnge kr ky print krwa diya

print(NAME)
print(EnterAge)
print("your name is: " + NAME + " Your age is: " + str(EnterAge))
# asy apko confusion ho rhi hum break down krty hai ok

print("Your name is : " + name)
print("Your age is : " + str(EnterAge))


print(NAME)
print(EnterAge)
print(gender)

print("Your name is: " + NAME)
print("Your age is: + EnterAge " + str(EnterAge))    #ap asy kr rhi thi run kr ky dako age kaha gai idk
print("Your gender is male/female : " + gender)

#if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")
    
    #short hand if
    
    if a > b: print("a is greater than b")