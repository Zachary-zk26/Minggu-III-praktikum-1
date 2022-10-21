print("PROGRAM GAJI KARYAWAN".center(80))
nama=input("\tNama karyawan\t: ")
anak=int(input("\tJumlah anak\t: "))
gapok=int(input("\tGaji pokok\t: "))
tks=gapok*(20/100)
tkl=gapok*(10/100)*anak
gator=gapok+tks+tkl
pajak=gator*(10/100)
gaber=gator-pajak
print("_"*80)
print("\tGaji pokok\tT. kesejahteraan\tT. keluarga\tPajak")
print(f"\t{gapok}\t{tks}\t{tkl}\t{pajak}")
print("_"*80)
print(f"Gaji kotor\t: {gator}")
print(f"Gaji Bersih\t: {gaber}")