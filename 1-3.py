print("PROGRAM PENJUALAN BUKU".center(80))
print("_"*80)
hsatuan=float(input("\t\tHarga satuan\t\t: Rp"))
jumlah=int(input("\t\tJumlah penbelian\t: "))
diskon=int(input("\t\tDiskon\t\t\t: "))
new_diskon=(diskon/100)*(hsatuan*jumlah)
htotal=(hsatuan*jumlah)-new_diskon
print(f"\t\tHarga total\t\t: Rp{htotal}")