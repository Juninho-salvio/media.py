# Desenvolva um programa que leia as duas notas de um aluno.
# Calcule e mostre a sua média
aluno1 = float(input('Digite a nota do aluno 1: '))
aluno2 = float(input('Digite a nota do aluno 2: '))

m = (aluno1 + aluno2) / 2
print('')
print('====================================')
print('* Aluno 1:                        {}' .format(aluno1))
print('* Aluno 2:                        {}' .format(aluno2))
print('')
print('MEDIA ENTRE OS DOIS ALUNOS:       \033[1;31m{:.1f}\033[m' .format(m))
print('====================================')