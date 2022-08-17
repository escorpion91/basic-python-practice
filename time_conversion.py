# La idea de esta funcion es que convierta, la hora dada en formato de 12 horas am/pm,
# convertirla a formato de 24 horas

# el aproach basicamente es este:
# si te dan:
# 12am, lo conviertes a 00
# 1am a 12pm, no haces nada
# 1pm a 12 pm, le sumas 12 horas.
# en todos los casos le quitas el am o pm, ya que eso no existe en el formato militar


def timeConversion(s):
    meridian = s[-2:]
    if meridian == 'PM' and s[:2] != '12':
        s = str(12 + int(s[:2])) + s[2:]
    if meridian == 'AM' and s[:2] == '12':
        s = 'OO' + s[2:]
    return s[:-2]


result = timeConversion("12: 40: 22AM")
print(result)
