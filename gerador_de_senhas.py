#!/bin/python3

import random
import os

# Montando a senha
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '#@$%&*-=+/_'

os.system('clear') # CLEAR

# VARS_ALL
vars_all = lower + upper + numbers + symbols

# Tamanho da senha
length = int(input('Digite o tamanho da sua senha: '))

# Gerando a senha
password = ''.join(random.sample(vars_all , length))
print('\n' , password)
