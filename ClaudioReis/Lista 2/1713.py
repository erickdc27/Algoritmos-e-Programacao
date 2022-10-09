valorHora = float(input(""))
horaTrabalhada = float(input(""))

salarioBruto = (valorHora * horaTrabalhada)
INSS = (salarioBruto * 0.08)
sindicato = (salarioBruto * 0.05)
impostoRenda = (salarioBruto * 0.11)
salarioliquido = (salarioBruto - INSS - sindicato - impostoRenda)

print("Salário bruto: R$%0.2f"%(salarioBruto),"\nImposto: R$%0.2f" %(impostoRenda), "\nINSS: R$%0.2f" %(INSS), "\nSindicato: R$%0.2f" %(sindicato), "\nLíquido: R$%0.2f" %(salarioliquido))

https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713