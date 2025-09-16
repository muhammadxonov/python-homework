# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 08:54:16 2025

@author: Asus
"""

#takrorlash
# dasturlash="Hello world"
# print(dasturlash)
# xabar="O`zbekistonda bugundan yangi oquv yili boshlandi"
# print(xabar)
# xabar="Universtitetlarda darslar 9-sentabrdan boshlanadi"
# print(xabar)

# kocha="Bog`bon"
# mahalla="Sag`bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# print(kocha,"ko`chasi ,",mahalla , "mahallasi ,", tuman , "tumani," , viloyat , 'viloyati')


#sorovnoma
# kocha_=input("Yashaydigan kochangiz nomini kiriting\n>>>")
# mahalla_=input("Yashaydigan maxallangiz nomini kiriting\n>>>")
# tuman_=input("Yashaydigan tumaningiz nomini kiriting\n>>>")
# viloyat_=input("Yashaydigan viloyatingizni nomini kiriting\n>>>")
# print(">>>" , kocha_ ,"kochasi,\n>>>",mahalla_ ,"maxallasi,\n>>> " ,tuman_ ,' tumani,\n>>> ',viloyat_ , "viloyati")



#test
# kocha="Bogbon kochasi,"
# mahalla="Sagbon mahallasi,"
# tuman="Bodomzor tumani,"
# viloyat="Samarqand viloyati"
# manzil=f"{kocha.title()} {mahalla.lower() } {tuman.upper() } {viloyat.capitalize()}"
# print(manzil)

#keyingi dars
# son=int(input("sonni kiriting\n>>>"))
# print("kvadrati:" , son**2 , "\nkubi:" , son**3)

# yosh=int(input("Yoshingiz nechida?\n>>>"))
# print("Demak siz  ", 2025-yosh,"da tugilgan ekansiz")


# bax=int(input("1 -sonni kiriting:\n>>>"))
# vax=int(input("2-sonni kiriting:\n>>>"))
# print('yigindisi:',bax+vax,"\nayirmasi:",bax-vax,"\nkopaytmasi:",bax*vax,"\nbolinmasi",bax/vax)

#for tsikli


# mehmonlar=['Ali' , 'Vali' , 'Hasan' , 'Husan' , 'Olim']
# for mehmon in mehmonlar:
#     print("Salom" , mehmon)


# mehmonlar=['Ali' , 'Vali' , 'Hasan' , 'Husan' , 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon} , siz    print("Hurmat bilan , Palonchiyevlar oilasi\n")
# ni 20 Dekabr kuni nahorgi oshga taklif etamiz")

#sonlar bilan 
# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f"{son}ning kvadrati{son**2} ga teng")
    
# sonlar=list(range(11))
# sonlar_kvadrati=[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlar_kvadrati)

#dostlar 
# dostlar=[] # bosh royxat yaratib olamiz
# print("5 ta eng yaqin dostingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-dostingizning ismini kiriting\n>>>"))
# print(dostlar)

#Amaliyot 

# ismlar=['Ali', 'Umar', 'Rahim' , 'Doniyor', 'Ibrohim']
# for ism in ismlar:
#     print('Salom' , ism) #kod 5 marta takrorlanadi

#2-amaliyot
# sonlar=list(range(11,101,2))
# for son in sonlar:
#      print(f"kubi={son**3}\n")

#3-amaliyot
# kinolar=[]#bosh toplam yaratamiz
# print("5 ta ozingiz sevgan kinolar qaysi")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-siz yoqtirgankino nomini kiriting\n>>>"))
# print(kinolar)


#10-dars tarmoqlanish


# avtolar=['audi','bmw','volvo','kia','hyundai']

# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism=input('Salom , ismingiz nima?\n>>>')
# if ism.lower() != 'ibrohim':
#     print(f'Uzr {ism.title()} , biz Ibrohimni kutyapmiz.')
# else:
#     print("Salom Ibrohim,\nXush kelibsiz!")



# javob=float(input("12x6 nechaga teng?\n>>>"))
# if javob != 72:
#     print("Javobingiz xato")


# yosh=int(input("Yoshingiz nechida?\n>>>"))
# if yosh >= 18:
#     print("Xush kelibsiz!")
# else:
#     print("Kirish mumkin emas")


# Login=input("Yangi login kiriting:\n")
# if len(Login)<5:
#     print("Login 5 ta xarfdan uzun bolishi shart")
    
# yil=int(input("Tugilgan yilingizni kiriting\n"))
# if 2025-yil<18:
#     print(f'Yoshingiz {2025-yil}da ekan')
#     print("Kirish mumkin emas")
# else:
#     print("Xush kelibsiz!")


#uy iwi
# yangi_cars = ['toyota','mazda','hyundai','gm','kia']
# for avto in yangi_cars:
#     if avto != 'gm':
#         print(avto.title())
#     else:
#         print(avto.upper())




# ism=input("Salom , ismingizni kiriting\n")
# if ism.lower()=="ibrohim":
#     print("Xush kelibsiz Ibrohim\nFoydalanuvchilar royxatini korasizmi?")
# else:
#     print(f"Xush kelibsiz {ism.title()}!")


# son=str(input("Birinchi sonni kiriting\n"))
# son_=str(input("Ikkinchi sonni kiriting\n")) 
# if son == son_:
#     print("Ikkta son bir xil ekan")


# son=int(input('Isatgan soningizni kiriting.\n>>>'))
# if son < 0:
#     print("Manfiy son")
# else:
#      print("Musbat son")    
    


# son=int(input("Isatagn soningizni kiriting.\n>>>"))
# if son > 0:
#     print(f'Siz kiritgan son ildizi {son**(0.5)}ga teng ekan')
# else:
#     print('Musbat son kiriting')



# son=int(input("Istalgan sonni kiriting.\n>>"))
# if son % 2 == 0:
#     print("juft son ")
# else:
#     print("Toq son ")


#11-dars: If-elif-else

# yosh=int(input("Yoshingiz nechada?\n>>>"))
# if yosh <= 4:
#     narh = 0
# elif yosh<=12:
#     narh = 5000
# elif yosh<=18:
#     narh = 8000
# else:
#     narh = 10000

# print(f'Sizga kirish {narh} so\'m')
  


# kun=input("Bugun kun nima?\n>>>")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni")

    

# kun=input("Bugun nima kun?\n>>>")
# harorat=float(input("Bugun harorat qanday?\n>>>"))

# if kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat>=30:
#     print("Cho'milgani kettik!")
# elif kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat <30:
#     print('Bugun uyda dam olamiz!')


# narh=15000 #mijoz 15000 so'mga taom oldi
# choy = True
# salad = True

# if choy and salad:
#     narh = narh + 10000
# elif choy or salad:
#     narh = narh + 5000
    
# print(f"Jami {narh} so'm ")
     

# narh=15000 #mijoz 15000 so;mga ovqat oldi
# choy=1
# salad=1
# non=0
# kompot=1
# assorti=0
# #quyidagi xar bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy :
#     print("Mijoz choy oldi")
#     narh=narh+5000
# if salad:
#     print("Mijoz salad oldi")
#     narh=narh+3000
# if non :
#     print("Mijoz non oldi")
#     narh=narh+3000
# if kompot:
#     print("Mijoz kompot oldi")
#     narh=narh+7000
# if assorti:
#     print("Mojoz assorti oldi")
#     narh=narh+10000
    
# print(f"Jami{narh}")




# menu=['osh','qozonkabob','shashlik','norin','somsa']
# ovqat=input("Nima ovqat yeysiz?\n>>>")
# if ovqat.lower() in menu:
#     print("Zakaz qabul qilindi")
# else:
#     print('Afsuski bizda bunday ovqat mavjud emas')


# menu=['osh','qozonkabob','shashlik','norin','somsa']
# buyurtma=['osh','somsa','sho\'rva','kabob']
# for taom in buyurtma:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Menuda {taom} yo'q")
    

# menu=['osh','qozonkabob','shashlik','norin','somsa']
# buyurtmalar=['osh','somsa','sho\'rva','kabob']
# if buyurtmalar:
#      for taom in buyurtmalar:       
#          if taom in menu:
#              print(f"Menuda{taom} bor")
#          else:
#              print(f"Kechirasiz menuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh")

    




# sonlar=int(input("Juft son kiriting\n>>>"))
# if sonlar % 2 == 0:
#     print("Rahmat!")
# elif sonlar%2!=0:
#     print("Bu son juft emas")




# yosh=int(input("Yoshingizni kiriting!\n>>>"))
# if yosh<4 or yosh > 60:
#     print("Sizga bilet bepul")
# elif yosh < 18 :
#     print("Sizga bilet narxi 10000 so'm")
# else:
#     print("Sizga bilet narxi 20000 so'm")    
    
 
    
 
# test=int(input("1-sonni kiriting\n>>>"))
# test_1=int(input("2-sonni kiriting\n>>>"))
# if test > test_1 :
#     print("Birinchi son katta.") 
# elif test==test_1:
#     print("Sonlar bir biriga teng.")
# else:
#     print("Ikkinchi birinchisidan katta.")


# mahsulotlar=['olma','anor','banan','kivi','olicha','gilos','nok','uzum','behi','ananas','xurmo','o\'rik','shftoli']
# savat=[]#bosh ro'yxat

# for i in range(5):
#     mahsulot=input(f"{i+1} maxsulotni kiriting\n>>>")
#     savat.append(mahsulot)
    
# for mahsulot in savat:
    
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot.title()}-dokonimizda bor")
#     else:
#         print(f"{mahsulot.title()}-dokonimizda yo'q")



# mahsulotlar=['olma','anor','banan','kivi','olicha','gilos','nok','uzum','behi','ananas','xurmo','o\'rik','shftoli']
# bor_mahsulotlar=[]
# mavjud_emas=[]
# for i in range(5):
#     buyurtma=input(f"{i+1}-mahsulotni kiriting\n>>>").lower()
#     if buyurtma in mahsulotlar:
#         bor_mahsulotlar.append(buyurtma)
#     else:
#         mavjud_emas.append(buyurtma)
        
# if not mavjud_emas:
#     print("Barcha mahsulotlar do'konimizda mavjud.")
# else:
#     print("Quyidagi mahsulotlar do'konimizda yo'q")
#     for m in mavjud_emas:
#         print("-", m.title())




# foydalanuvchi=['usmonxon','nargizaxon','ibrohim','ismoil','muhammad sodiq']
# login=input('Login kiriting\n>>>').lower()
# if login in foydalanuvchi:
#     print("Login band, yangi login kiriting.")
# else:
#     print(f"Xush kelibsiz {login.title()}. ")



# son=int(input("Butun son kiriting\n>>>"))
# bolinuvchilar=[]
# for i in range(2,11):
    
#     if son % i == 0:
#         bolinuvchilar.append(i)
# print(bolinuvchilar)



#14-dars lugatlar
# car_0={'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# en_uz={'apple':10000 , 'apricot':8000 , 'banana' : 10000}
# print(f"olma narxi {en_uz['appl}e'] so'm")

# talaba_0={'ism' : 'murod olimjonov','yosh' : 20,'yil' : 2005}


# talaba_0['kurs']=4
# talaba_0['fakultet']='informatika'
# talaba_0['ism'] = 'abdulloh'

# print(talaba_0)



# ota={'ism':'usmonxon','familiya':'saidov','t_yil':'1979','t_joy':'chust'}
# print(f"{ota['familiya'].title()}  {ota['ism'].title()}  {ota['t_yil']} yilda {ota['t_joy'].title()} tumanida tugilganlar")

  
# ona={'ism':'nargizaxon','familiya':'azizova','t_yil':'1987','t_joy':'chust'}    
# print(f"{ona['familiya'].title()}  {ona['ism'].title()}  {ona['t_yil']} yilda {ona['t_joy'].title()} tumanida tugilganlar")
    
 
# aka_1={'ism':'ibrohimxon','familiya':'muhammadxonov','t_yil':'2007','t_joy':'chust'}   
# print(f"{aka_1['familiya'].title()}  {aka_1['ism'].title()}  {aka_1['t_yil']} yilda {aka_1['t_joy'].title()} tumanida tugilganlar") 
         

# ota_1={'bir':'osh','ikki':'kabob','uch':'sho\'rva','to\'rt':'manti','besh':'lag\'mon'}
# ona_1={'bir':'somsa','ikki':'norin','uch':'mastava','to\'rt':'dimlama','besh':'chuchvara'}
# aka_2={'bir':'beshbarmoq','ikki':'galupsi','uch':'pitsa','to\'rt':'qurtob','besh':'sushi'}
# print(f"{ota_1['ikki']} {ona_1['uch']} {aka_2['ikki']}")


# talaba_1={}
# talaba_1['ism']='qobil rasulov'
# talaba_1['kurs']=3
# talaba_1['yosh']=20
# talaba_1['ism']='abdulloh rasulov'
# del talaba_1['yosh']
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# en_uz={'apple':'olma','appricot':'o\'rik','banana':'banan'}
# print(en_uz)

# telefonlar={ 
#     'ali':'IPhone X',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'anvar':'pixel 3xl'
#     }
# phone=telefonlar.get('nodir','Bunday ism mavjud emas')
# print(phone)



# lugat={'integer':'butun son malumot turi','float':'10lik son malumot turi','string':'matnli malumot turi','if':'agar','else':'aks xolda','elif':'aks xolda(shart bolsa)'}
# print(lugat)


#lugat
# lugat={'apple':'olma','apricot':'o\'rik','banana':'banan','pineapple':'ananas'}
# #Foydalanuvchidan sozni kiritishini soraymiz
# soz=input("So'zni kiriting:\n>>>").lower()
# #soz lugatda bor yoqligini tekshiramiz
# if soz in lugat :
#     print(lugat[soz])
# else:
#     print("Bunday soz mavjud emas")



# talaba_0={'ism':'alijon','familiya':'shamsiyev','yosh':'22','faultet':'matematika','kurs':'4'}
# print(talaba_0.items())
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit : {kalit}")
#     print(f"Qiymat : {qiymat}\n")


# telefonlar={ 
#     'ali':'IPhone X',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'anvar':'pixel 3xl'
#     } 
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")


# mahsulotlar={
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
#print(mahsulotlar.keys())
# print("Dokondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
    
    
    
# mahsulotlar={
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# bozorlik={'anor','uzum','non','baliq'}
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()}ning narxi {mahsulotlar[mahsulot]}")
    
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos dokoningizga {buyum } xam olib kelib qoying")
    
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())    

    
#values
# print("Foydalanuvchilar quyidagi telefonlar ishlatishadi: ")
# for tel in telefonlar.values():
#     print(tel)
    
    
# telefonlar={
#      'ali':'IPhone X',
#      'vali':'galaxy s9',
#      'olim':'mi 10 pro',
#      'orif':'nokia 3310',
#      'hamida':'galaxy s9',
#      'maryam':'huawei p30',
#      'tohir':'IPhone X',
#      'umar':'IPhone X'}
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
# for tel in set(telefonlar.values()):
#     print(tel)  


# toys={"bear","doll","ball","bear","lamp","car"}
# print(toys)    


    



    
    
    
    
        
        

     
    
    



    

      








































































































































