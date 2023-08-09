sec = int(input("Digite o valor em segundos: "))
horas = sec // 3600
sec = sec % 3600
min = sec // 60
sec = sec % 60

print("%02.i" % horas,"%02.i" % min,"%02.i" % sec, sep=":")
