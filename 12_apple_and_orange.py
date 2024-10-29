s = 7
t = 11

a = 5
b = 15

m = 3
n = 2

apples = [-2,2,1]
oranges = [5,-6]


def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Conta o número de maçãs e laranjas que caem dentro da área da casa, 
    com base nas distâncias que caíram de suas respectivas árvores.

    Args:
        s (int): O limite esquerdo da casa.
        t (int): O limite direito da casa.
        a (int): A posição da macieira.
        b (int): A posição da laranjeira.
        apples (list of int): Lista de distâncias que as maçãs caíram da árvore.
        oranges (list of int): Lista de distâncias que as laranjas caíram da árvore.

    Returns:
        None: A função apenas imprime o número de maçãs e laranjas que caem dentro da área da casa.
    """
    
    # Contar quantas maçãs caíram dentro dos limites da casa (s <= posição final <= t)
    count_apples = sum([1 for f in apples if s <= (a + f) <= t])
    
    # Contar quantas laranjas caíram dentro dos limites da casa (s <= posição final <= t)
    count_oranges = sum([1 for f in oranges if s <= (b + f) <= t])
    
    # Imprimir o número de maçãs que caíram dentro da casa
    print(count_apples)
    
    # Imprimir o número de laranjas que caíram dentro da casa
    print(count_oranges)


countApplesAndOranges(s, t, a, b, apples, oranges)
    