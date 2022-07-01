def getIndexList(v_kata,v_list,idx, v_temp):
	print("Output : ")
	strList.insert(idx, v_temp)
	for i, j in enumerate(v_list):
		if j == v_kata:
			print("Kata "+j+" pada urutan ke : ",i+1)
			
x = (input("Masukan jumlah kata : "))

try:
	strList = []
	for i in range(int(x)):
		kata = (input("Masukan kata : "))
		strList.append(kata)
	v_result = 0
	v_temp = ''
	for i in range(len(strList)):
		strList[i] = strList[i].lower()
	# print("STR LIST : ",strList)

	for idx, x in enumerate(strList):
		strList = strList
		v_temp = strList[idx]
		strList.pop(idx)
		if v_temp in strList:
			getIndexList(v_temp,strList,idx, v_temp)
			break
		else:
			pass
		strList.insert(idx, v_temp)
		
except Exception as e:
	print("Jumlah kata harus berupa angka")




