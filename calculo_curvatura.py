### AUTOR: Carlos Machado Jr.

'''
DESCRIÇÃO:

Código escrito em Python 3 que calcula a distância do horizonte e a obstrução 
causada pela curvatura da Terra em objetos distantes que se encontram após a
linha do horizonte.

Ambos os cálculos levam em consideração a influência da refração atmosférica.

'''

##### INÍCIO DO PROGRAMA ######################################################

import math

print('\n' + '-' * 80)
print('''
Este programa calcula a distância do horizonte e a obstrução causada pela 
curvatura da Terra em objetos distantes, considerando também os efeitos da 
refração atmosférica.''')

# -----------------------------------------------------------------------------

##### ATRIBUIÇÃO RÁPIDA DOS VALORES DOS DADOS DE ENTRADA ######################

switch    = 0
# switch  = 0 --> Dados de entrada fornecidos pelo usuário na tela do terminal.
# switch  = 1 --> Dados de entrada inseridos diretamente no código. 

escolha   = 3
# escolha = 1 --> Coeficiente de Refração Padrão --> k = 0.143.
# escolha = 2 --> Fornecer o valor do Coeficiente de Refração 'k'.
# escolha = 3 --> Calcular o Coeficiente de Refração 'k', em função dos
#                 parâmetros meteorológicos.

r_terra  = 6371

if switch   == 0:
    escolha = None
elif switch == 1:
    h_observ         =  1.75
    d_alvo           =  20
    h_alvo           =  50
    coef_k           =  0.143
    if escolha == 2:
        coef_k       =  0.143
    if escolha == 3:
        pressao      =  101325
        temperatura  =  20
        gradiente    =  -0.0065
    else:
        print("\nERRO: A variável 'escolha' deve receber apenas os valores " +
        '1, 2 e 3!\n') 
        exit()      
else:
    print("\nERRO: A variável 'switch' deve receber apenas os valores 0 e 1 ")
    print()
    exit()

# -----------------------------------------------------------------------------

##### DEFINIÇÃO DAS FUNÇÕES ###################################################

##### Função para cálculo da distância do horizonte em relação ao observador

def horizonte(raio_km, altura_observ_m):
    """ Calcula a distância do horizonte em relação ao observador.
    
    Args:
        raio_km (float): Raio da Terra (geométrico ou efetivo) em quilômetro.
        altura_observ_m (float): Altura do observador, em metro.
    """ 
    raio          = float(raio_km) * 1000
    altura_observ = float(altura_observ_m)
    dist_hor      = math.sqrt((raio + altura_observ) ** 2 - raio **2)
    return dist_hor

##### Função para cálculo da altura ocultada pela curvatura

def ocultacao(raio_km, dist_alvo_km, dist_hor_m):
    """ Calcula a obstrução causada pela curvatura da Terra.
    
    Args:
        raio_km (float): Raio da Terra (geométrico ou efetivo) em quilômetro.
        dist_alvo_km (float): Distância do alvo, em quilômetro.
        dist_hor_m (float): Distância do horizonte, em metro.    
    """ 
    raio          = float(raio_km) * 1000
    dist_alvo     = float(dist_alvo_km) * 1000
    altura_oculta = math.sqrt(raio ** 2 + (dist_alvo - dist_hor_m) ** 2) - raio
    return altura_oculta

##### Função para cálculo do Coeficiente de Refração 'k'

def refracao(pressao, temperatura, gradiente_temp):
    """ Calcula o Coeficiente de Refração 'k' em função dos parâmetros 
    meteorológicos.

    Args:
        pressao (float): Pressão atmosférica, em Pascal (Pa).
        temperatura (float): Temperatura ambiente, em graus Célcius (°C).
        gradiente_temp (float): Gradiente Vertical de Temperatura, em °C/m.    
    """ 
    pressao       = float(pressao)        * 0.01
    temperatura   = float(temperatura)    + 273.15
    gradiente     = float(gradiente_temp)
    coeficiente_k = (503 * pressao / temperatura ** 2) * (0.0343 + gradiente)
    return coeficiente_k

##### Função para cálculo do Raio Efetivo

def raio_efetivo(raio_terra_km, coeficiente_k):
    """ Calcula o Raio Efetivo para um determinado Coeficiente de Refração 'k'

    Args:
        raio_terra_km (float): Raio da Terra em quilômetro.
    coeficiente_k (float): Coeficiente de Refração.  
    """ 
    raio_terra = float(raio_terra_km)
    r_efetivo  = raio_terra * (1 / (1 - coeficiente_k))
    return r_efetivo

# -----------------------------------------------------------------------------

##### MENU DE OPÇÕES ##########################################################

op_0  = 'Escolha uma das opções abaixo:\n'
op_1  = 'Utilizar o Coeficiente de Refração Padrão --> k = 0.143.'
op_2  = "Fornecer o valor do Coeficiente de Refração 'k'"
op_3a = "Calcular o Coeficiente de Refração 'k' " 
op_3b = 'em função dos parâmetros meteorológicos'
op_4a = 'Modificar valor do raio da Terra'
op_4b = '(O padrão adotado pelo programa é: R = 6371 km )'
op_5  = 'SAIR'

options = [op_0, op_1, op_2, (op_3a + op_3b), (op_4a +op_4b), op_5]

