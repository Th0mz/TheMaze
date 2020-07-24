# Nome: Tomas de Araujo Tavares         Numero: 95680

def eh_labirinto(labirinto):
    """Verifica se o seu argumento e um labirinto valido e devolve: 
       .    - True : se for considerado em labirinto valido 
       .    - False : se nao for considerado um labirinto valido"""
    
    
    # Verificar se o labirinto e um tuplo e nao e vazio
    if not (type(labirinto) is tuple) or not (len(labirinto) != 0):
        return False
    
    num_linhas, num_colunas = len(labirinto[0]), len(labirinto) 
    # Verificar tamanho minimo 3x3
    if not (num_linhas >= 3 and num_colunas >= 3):
        return False    
    
    # Verifica se as colunas sao colunas validas:
    #     - Sao tuplos
    #     - Cada coluna tem o mesmo numero de entradas
    #     - Verifica se o primeiro e ultimo elementos da coluna sao paredes (rebordo do labirinto)
    for coluna in labirinto:
        if not (type(coluna) is tuple) or \
           len(coluna) != num_linhas or \
           (coluna[0] != 1 or coluna[len(coluna) - 1] != 1):
            return False      
        
        # Verificar se cada entrada e inteira igual a 1 ou 0
        for entrada in coluna:
            if not (type(entrada) is int) or \
               (entrada != 1 and entrada != 0):
                return False          
    

        # Verificar se a primeira coluna verifica as condicoes do labirinto
        for entrada in labirinto[0]:
            if entrada != 1:
                return False
                   
    # Verificar se a primeira coluna e igual a ultima
    return labirinto[0] == labirinto[num_colunas - 1]

def eh_posicao(posicao):
    """Verifica se o seu argumento e uma posicao do labirinto e devolve: 
     .    - True : se pertencer ao labirinto 
     .    - False : nao se pertencer ao labirinto"""
    
    # Verifica se a posicao e um tuplo com duas coordenadas
    if not (type(posicao) is tuple) or \
       not (len(posicao) == 2):
        return False
    
    # Verificar se as posicoes do tuplo correspondem a inteiros
    for coordenada in posicao:
        if not (type(coordenada) is int):
            return False
    
    # Verifica se os valores nao positivos nao nulos
    return posicao[0] >= 0 and posicao[1] >= 0


def eh_conj_posicoes(cnj_posicoes):
    """Verifica se o seu argumento e um conjunto de posicoes ynicas do labirinto e devolve: 
     .    - True : se todas pertencerem ao labirinto 
     .    - False : nao se pertenceremao labirinto"""
    
    sao_posicoes = True
    # Verificar so o conjunto e tuplo
    if not (type(cnj_posicoes) is tuple):
        return False
    
    posicoes_vistas = ()
    # Verificar se cada posicao e um tuplo
    for posicao in cnj_posicoes:
        if not type(posicao) is tuple:
            return False
        # Verificar se a posicao eh_posicao
        sao_posicoes = sao_posicoes and eh_posicao(posicao)
        # Verificar se a posicao e unica
        if posicao in posicoes_vistas:
            return False
        posicoes_vistas += (posicao, )
            
    return sao_posicoes



    

def tamanho_labirinto(labirinto):
    """ Devolve o numero de linhas e colunas em um tuplo na forma: 
        .        (numero linhas , numero colunas)
        
        - Se o seu argumento for invalido levanta um erro"""
    
    
    # Verificar se e labirinto
    if not eh_labirinto(labirinto):
        raise ValueError("tamanho_labirinto: argumento invalido")
    
    # Devolve o numero de linhas e colunas
    num_linhas = len(labirinto)
    num_colunas = len(labirinto[0])
    return (num_linhas, num_colunas)    
        
    
     
def eh_mapa_valido(labirinto, coordenadas):
    """ Verifica se se as coordenadas pertencem ao labirinto dado ,
       (nao ocupando paredes e encontram-se dentro dos limites do labirinto) 
       e devolve:
       
     .    - True : se as coordenadas pertencerem ao labirinto
     .    - False : se as coordenadas nao pertencerem ao labirinto
     .    - Se algum dos seus argumentos for invalido levanta um erro"""
    
    #Testar se e labirinto e se as coordenadas sao aceites
    if not (eh_labirinto(labirinto)) or \
       not (eh_conj_posicoes(coordenadas)):
        raise ValueError("eh_mapa_valido: algum dos argumentos e invalido")
    

    num_linhas = len(labirinto)
    num_colunas = len(labirinto[0])
    #Verificar se as coordenadas pertencem ao labirinto e nao sao paredes
    for coordenada in coordenadas:
        x = coordenada[0]
        y = coordenada[1]      
        if not((x in range(1, num_linhas - 1)) and \
               (y in range(1, num_colunas - 1))):
            return False
        
        # Testar se nao corresponde a alguma parede
        if labirinto[x][y] == 1:  
            return False
    return True



