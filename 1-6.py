uang=int(input("Nilai uang = "))
seribuan=int(uang/1000)
dua_ratusan=int((uang-(seribuan*1000))/200)
lima_puluhan=int((uang-(seribuan*1000+dua_ratusan*200))/50)
print(f"{uang} rupiah = {seribuan} (seribuan) + {dua_ratusan} (duaratusan) + {lima_puluhan} (limapuluhan)")
