import networkx as nx
from simplify import load_participants
from data.vectorization_texts import *

participants = load_participants() #Llista d'elements classe Participant

def crear_grafo(participants): #Función que crea un grafo con los participantes como nodos y sus atributos como atributos de los nodos
    G = nx.Graph()

    #Lista de atributos de la nueva clase SimpleParticipant
    atributs = ['year','program_skills','experience','hackathons','roles','languages','challenges','friend_registration','preferred_team_size','interests','objective','availability']

    #Convertir los participantes en nodos
    for participant in participants:
        # Añadir el nodo con su ID
        G.add_node(participant.id)
        
        # Añadir atributos al nodo
        for característica in atributs:
            # Usar getattr para obtener el valor del atributo dinámicamente
            valor = getattr(participant, característica, None)  # None si no existe el atributo
            G.nodes[participant.id][característica] = valor
    return G


def conexiones_amigos(G,id_usuari): #Función que crea las aristas entre el nodo del usuario si cumplen la condición de friend_registration del nodo usuario
    
    G_amistats = nx.Graph()

    for node in G.nodes[id_usuari]['friend_registration']:  
    # Crear una arista entre el nodo y cada uno de sus amigos
         G_amistats.add_edge(id_usuari, node)
    return G_amistats


def comparar_disponibilidad(horas_usuari, horas_x): #Función que comprueba si se coincide en al menos 3 rangos de horas
    horas_compatibles = sum(1 for i in range(len(horas_usuari)) if horas_usuari[i] and horas_x[i])
    return horas_compatibles >= 3


def preferencias_experiencia(G,id_usuari,id_x): #Función que compara el nivel de experiencia entre usuarios

    atributos_exp = ['year','experience','hackathons','program_skills']
    weight = 0
    for atributo in atributos_exp:
        if G.nodes[id_usuari][atributo] == G.nodes[id_x][atributo]:
            weight+=1
    return weight


def preferencias_prioritarias(G,id_usuari,id_x): #Función que compara los objetivos y necesidades linguísticas entre usuarios

    weight = 0

    for element in G.nodes[id_usuari]['challenges']:
        if element in G.nodes[id_x]['challenges']:
            weight += 1
            break
    
    for element in G.nodes[id_usuari]['languages']:
        if element in G.nodes[id_x]['languages']:
            weight += 1
            break 
    
    #Falta implementar el objetivo

    return weight*2


def preferencias_min(G,id_usuari,id_x): #Función que compara intereses ajenos y compativilidad del rol

    weight = 0
    if G.nodes[id_usuari]['roles'] != G.nodes[id_x]['roles']:
        weight +=1

    #Falta implementar interest

    return weight*0.5


def conexiones_preferencias(G,id_usuari): #Función que crea las aristas entre el nodo usuario y nodos desconocidos añadiendo un peso en función de la compatibilidad de preferencias

    H = nx.Graph()
    nodos_amigos_a_eliminar = list(conexiones_amigos(G,id_usuari)) #Eliminamos a los amigos, ya se habrán añadido si previametne si hay
    for node in nodos_amigos_a_eliminar:
        G.remove_node(node)
    
    for node in G.nodes():
        if comparar_disponibilidad(G.nodes[id_usuari]['availability'],G.nodes[node]['availability']):
            weight = 0
            weight += preferencias_experiencia(G,id_usuari,node)
            weight += preferencias_prioritarias(G,id_usuari,node)
            weight += preferencias_min(G,id_usuari,node)
            weight += calcular_similitud_intereses(G.nodes[id_usuari]['interests'],G.nodes[node]['interests'])
            weight += calcular_similitud_objetivos(G.nodes[id_usuari]['objective'],G.nodes[node]['objective'])
        if weight > 0:
            H.add_edge(id_usuari, node, weight=weight) #Nuevo grafo H formado por todas las nuevas conexiones del usuario

    return H





    
            
        

    


        
    


    





         







