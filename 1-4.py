from xml.sax.xmlreader import InputSource


print("PROGRAM PENGHITUNG TAGIHAN TELEPON".center(80))
print("_"*80)
print("\t\tDATA PELANGGAN")
nama=input("\t\tNama pelanggan\t\t: ")
percakapan=int(input(f"\t\tWaktu percakapan\t: "))
sms=int(input("\t\tJumlah SMS\t\t: "))
abodemen=20000
bpercakapan=percakapan*1000
bsms=sms*300
tagihan=abodemen+bpercakapan+bsms
print("\n")
print("\t\tTAGIHAN")
print(f"\t\tAbodemen\t\t: Rp{abodemen}")
print(f"\t\tBiaya percakapan\t: Rp{bpercakapan}")
print(f"\t\tTotal tagihan\t\t: Rp{tagihan}")


