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

# poytaxtlar={
#         'Fransiya':'Parij',
#         'Germaniya':'Berlin',
#         'Italiya':'Rim',
#         'Rossiya':'Moskva',
#         'Xitoy':'Pekin',
#         'Yaponiya':'Tokiyo',
#         'Hindiston':'Dehli',
#         'AQSH':'Vashington',
#         'Buyuk Britaniya':'London',
#         'Turkiya':'Anqara'
#         }
# print("Davlatlar:")
# for davlat in sorted(poytaxtlar.keys()):
#     print(davlat)
    
# print()

# print("Poytaxtlar:")
# for poytaxt in sorted(poytaxtlar.values()):
#     print(poytaxt)



    
# poytaxtlar={
#         'Fransiya':'Parij',
#         'Germaniya':'Berlin',
#         'Italiya':'Rim',
#         'Rossiya':'Moskva',
#         'Xitoy':'Pekin',
#         'Yaponiya':'Tokiyo',
#         'Hindiston':'Dehli',
#         'AQSH':'Vashington',
#         'Buyuk Britaniya':'London',
#         'Turkiya':'Anqara'
#         }
# sorovnoma=input("Davlat nomini kiriting:\n>>>")
# if sorovnoma in poytaxtlar :
#     print(poytaxtlar[sorovnoma])
# else:
#     print("Bizda bunday malumot yo'q")


# car_0={
#        'model':'lacetti',
#        'rang':'oq',
#        'yil':2018,
#        'narh':13000,
#        'km':50000,
#        'korobka':'avtomat'
#        }

# car_1={
#        'model':'nexia 3',
#        'rang':'qora',
#        'yil':2015,
#        'narh':9000, 
#        'km':89000,
#        'korobka':'mexanika'
#        }

# car_2={
#        'model':'gentra',
#        'rang':'qizil',
#        'yil':2019,
#        'narh':15000,
#        'km':20000,
#        'korobka':'mexanika'
#        }

# cars=[car_0 , car_1 , car_2]
# # for car in cars:
# #     print(f"{car['model'].title()},"
# #           f"{car['rang']} rang ,"
# #           f"{car['yil']}-yil , {car['narh']}$")

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")


# malibus=[]
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil':2025,
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car)
# for malibu in malibus:
#     print(malibu)
    
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
    
# for malibu in malibus:
#     print(malibu)

# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
    
# for malibu in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['korobka']='mexanika'
    
# # for malibu in malibus:
# #     print(malibu)
    
# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000 
        
# for malibu in malibus:
#     print(malibu)
#     print()


# dasturchilar={
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
# for ism , tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: " , end='')
#     for til in tillar:
#         print(f'{til.upper()}' , end=' ')


# son=1 
# while son<=5:
#     print(son , end=' ')
#     son+=1 
# print("Dastur tugadi")

# print("Kiritilgan soni kvadratini qaytaruvchi dastur")
# savol="Istalgan soni kiriting"
# savol+="(dasturni toxtatish uchun 'exit' deb yozing)\n>>>"
# qiymat=''
# while qiymat != 'exit':
#     qiymat=input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi")




# print("Kiritilgan sonni kvadratini chiqaruvchi dastur")
# savol="istalgan sonni kiriting"
# savol+="(dasurni toxtatish uchun 'exit' deb yozing)\n>>>"
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
        
# print("Dastur tugadi")


# print("Kiritilgan sonni kvadratini chiqaruvchi dastur")
# savol="istalgan sonni kiriting"
# savol+="(dasurni toxtatish uchun 'exit' deb yozing)\n>>>"
# while True:      #cheksiz tsikl:
#     qiymat=input(savol)
#     if qiymat == 'exit':
#          break
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi")


# sonlar=list(range(1,11))
# for son in sonlar:
#     if son == 7:
#         break 
#     print(f"{son}ning kvadrati {son**2}ga teng")





# sonlar=list(range(1,11))
# for son in sonlar:
#     if son == 7:
#         continue 
#     print(f"{son}ning kvadrati {son**2}ga teng")



# kitob = "Siz yoqtirgan kitoblarni kiriting:"
# while True:
#     savol=input(kitob)
#     if savol == 'exit':
#         break