while escolha == None:
    print('\n' + '-' * 80 + '\n')
    print(options[0])
    for i in range(1,6):
        print(f'[ {i} ] - {options[i]}\n')
  
    while escolha == None:
        escolha = input('Digite a opção desejada: ')
        if escolha == '5':
            print('\n' + '-' * 80 + '\n')
            print('PROGRAMA FINALIZADO!\n')
            exit()
        if escolha.isnumeric() == True and int(escolha) in range(1,6):
            if int(escolha) == 4:
                r_terra = input('\nDigite o valor do raio da Terra (em km): ')
                op_4b = f'(O valor atual é: R = {r_terra} km)'
                options[4] = op_4a + op_4b
                r_terra = float(r_terra)
                escolha = None
                break
            else:
                escolha = int(escolha)
        else:
            print('\nOpção inválida!\n')
            escolha = None  

        if escolha != None:
            print('\n' + '-' * 80 + '\n')
            print(f'[ {escolha} ] - {options[escolha]}')

# -----------------------------------------------------------------------------

##### DADOS DE ENTRADA (FORNECIDOS NO TERMINAL) ###############################

if switch == 0:

    print ('\nEntre com os dados solicitados abaixo:')

    if escolha == 1:
        coef_k = 0.143

    if escolha == 2:
        coef_k = float(input("\nCoeficiente de Refração 'k': "))
        
    if escolha == 3:
        pressao     = input('\nPressão atmosférica (em Pascal): ')
        temperatura = input('\nTemperatura (em Celcius): ')
        gradiente   = input('\nGradiente Vertical de Temperatura (em °C/m): ')
    
    h_observ = input('\nAltura do observador (em metro): ')
    d_alvo   = input('\nDistância do alvo em relação ao observador (em km): ')
    h_alvo   = input('\nAltura do alvo (em metro): ')

# -----------------------------------------------------------------------------

##### CÁLCULO DOS PARÂMETROS DE REFRAÇÃO ######################################

if escolha == 1 or escolha == 2:
    pressao     = ' - '
    temperatura = ' - '
    gradiente   = ' - '

if escolha == 3:
    coef_k    = refracao(pressao, temperatura, gradiente)

r_efetivo    = raio_efetivo(r_terra, coef_k)

# -----------------------------------------------------------------------------

##### CÁLCULO GEOMÉTRICO ######################################################

##### SEM Refração

d_hor    = horizonte(r_terra, h_observ)
h_oculto = ocultacao(r_terra, d_alvo, d_hor)

if float(d_alvo) * 1000 > d_hor:
    if h_alvo == 0:
        h_visivel = 0
    else:
        if h_oculto  >= float(h_alvo):
            h_visivel = 0.00
        else:
            h_visivel = float(h_alvo) - h_oculto
else:
    h_visivel = float(h_alvo)

##### COM Refração

d_hor_ref     = horizonte(r_efetivo, h_observ)
h_oculto_ref  = ocultacao(r_efetivo, d_alvo, d_hor_ref)

if float(d_alvo) * 1000 > d_hor_ref:
    if  h_alvo == 0:
        h_visivel_ref = 0
    else:
        if  h_oculto_ref >= float(h_alvo):
            h_visivel_ref = 0.00
        else:
            h_visivel_ref = float(h_alvo) - h_oculto_ref
else:
    h_visivel_ref = h_alvo

# -----------------------------------------------------------------------------

##### IMPRESSÃO DOS RESULTADOS ################################################

print('\n' + '-' * 80)

refracao_str  = [str(pressao), str(temperatura), str(gradiente), 
    str(round(coef_k,3))]

curvatura_str = [r_terra, h_observ, d_alvo, h_alvo, d_hor * 0.001, h_oculto, 
    h_visivel]

refr_curv_str = [d_hor_ref * 0.001, h_oculto_ref, h_visivel_ref]

for i in range(0 , len(curvatura_str)):
    curvatura_str[i] = str(round(float(curvatura_str[i]) , 2))

for i in range(0 , len(refr_curv_str)):
    refr_curv_str[i] = str(round(float(refr_curv_str[i]) , 2))

if escolha == 3:
    undd = [ 'Pa'  , '°C'  , '°C/m',   ''  ]

else:
    undd = [  ''   ,   ''  ,   ''  ,   ''  ]

grdz = [['Pressão Atmosférica'     , undd[0]] ,
        ['Temperatura Ambiente'    , undd[1]] ,
        ['Gradiente de Temperatura', undd[2]] ,
        ['Índice de Refração'      , undd[3]] ]

print('\nPARÂMETROS METEOROLÓGICOS:')
for i in range(0,len(grdz)):
    tab = 32 - len(grdz[i][0])   
    print(f'- {grdz[i][0]}: {refracao_str[i].rjust(tab)} { grdz[i][1]}') 

grdz = [['Raio da Terra'         , 'km'] ,
        ['Altura do observador'  , 'm' ] ,
        ['Distância do alvo'     , 'km'] ,
        ['Altura do alvo'        , 'm' ] ,
        ['Distância do horizonte', 'km'] , 
        ['Altura oculta'         , 'm' ] ,
        ['Altura visível'        , 'm' ] ]

print('\nCÁLCULO GEOMÉTRICO:')
for i in range(0,len(grdz)):
    tab = 32 - len(grdz[i][0])   
    print(f'- {grdz[i][0]}: {curvatura_str[i].rjust(tab)} { grdz[i][1]}')    

grdz = [['Distância do horizonte', 'km'] ,
        ['Altura oculta'         , 'm' ] ,
        ['Altura visível'        , 'm' ] ]

print('\nCÁLCULO GEOMÉTRICO COM REFRAÇÃO:')
for i in range(0,len(grdz)):
    tab = 32 - len(grdz[i][0])    
    print(f'- {grdz[i][0]}: {refr_curv_str[i].rjust(tab)} { grdz[i][1]}') 

print('\n' + '-' * 80 + '\n')

# -----------------------------------------------------------------------------

##### FIM DO PROGRAMA #########################################################
