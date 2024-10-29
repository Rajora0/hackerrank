x1 = 0
v1 = 2

x2 = 5
v2 = 3


def kangaroo(x1, v1, x2, v2):
    # Continuar enquanto o primeiro canguru não ultrapassar o segundo ou vice-versa
    while x1 <= x2:
        # Se eles estiverem na mesma posição, retornar "YES"
        if x1 == x2:
            return "YES"
        # Fazer os dois cangurus pularem
        x1 += v1
        x2 += v2
    # Se o laço terminar sem que os cangurus se encontrem, retornar "NO"
    return "NO"

print(kangaroo(x1, v1, x2, v2))