def eh_mapa_valido_sem_erros(labirinto, coordenadas):
    """ eh_mapa_valido so que nao gera erros"""
    
    #Testar se e labirinto e se as coordenadas sao aceites
    if not (eh_labirinto(labirinto)) or \
       not (eh_conj_posicoes(coordenadas)):
        return False
    

    num_linhas = len(labirinto)
    num_colunas = len(labirinto[0])
    #Verificar se as coordenadas pertencem ao labirinto e nao sao paredes
    for coordenada in coordenadas:
        x = coordenada[0]
        y = coordenada[1]      
        if not((x in range(1, num_linhas - 1)) and \
               (y in range(1, num_colunas - 1))):
            return False
        
        # Testar se nao corresponde a alguma parede
        if labirinto[x][y] == 1:  
            return False
    return True



def eh_posicao_livre(labirinto, unidades, posicao):
    """ Dado um labirinto, um conjunto de unidades e uma posicao
        verifica se esta posicao se encontra dentro do labirinto
        , que nao corresponde a uma parede e que nao coincide com
        uma unidade. E devolve:
        
        .    - True : se essas condicoes forem verificadas
        .    - False : se as condicoes nao forem verificadas
        .    - Se algum dos seus argumentos for invalido levanta um erro"""
    
    # Verificar se os argumantos sao validos
    if not (eh_labirinto(labirinto)) or not \
       (eh_mapa_valido_sem_erros(labirinto, unidades)) or \
       not (eh_posicao(posicao)):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")
              
    # Verificar se a posicao e corredor
    x = posicao[0]
    y = posicao[1]
    pos = labirinto[x][y]
     
    # A posicao e igual a uma unidade
    if posicao in unidades:
        return False
        
    # A posicao e igual a uma parede    
    return eh_mapa_valido_sem_erros(labirinto, (posicao, ))



def posicoes_adjacentes(posicao):
    """ Recebe uma posicao e devolve um tuplo com todas as posicoes
        adjecentes a essa posicao por ordem de leitura
        
        .    - Se o seu argumento for invalido levanta um erro"""
    
    # Verifica se e uma posicao valida
    if not eh_posicao(posicao):
        raise ValueError("posicoes_adjacentes: argumento invalido")
    
    # Calcula as posicaoes adjecentes
    posicoes_adjacentes = ()
    formula = ((0, -1), (-1, 0), (1, 0), (0, 1))
    for tuplo in formula:
        posicao_adjecente = (posicao[0] + tuplo[0], posicao[1] + tuplo[1])
        if eh_posicao(posicao_adjecente):
            posicoes_adjacentes += (posicao_adjecente, )
    
    return posicoes_adjacentes
    
    
def mapa_str(labirinto, unidades):
    """ Recebe como argumentos um labirinto e um conjunto de unidades
        pertencentes a este labirinto e retorna uma string que vai representar
        graficamente o conteudo do labirinto (paredes[#], corredores[.], unidades[O])
        
        .    - Se o seu argumento for invalido levanta um erro"""
    
    #Testar se os argumentos dados sao validos
    if not (eh_labirinto(labirinto)) or \
       not (type(unidades) is tuple):
        raise ValueError("mapa_str: algum dos argumentos e invalido")
    
    
    if len(unidades) != 0:
        if not(eh_mapa_valido_sem_erros(labirinto, unidades)):
            raise ValueError("mapa_str: algum dos argumentos e invalido")
            
    str_mapa = ""
    num_colunas = len(labirinto)
    num_linhas = len(labirinto[0])
        
    elementos_labirinto = [".", "#"]
    # Iterar por todos os elementos do labirinto para os converter para string
    for y in range(num_linhas):
        for x in range(num_colunas):
            if len(unidades) != 0 and \
               (unidades[0] == (x, y) or unidades[1] == (x, y)):
                # Unidades
                str_mapa += "O"                     
            else:
                # Paredes e Corredores
                str_mapa += elementos_labirinto[labirinto[x][y]]
               
        if y != num_linhas - 1:
            str_mapa += "\n"
    return str_mapa     

   
