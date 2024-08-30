'''
11. O volume de uma esfera pode ser calculado pela fórmula v = (4/3)*pi*r^3 onde r é o raio da
esfera. Faça um programa que imprima uma tabela de volumes para esferas que
tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.
'''

def v_esfera(r):
    return (4/3)*3.14*r**3

print("-="*10, "TABELA", "-="*10)
print(f"{'RAIO (cm)':<15} {'VOLUME (cm³)':<15}")
print()

raio = 0 
while raio <= 16:
    v = v_esfera(raio)
    print(f"Raio {raio:<12.1f} {v:<15.2f}")
    raio += 0.5 
print("-="*25)


    