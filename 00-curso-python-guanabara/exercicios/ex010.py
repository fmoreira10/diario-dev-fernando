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
print(f'A medida de {km:.1f} m corresponde a:\n{hm:.3f} km\n{dam:.3f} ham\n{dm:.3f} dam\n{cm:.0f} dm\n{mm:.0f} cm\n{:.0f} mm')
