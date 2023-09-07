"""Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no
final, conforme a sua méedia atinginda:
> media abaixo de 5,0 = REPROVADO
> Média entre 5,0 e 6,9 = RECUPERAÇÃO
Média 7,0 ou superior = APROVADO
"""
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2
print('Tirando \33[0;49;92m{}\33[0m e \33[0;49;92m{}\33[0m, A média do aluno é \33[0;49;92m{:.1f}\33[0m'.format(n1, n2,
                                                                                                                med))
if med > 7:
    print('O aluno está \33[2;49;92mAPROVADO\33[0m.')
elif med < 5:
    print('Você não atingiu a média necessária \33[0;49;31mREPROVADO\33[0m!!')
else:
    print('Reforçar os estudos, \33[0;49;31mRECUPERAÇÃO\33[0m!!!')