# olimlar={
#     "Alisher Navoiy":{"ismi":"Mir Alisher Navoiy",
#                       "tugilgan":"1441-yil 9- fevral",
#                       "tugilgan_joy":"Hirot",
#                       "mutaxassisligi":"Buyuk shoir"
#                       },
#     "Abdurahmon Jomiy":{"ismi":"Abdurahmon Nuriddin Jomiy",
#                         "tugilgan":"1414-yil",
#                         "tugilgan_joy":"Eron",
#                         "mutaxassisligi":"shoir"
#                         },
#     "Abdulla Qodiriy":{"ismi":"Abdulla Qodiriy",
#                         "tugilgan":"1894-yil 10-aprel",
#                         "tugilgan_joy":"Ozbekiston",
#                         "mutaxassisligi":"yozuvchi"
#                         }
#     }
    
    
# olimlar['Alisher Navoiy']['asar']='Xamsa'
# olimlar['Abdurahmon Jomiy']['asar']='Bahriston'
# olimlar['Abdulla Qodiriy']['asar']='O\'tkan kunlar'

# for ismi , info in olimlar.items():
#     print(f"{info['ismi'].title()} {info['tugilgan']} {info['tugilgan_joy']}da tugilgan .\n"
#           f"Mutaxassisligi:{info['mutaxassisligi']}\n"
#           f"Uning yozgan mashxur asarlaridan biri {info['asar']}\n")


# ismi=input("Ismingizni kiriting:\n>>>")
# tartiblar=['birinchi','ikkinchi','uchinchi']
# qiziqishlar=[]
# for i in range(3):
#     kino=input(f"Siz sevgan {tartiblar[i]} kino nomini kiriting:\n>>>")
#     qiziqishlar.append(kino)
# malumot={ismi:qiziqishlar}
# print(malumot)

# savol="Siz yoqtirgan kitob nomini yozing:\n>>>"
# kitoblar=[]
# while True:
#     qiymat=input(savol)
#     if qiymat.lower() == 'stop':
#         break
#     else:
#         kitoblar.append(qiymat)
# print("Siz yoqtirgan kitoblar royxati:")       
# for kitob in kitoblar:
#     print(f"{kitob}")
    

# narxlar={"2000 so'm":(0,7),
#          "3000 so'm":(7,19),
#          "10000 so'm":(18,66),
#          "Bepul":(65, 160)
#          }
# savol='Yoshingizni kiriting'
# savol+="(dasturdan chiqish uchun 'exit' yoki 'quit' deb yozing)\n>>>"
# while True:
#         yosh=input(savol)
#         if yosh.lower() == 'exit'or yosh.lower() == 'quit':
#             break
#         yosh=int(yosh)
#         for key , value in narxlar.items():
#             if value[0]<= yosh < value[1]:
#                 print(f"Siz uchun chipta narxi:{key}\n")
#                 break
# print("Maroqli xordiq chiqaring!")



# buyurtmalar=[]
# while True:
#     savol=input("Nima buyurtma qilasiz?\n(Dasturni yakunlash uchun 'quit' deb yozing)\n>>>")
#     if savol == 'quit':
#         break
#     buyurtmalar.append(savol)
# print(buyurtmalar)




# savol="Kiritilga sonning ildizini qaytaruvchi dastur/\n"
# savol+="Musbat sonni kiriting"
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing):\n>>>"

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     qiymat=int(qiymat)
#     if qiymat<0:
#         continue
#     else:
#         ildiz=float(qiymat)**(0.5)
#         print(f"{qiymat}ning ildizi {ildiz} ga teng")




# print("Yaqin do'stlaringiz ro'yxatini tuzamiz:")
# ismlar=[]
# n=1

# while True:       
#     savol=f"{n}-do'stingizni ismini kiriting:\n>>>"
#     ism=input(savol)
#     ismlar.append(ism)
#     taklif=input("Yana ism qo'shishni xoxlaysizmi?(ha/yo'q)")
#     n+=1
#     if taklif != 'ha':
#         break
    
# print("Yaqin do'stlaringiz royxati:")
# for ism in ismlar:
#     print(ism.title())




# dostlar={}
# ishora=True
# while ishora:
#     ism=input("do'stingizni ismini kiriting:\n>>>")
#     yosh=input(f"{ism.title()}ning yoshini kiriting:\n>>>")
#     dostlar[ism]=int(yosh)
#     taklif=input("Yana ma'lumot kiritishni xoxlaysizmi?(ha/yo'q)\n>>>")
#     if taklif == "yo'q":
#         ishora = False
        
# for ism , yosh in dostlar.items():
    
#     print(f"{ism.title()} {yosh}da")





# talabalar=['hasan','husan','asmo','ali']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba}ni bahosini kiriting\n>>>")
#     print(f"{talaba} baholandi\n")
    
#     baholangan_talabalar[talaba]=int(baho)

# print(baholangan_talabalar)    
        


#Funksiyalar:
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum , hurmatli {ism.title()}!")
# salom_ber("Asmo")


# buyurtma=[]
# ishora = True
# while True:
#     buyurtma=input("Nima xarid qilmoqchisiz?\n>>>")



