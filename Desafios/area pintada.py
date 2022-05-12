alt = float(input("Qual a altura da parede?"))
lar = float(input("Qual a largura da parede?"))
area = alt * lar
pit = area / 2
print(f"Sua parede tem a dimensão de {alt} X {lar} e sua área é de {area}m²")
print(f"Para pintar essa parede, você precisará de {pit}l de tinta")