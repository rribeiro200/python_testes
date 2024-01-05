"""
TDD - Test Driven Development (Desenvolvimento dirigido a testes)

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar meu código
"""
def bacon_com_ovos(n):
    assert isinstance(n, int), 'N deve ser INT'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    
    if n % 3 == 0:
        return 'Bacon'
    
    if n % 5 == 0:
        return 'Ovos'

    return "Passar fome"