# mevalar={'anjir','olma','uzum'}
# mevalar.add('banan')
# #print(mevalar)
# mevalar.update(['anor','gilos'])
# #print(mevalar)
# mevalar.discard('anjir')
# #print(mevalar)
# meva=mevalar.pop()     
# print(meva)
# print(mevalar)   


# A={1,2,3,4}
# B={3,4,5,6}
# c=A|B
# print(c)
# D=A.union(B)
# print(D)


# A={1,2,3,4}
# B={3,4,5,6}
# # print(A&B)
# # D=A.intersection(B)
# # print(D)

# # print(A-B)
# # D=B.difference(A)
# # print(D)

# print(A^B)
# print(A.symmetric_difference(B))

#Homework
# colors={'red','blue','purple'}
# colors.add('yellow')
# colors.update(['white','black','pink'])
# print(colors)


# set1={10, 20, 30, 40, 50}
# set2={30, 40, 50, 60, 70}
# # similar=set1&set2
# # print(similar)
# # bir_xil=set1.intersection(set2)
# # print(bir_xil)

# D=set1.symmetric_difference(set2)
# print(D)


# bozorlik = ['choy','non','kartoshka','tuxum','sut']
# mahsulotlar = ['non','sut','tuxum','olma','un','tuz']
# bor_mahsulotlar=set(bozorlik).intersection (mahsulotlar)
# dokonda_yoq=set(bozorlik).difference(mahsulotlar)

# print(f"Do'konda bor maxsulotlar:{bor_mahsulotlar}")
# print(f"Do'konda yo'q mahsulotlar:{dokonda_yoq}")

# mahsulotlar.extend(dokonda_yoq)
# print(f"Yangilangan dokon mahsulotlari:{mahsulotlar}")

# yosh = input("Yoshingizni kiriting?\n>>>")
# try:
#     yosh = int(yosh)
#     print(f"siz {2025-yosh} yilda tugilgan ekansiz")
# except:
#     print("Butun son kiritmadingiz")
    
# print("Dastur tugadi!")




# x , y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")


# mevalar=['olma','anor','anjir','uzum']
# try:
#     print(mevalar[6])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")


# if yosh < 20:
#     pass
# else:
#     pass





# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2025-yosh}-yilda tugilgan ekansiz")



# try:
#     x= int(input("son kiriting: "))
# except ValueError:
#     print("Butun son kiritmadingiz")
# try:
#     y= int(input( "yana bir son kiriting: "))
# except ValueError:
#     print("Butun son kiritmadingiz")
# print(x, '/' , y, '=' ,x/y)



# while True:
#     x = input("Son kiriting: ")
#     if x.isdigit():
#         x=int(x)
#         break
#     else:
#         print("Faqat butun son kiriting")
        
# while True:
#     y = input("Yana bir son kiriting: ")
#     if y.isdigit():
#         y=int(y)
#         break
#     else:
#         print("Faqat butun son kiriting")
# print(x, '/', y, '=' ,x/y) 
   

# def salom_ber():
#     """Salom beruvchi dastur"""
#     print("Assalomu alaykum , xurmatli foydalanuvchi")

# salom_ber()

# def salom_ber(ism):
#     """Ism bilan salom beruvchi dastur"""
#     print(f"Assalomu alaykum , xurmatli {ism.title()}")
    
# salom_ber('ali')
# salom_ber("Asmo")

# def toliq_ism_yoz(ism , familiya):
#     """Foydalanuvchidan toliq ism qabul qilib oluvchi dastur"""
#     print(f"Foydalanuvchi ismi : {ism.title()}\n"
#           f"Foydlanuvchi familiyasi : {familiya.title()}")
    
# toliq_ism_yoz('Asmo', 'Usmonova')



# def yosh_hisobla(ism , tugilgan_yil):
#     """Foydalanuvchini yoshini hisobla""" 
#     print(f"{ism.title()} {2025-tugilgan_yil} yoshda")
    
# yosh_hisobla('Ibrohim', 2007)


# def tugilgan_yil(ism , yosh):
#     """Foydalanuvchi ismi va yoshini sorab ,\n
#     uning tugilgan yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2025-yosh} yilda tugilgan")
    
# tugilgan_yil('Ibrohim', 18)


# def hisobla(son):
#     """Foydalanuvchidan son qabul qilin ,\n
#     uning kvadrati va kubini hisoblaydigan funksiya"""
#     print(f"soning kvadrati: {son**2}\n"
#           f"sonning kubi: {son**3}")
    
# hisobla(15)


# def tekshir(son):
#     """Sonni juft yoki toqligini hisoblovchi funksiya"""
#     while True:
#         if son%2==0:
#             print("Siz kiritgan son juft son")
#             break
#         else:
#             print("Siz kiritgan son toq son")
#             break
            