def obter_objetivos(labirinto, unidades, posicao):
    """ Devolve um tuplo com todas as posicoes possiveis de serem ocupadas 
        (posicoes adjecentes a unidade) nao coincidentes com outras unidades 
                                ou paredes
                                
        .    - Se o seu argumento for invalido levanta um erro"""
    
    # Verificar a validade dos argumentos da funcao
    if not (eh_labirinto(labirinto)) or \
       not (eh_mapa_valido_sem_erros(labirinto , unidades)) or \
       not (eh_posicao(posicao)):
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    
    # Verificar se a posicao pertence as unidades
    if posicao not in unidades:
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    
    pos_possiveis = ()
    for unidade in unidades:
        if unidade != posicao:
            pos_possiveis += posicoes_adjacentes(unidade)
            
    pos_possiveis_filtradas = ()
    # Filtrar as posicoes que correspondem ou a paredes ou a outras unidades
    for pos in pos_possiveis:
        if eh_mapa_valido(labirinto, (pos, )) and \
           pos not in pos_possiveis_filtradas and \
           pos not in unidades:
            pos_possiveis_filtradas += (pos, )
    
    return pos_possiveis_filtradas


def obter_caminho(labirinto, unidades, posicao):
    """ Funcao que recebe como argumentos um labirinto unidades e uma posicao, e
         devolve num tuplo o caminho mais curto da posicao ate uma das unidades 
                  aquela que se encontra mais perto dessa posicao"""
    
    # Verificar a validade dos argumentos da funcao
    if not (eh_labirinto(labirinto)) or \
       not (eh_mapa_valido_sem_erros(labirinto ,unidades)) or \
       not (eh_posicao(posicao)):
        raise ValueError("obter_caminho: algum dos argumentos e invalido")
    
    # Verificar se a posicao pertence as unidades
    if posicao not in unidades:
        raise ValueError("obter_caminho: algum dos argumentos e invalido")    
    
    lista_exploracao = [[posicao, ()]]
    lista_objetivos = obter_objetivos(labirinto, unidades, posicao)
    
    while lista_exploracao != []:
        posicao_atual = lista_exploracao[0][0]
        caminho_atual = lista_exploracao[0][1]
        posicoes_adjecentes = posicoes_adjacentes(posicao_atual)
        
        if posicao_atual not in caminho_atual:
            caminho_atual += (posicao_atual, )
            if posicao_atual in lista_objetivos:
                return caminho_atual
            else:
                for posicao_adjecente in posicoes_adjecentes:
                    if eh_posicao_livre(labirinto, unidades, posicao_adjecente):
                        lista_exploracao += [[posicao_adjecente, caminho_atual]]
                       
        lista_exploracao.pop(0)
    return ()


def mover_unidade(labirinto, unidades, posicao):
    # Verificar a validade dos argumentos da funcao
    if not (eh_labirinto(labirinto)) or \
       not (eh_mapa_valido_sem_erros(labirinto ,unidades)) or \
       not (eh_posicao(posicao)):
        raise ValueError("mover_unidade: algum dos argumentos e invalido")

    
    # Verificar se a posicao pertence as unidades
    if posicao not in unidades:
        raise ValueError("mover_unidade: algum dos argumentos e invalido")
    
    
    # Testar se as unidades estao dentro do objetivo
    posicoes_adj = ()
    for unidade in unidades:
        posicoes_adj += posicoes_adjacentes(unidade) 
    
    
    if (posicao in posicoes_adj) or len(unidades) < 2:
        return unidades
    
    # Verificar se o caminho nao e vazio
    caminho_minimo = obter_caminho(labirinto, unidades, posicao)
    if len(caminho_minimo) == 0:
        return unidades
    
    posicao_seguinte = caminho_minimo[1]
    
    unidades_deslocadas = ()
    for i in range(len(unidades)):
        if unidades[i] == posicao:
            unidades_deslocadas += (posicao_seguinte, )
        else:
            unidades_deslocadas += (unidades[i], )
            
    return unidades_deslocadas