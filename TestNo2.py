import keyboard
import math

def formatrupiah(uang):
	if uang is None or uang == "None":
		return ""
	nominal = str(uang)
	if len(nominal) <= 3:
		nominal = nominal
		hasil = nominal
		return hasil
	else:
		p = nominal[-3:]
		q = nominal[:-3]
		hasil = (formatrupiah(q) + '.' + p)
		return hasil

def pecahan(uang):
	result = ""
	if uang is None or uang == "None":
		return ""
	nominal = int(uang)
	if nominal >= 100000:
		hasil = nominal / 100000
		vket = "100.000"
		vangka = 100000
	elif nominal >= 50000:
		hasil = nominal / 50000
		vket = "50.000"
		vangka = 50000
	elif nominal >= 20000:
		hasil = nominal / 20000
		vket = "20.000"
		vangka = 20000
	elif nominal >= 10000:
		hasil = nominal / 10000
		vket = "10.000"
		vangka = 10000
	elif nominal >= 5000:
		hasil = nominal / 5000
		vket = "5.000"
		vangka = 5000
	elif nominal >= 2000:
		hasil = nominal / 2000
		vket = "2.000"
		vangka = 2000
	elif nominal >= 1000:
		hasil = nominal / 1000
		vket = "1.000"
		vangka = 1000
	elif nominal >= 500:
		hasil = nominal / 500
		vket = "500"
		vangka = 500
	elif nominal >= 200:
		hasil = nominal / 200
		vket = "200"
		vangka = 200
	elif nominal >= 100:
		hasil = nominal / 100
		vket = "100"
		vangka = 100
	if math.floor(hasil) >= 1:
		result += str(math.floor(hasil))+" lembar Rp "+vket
		print(result)
		if int(nominal-(math.floor(hasil)*vangka)) == 0:
			pass
		else:
			pecahan(nominal-(math.floor(hasil)*vangka))

x = (input("Total belanja seorang customer: Rp "))
y = (input("Pembeli membayar: Rp "))

kembali = (int(y) - int(x))
pembulatanKembali = kembali // 100 *100
if int(pembulatanKembali) >= 0:
	print("\nKembalian yang harus diberikan kasir: Rp " + str(kembali), "dibulatkan menjadi " + str(pembulatanKembali) +"\n")
	print("Pecahan uang:")
	pecahan(pembulatanKembali)
else:
	print("\nFalse, kurang bayar")


