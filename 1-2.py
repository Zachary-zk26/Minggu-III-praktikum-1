print("PROGRAM PENGHITUNG PEMBELIAN".center(80))
print("_"*80)
hsatuan=float(input("\t\tHarga satuan\t\t: Rp "))
jumlah=int(input("\t\tJumlah pembelian\t: "))
diskon=(hsatuan*jumlah)*(10/100)
htotal=(hsatuan*jumlah)-diskon
print(f"\t\tDiskon\t\t\t: Rp{diskon}")
print(f"\t\tHarga total\t\t: Rp{htotal}")
