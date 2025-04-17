# 📏 Como converter metros em outras unidades de medida?
#
# Este programa em Python solicita ao usuário uma distância em metros
# e realiza a conversão para outras unidades do sistema métrico:
# quilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros.
# Uma ótima forma de treinar operações matemáticas básicas e formatação de saída.

medida = float(input('Uma distância em netros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {:.1f} m corresponde a:\n{:.3f} km\n{:.3f} ham\n{:.3f} dam\n{:.0f} dm\n{:.0f} cm\n{:.0f} mm' .format(medida,km,hm,dam,dm,cm,mm))



