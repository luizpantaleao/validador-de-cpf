CPF = input('Digite o cpf:')
cpf = CPF[0: 9]
p = 10
f = 11
S1 = 0
S2 = 0
for i in cpf:
    d = int(i)
    m = d * p
    print(d, f'x {p} = {m}')
    p -= 1
    S1 += m
print()
for i in cpf:
    d = int(i)
    M = d * f
    print(d, f'x {f} = {M}')
    f -= 1
    S2 += M
print()
D1 = 11 - (S1 % 11)
if D1 > 9:
    D1 = 0
print(f'O dígito 1 é {D1}\n')
S2F = S2 + (D1 * 2)
D2 = 11 - (S2F % 11)
if D2 > 9:
    D2 = 0
print(f'O dígito 2 é {D2}')
a = int(CPF[9])
b = int(CPF[10])
if a == D1 and b == D2:
    print('CPF validado')
else:
    print('CPF inválido')