# tekshir(15)


# def taqqosla(son_1 , son_2):
#     """Sonni katta kichikligini hisoblovchi funksiya"""
#     while True:
#         if son_1>son_2 or son_1<son_2:
#             print(max)
#             break
#         elif son_1==son_2:
#             print("Sonlar teng")
#             break
        
# taqqosla(5, 3)
            
            
# def toliq_ism_yasa(ism,familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism=f"{ism} {familiya}"
#     return toliq_ism

# talaba_1=toliq_ism_yasa('olim', 'hakimov')
# talaba_2=toliq_ism_yasa('hakim','olimov')
# print(f"Darsga {talaba_1.title()} va {talaba_2.title()} kelmadi")
# print(f"{talaba_1.title()} darsga kechikib keldi")




# def avto_info(kompaniya, model , rangi , korobka , yili , narh=None):
#     avto={'kompaniya' : kompaniya,
#           'model': model,
#           'rangi': rangi,
#           'korobka': korobka,
#           'yili': yili,
#           'narh': narh}
#     return avto


# avto1=avto_info('GM', 'Malibu', 'Qora', 'avtomat' , 2018)
# avto2=avto_info('GM', 'Gentra', "Oq", 'Mexanika', 2016 , 15000)
    
# avtolar=[avto1 , avto2]

    
# print("Online bozordagi mavjud avomashinalar:\n")
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh=("Noma'lum")
        
    
#     print(f"{avto['rangi']} {avto['model']} . Narhi : {narh}")



# def oraliq(min , max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar

# print(oraliq(10, 20))




# def human_info(ism, familiya, tugilgan_yil, tugilgan_joy, e_mail=None, tel_num=None):
#     human={"Foydalanuvchi ismi":ism,
#           'familiyasi':familiya,
#           'tugilgan yili':tugilgan_yil,
#           'tugilgan joyi':tugilgan_joy,
#           'elektron pochta':e_mail,
#           'tefon raqami':tel_num}
#     return human





# print("Ozingiz haqingizdagi malumotlarni kiriting.")
# malumotlar=[]#malumotlarni qoshish uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi malumotlarni kiriting" , end=' ')
#     ism=input('\nFoydalanuvchi ismini kiriting: ')
#     familiya =input('familiyasi: ') ,
#     tugilgan_yil=input('tugilgan yili: '),
#     tugilgan_joy=input('tugilgan joyi: '),
#     e_mail=input('elektron pochta: '),
#     tel_num=input('telefon raqami: ')
#     #Kiritilgan malumotlarni human_info funksiyasi yordamida 
#     #lugat shakllantirib , royxatga qoshamiz:
#     malumotlar.append(human_info(ism, familiya, tugilgan_yil, tugilgan_joy, e_mail, tel_num))
    
#     break

# print(malumotlar)




# def human_info(ism, familiya, tugilgan_yil, tugilgan_joy, e_mail=None, tel_num=None):
#     human={"Foydalanuvchi ismi":ism,
#           'familiyasi':familiya,
#           'tugilgan yili':tugilgan_yil,
#           'tugilgan joyi':tugilgan_joy,
#           'elektron pochta':e_mail,
#           'tefon raqami':tel_num}
#     return human





# print("Ozingiz haqingizdagi malumotlarni kiriting.")
# malumotlar=[]#malumotlarni qoshish uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi malumotlarni kiriting" , end=' ')
#     ism=input('\nFoydalanuvchi ismini kiriting: ')
#     familiya =input('familiyasi: ') ,
#     tugilgan_yil=input('tugilgan yili: '),
#     tugilgan_joy=input('tugilgan joyi: '),
#     e_mail=input('elektron pochta: '),
#     tel_num=input('telefon raqami: ')
#     #Kiritilgan malumotlarni human_info funksiyasi yordamida 
#     #lugat shakllantirib , royxatga qoshamiz:
#     malumotlar.append(human_info(ism, familiya, tugilgan_yil, tugilgan_joy, e_mail, tel_num))
#     javob=input("Davom etasizmi?  (yes/no): \n")
#     if javob == 'no':
#         break


# print(malumotlar)

        


# def eng_katta(a, b, c):
#     print(max(a, b, c))
    
# eng_katta(4, 754, 96)
# eng_katta(85, 18, 9874)


def calculate(a):
    """Tub son qaytaruvchi funksiya"""
    if a /a==0 or a / 1 == 0:
        print(a)
    else:
        print("Siz kiritgan son 'tub son' emas")
    return a

calculate(11)
calculate(7)
calculate(100)
        








    