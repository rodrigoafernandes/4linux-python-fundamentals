variacao_papel = [('outubro/2000', 55.5),('novembro/2000', 35.2), ('dezembro/2000', 40.2), ('janeiro/2001', 50.0), ('fevereiro/2001', 52,2)]

print(f"As variações foram: {variacao_papel}")

variacao_total = (variacao_papel[-1][1] / variacao_papel[0][1]) - 1
variacao_ano_2000 = variacao_papel

for variacao in variacao_papel:
    if variacao[0].endswith('2000'):
        print('ano 2000')

print("A variação total foi: {0:0.2f}".format(variacao_total))

