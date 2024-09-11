'''
11. O volume de uma esfera pode ser calculado pela fórmula v = (4/3)*pi*r^3 onde r é o raio da
esfera. Faça um programa que imprima uma tabela de volumes para esferas que
tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.
'''
import math

def v_esfera(r):
    return (4/3)*math.pi*r**3

print("-="*6, "TABELA", "-="*5)
print(f"\n{'RAIO (cm)':<15} {'VOLUME (cm³)':<15}")
print("-"*30)

def main():
    raio = 0 
    while raio <= 16:
        v = v_esfera(raio)
        print(f"Raio {raio:<10.1f} | {v:<15.2f}")
        print("-"*30)
        raio += 0.5 
    print("-="*15)
    
main()




    