produtos = {
    1: {"nome": "mouse", "preco": 400.00, "estoque": 12},
    12: {"nome": "teclado", "preco": 500.00, "estoque": 7},
    3: {"nome": "cadeira", "preco": 850.00, "estoque": 3},
    21: {"nome": "headset", "preco": 350.00, "estoque": 9},
    10: {"nome": "gabinete", "preco": 750.00, "estoque": 2}
}

clientes = {
    31: {"nome": "joao", "cpf": 98767891234},
    12: {"nome": "heloisa", "cpf": 12345678913},
    39: {"nome": "padilso", "cpf": 2221313975}
}

funcionarios = {
    100: {"nome": "mario", "cargo": "auxiliar"},
    77: {"nome": "frank", "cargo": "vendedor"},
    33: {"nome": "rock", "cargo": "analista"}
}

forma_de_pagamentos = ("pix", "dinheiro", "debito", "credito")

carrinho = []

while True:
    print("""
    ========== SISTEMA DE VENDAS ==========

    1 - Consultar clientes
    2 - Consultar funcionarios
    3 - Consultar produtos
    4 - Consultar formas de pagamento
    5 - Realizar uma venda
    0 - Encerrar o sistema
    """)

    try:
        opcao = int(input("Digite uma opcao: "))
    except ValueError:
        print("Digite um numero valido.")
        continue

    if opcao == 1:
        try:
            loc = int(input("Digite o codigo do cliente: "))

            if loc in clientes:
                print(clientes[loc])
            else:
                print("Cliente nao encontrado.")

        except ValueError:
            print("Codigo invalido.")

    elif opcao == 2:
        try:
            loc_fun = int(input("Digite o codigo do funcionario: "))

            if loc_fun in funcionarios:
                print(funcionarios[loc_fun])
            else:
                print("Funcionario nao cadastrado.")

        except ValueError:
            print("Codigo invalido.")

    elif opcao == 3:
        try:
            loc_prod = int(input("Digite o codigo do produto: "))

            if loc_prod in produtos:
                print(produtos[loc_prod])
            else:
                print("Produto nao localizado.")

        except ValueError:
            print("Codigo invalido.")

    elif opcao == 4:
        print("FORMAS DE PAGAMENTO:")

        for indice, pagamento in enumerate(forma_de_pagamentos, start=1):
            print(f"{indice} - {pagamento}")

    elif opcao == 5:

        print("========== REALIZAR VENDA ==========")

        

        try:
            cliente = int(input("Digite o codigo do cliente: "))
            funcionario = int(input("Digite o codigo do funcionario: "))

        except ValueError:
            print("Digite codigos numericos validos.")
            continue

        if cliente not in clientes:
            print("Cliente nao encontrado.")
            continue

        if funcionario not in funcionarios:
            print("Funcionario nao encontrado.")
            continue

        

        carrinho = []

        while True:

            print("\n========== PRODUTOS DISPONIVEIS ==========")

            for codigo, produto in produtos.items():
                print(
                    f"Codigo: {codigo} | "
                    f"Nome: {produto['nome']} | "
                    f"Preco: R$ {produto['preco']:.2f} | "
                    f"Estoque: {produto['estoque']}"
                )

            print("\nDigite 0 para terminar de adicionar produtos.")

            try:
                compra_produto = int(
                    input("Informe o codigo do produto: ")
                )

            except ValueError:
                print("Digite um codigo numerico valido.")
                continue

            if compra_produto == 0:
                break

            if compra_produto not in produtos:
                print("Produto nao encontrado.")
                continue

            try:
                qtd_produto = int(
                    input("Informe a quantidade desejada: ")
                )

            except ValueError:
                print("Digite uma quantidade numerica valida.")
                continue

            if qtd_produto <= 0:
                print("A quantidade deve ser maior que zero.")
                continue

            

            qtd_no_carrinho = 0

            for item in carrinho:
                if item["codigo"] == compra_produto:
                    qtd_no_carrinho += item["quantidade"]

            estoque_disponivel = (
                produtos[compra_produto]["estoque"] - qtd_no_carrinho
            )

            if qtd_produto > estoque_disponivel:
                print(
                    f"Estoque insuficiente. "
                    f"Quantidade disponivel para esta venda: "
                    f"{estoque_disponivel}"
                )
                continue

            

            item_carrinho = {
                "codigo": compra_produto,
                "nome": produtos[compra_produto]["nome"],
                "quantidade": qtd_produto,
                "preco_unitario": produtos[compra_produto]["preco"]
            }

            carrinho.append(item_carrinho)

            print("Produto adicionado ao carrinho!")

        

        if len(carrinho) == 0:
            print("Nao e possivel concluir uma venda sem produtos.")
            continue

        

        subtotal = 0

        print("\n========== RESUMO DO CARRINHO ==========")

        for item in carrinho:

            total_produto = (
                item["preco_unitario"] * item["quantidade"]
            )

            subtotal += total_produto

            print(
                f"{item['nome']} | "
                f"Quantidade: {item['quantidade']} | "
                f"Preco unitario: R$ {item['preco_unitario']:.2f} | "
                f"Total: R$ {total_produto:.2f}"
            )

        print(f"\nSubtotal: R$ {subtotal:.2f}")

        

        while True:
            try:
                desconto_percentual = float(
                    input("Informe o desconto percentual (0 a 100): ")
                )

                if 0 <= desconto_percentual <= 100:
                    break
                else:
                    print("O desconto deve estar entre 0 e 100.")

            except ValueError:
                print("Digite um desconto numerico valido.")

        valor_desconto = subtotal * desconto_percentual / 100

        total_pagar = subtotal - valor_desconto

        print(f"Desconto: {desconto_percentual:.2f}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Total a pagar: R$ {total_pagar:.2f}")

        

        print("========== FORMAS DE PAGAMENTO ==========")

        for indice, pagamento in enumerate(forma_de_pagamentos, start=1):
            print(f"{indice} - {pagamento}")

        while True:
            try:
                opcao_pagamento = int(
                    input("Escolha a forma de pagamento: ")
                )

                if 1 <= opcao_pagamento <= len(forma_de_pagamentos):
                    pagamento_escolhido = (
                        forma_de_pagamentos[opcao_pagamento - 1]
                    )
                    break

                else:
                    print("Forma de pagamento inexistente.")

            except ValueError:
                print("Digite uma opcao numerica valida.")

        

        print("\n========== CONFIRMACAO DA VENDA ==========")

        print(f"Cliente: {clientes[cliente]['nome']}")
        print(f"Funcionario: {funcionarios[funcionario]['nome']}")

        print("\nProdutos:")

        for item in carrinho:
            print(
                f"{item['nome']} | "
                f"Quantidade: {item['quantidade']} | "
                f"Preco unitario: R$ {item['preco_unitario']:.2f}"
            )

        print(f"\nSubtotal: R$ {subtotal:.2f}")
        print(f"Desconto: {desconto_percentual:.2f}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Total a pagar: R$ {total_pagar:.2f}")
        print(f"Pagamento: {pagamento_escolhido}")

        confirmacao = input(
            "\nDeseja confirmar a venda? (s/n): "
        ).strip().lower()

        

        if confirmacao == "s":

            

            estoque_valido = True

            for item in carrinho:
                if item["quantidade"] > produtos[item["codigo"]]["estoque"]:
                    estoque_valido = False
                    break

            if not estoque_valido:
                print("Venda cancelada: estoque insuficiente.")
                continue


            for item in carrinho:
                produtos[item["codigo"]]["estoque"] -= item["quantidade"]

            print("\n========== COMPROVANTE DA VENDA ==========")

            print(f"Cliente: {clientes[cliente]['nome']}")
            print(f"CPF: {clientes[cliente]['cpf']}")

            print(f"\nFuncionario: {funcionarios[funcionario]['nome']}")
            print(f"Cargo: {funcionarios[funcionario]['cargo']}")

            print("\nPRODUTOS VENDIDOS:")

            for item in carrinho:

                total_produto = (
                    item["preco_unitario"] * item["quantidade"]
                )

                
                print(f"Codigo: {item['codigo']}")
                print(f"Produto: {item['nome']}")
                print(f"Quantidade: {item['quantidade']}")
                print(
                    f"Preco unitario: R$ "
                    f"{item['preco_unitario']:.2f}"
                )
                print(f"Total do produto: R$ {total_produto:.2f}")

            print(f"Subtotal: R$ {subtotal:.2f}")
            print(f"Desconto aplicado: {desconto_percentual:.2f}%")
            print(f"Valor do desconto: R$ {valor_desconto:.2f}")
            print(f"Total a pagar: R$ {total_pagar:.2f}")
            print(f"Forma de pagamento: {pagamento_escolhido}")

            print("\nVENDA CONCLUIDA COM SUCESSO!")

        elif confirmacao == "n":
            print("Venda cancelada. O estoque foi mantido.")

        else:
            print("Opcao invalida. Venda cancelada.")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opcao invalida.")