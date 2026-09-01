# Entrada de dados
aparelho = (str(input("Digite o nome do aparelho. ")))
potencia = (int(input("Digite a potência dele em watts (ex: 400,4500) ")))
tempo_de_uso = (float(input("Digite o tempo de uso em horas durante o dia. ")))
custo_por_kWh = (float(input("Digite o custo do Kwh em sua cidade. (ex: 0.75, 0.90)")))

# Processamento 
consumo_mes = (potencia * tempo_de_uso * 30) /1000
custo = (consumo_mes * custo_por_kWh)

# Saída
print(f"\u2022 Aparelho: {aparelho}")
print(f"\u2022 Consumo: {consumo_mes:.2f} kWh")
print(f"\u2022 Custo: R$ {custo:.2f}")