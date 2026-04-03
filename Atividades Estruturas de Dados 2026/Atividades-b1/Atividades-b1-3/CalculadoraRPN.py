# Calculadora RPN baseada no fluxograma



while True:

    pilha = []
    pilha_expr = []

    expressao = input("\nDigite a expressão RPN (ou 'sair'): ")

    if expressao.lower() == "sair":
        print("Programa encerrado.")
        break

    caractere = expressao.split()

    for caractere in caractere:

       
        if caractere.isdigit():
            pilha.append(int(caractere))
            pilha_expr.append(caractere)

        else:
            
            x = pilha.pop()
            y = pilha.pop()

        
            expr_x = pilha_expr.pop()
            expr_y = pilha_expr.pop()

            
            if caractere == "+":
                resultado = y + x
            elif caractere == "-":
                resultado = y - x
            elif caractere == "*":
                resultado = y * x
            elif caractere == "/":
                resultado = y / x

            
            pilha.append(resultado)

            
            nova_expr = f"({expr_y} {caractere} {expr_x})"
            pilha_expr.append(nova_expr)

        
        x = pilha[-1] if len(pilha) > 0 else 0
        y = pilha[-2] if len(pilha) > 1 else 0
        z = pilha[-3] if len(pilha) > 2 else 0

        print("X =", x, "Y =", y, "Z =", z)

    print("\nResultado =", pilha[-1])
    print("Notação Algébrica:", pilha_expr[-1])