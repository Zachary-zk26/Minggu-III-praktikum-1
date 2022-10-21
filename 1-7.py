gaji=int(input("Gaji\t\t= "))
hutang=int(input("Hutang\t\t= "))
gaji_bersih=gaji-hutang
biaya=gaji_bersih*(70/100)
tabungan=gaji_bersih*(20/100)
infak=gaji_bersih-(biaya+tabungan)
print(f"Biaya sehari-hari\t= {biaya}")
print(f"Tabungan\t= {tabungan}")
print(f"Infak\t\t= {infak}")