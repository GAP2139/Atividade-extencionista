#Algumas variáveis declaradas para serem usadas no código
dados = []
b=0
headers =["Codigo do produto", "Produto", "Quantidade", "Valor"]
while True: # Uma estrutura de repetição com o While, essa estrutura só é quebrada caso o usuário digite uma entrada inválida, ou altere um item do documento
    print ( 'Escolha qual opção deseja:') # Tudo será trabalhado conforme a alteração do usuário
    print (' 1 - Verificar itens no estoque')
    print (' 2 - Adicionar um novo item no estoque')
    print (' 3 - Remover um item no estoque ')
    print (' 4 - Editar um item já existente ')
    print (' 0 - Sair do programa de estoque ')
    x = input ()
    if x == '1':
        estoque = open ( 'C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r") # A base de dados está sendo um arquivo na memória local do usuário
        print ('Codigo do produto         Produto         Quantidade         Valor') #Cabeçalho para exibir o estoque em tabela
        for linhas in estoque:
            linhas = linhas.strip()
            itens = linhas.split() # O for acima dividiu o arquivo em linhas, já esta função .split() está dividindo as palavras
            z = 1
            for y in itens:
                if z <= 8:
                    dados.append(itens[z]) # Armazeno as palavras que quero somente na variável dados
                    z += 2
                    y = y.strip()
                else:
                    break
            print('         ', dados[0], '               ', dados[1], '         ', dados[2], '              ', dados[3]) # Faço print das variáveis desejadas
            dados = [] # Limpo a variável com as palavras, caso venha usar novamente no código a mesma variável, ou precise consultar mais uma vez o estoque
        estoque.close()
    elif x == '2': # Utilizo o Elif para o programa não precisar ficar repetindo o teste se já encontrou uma igualdade
        while True:
            b=0
            arquivo = open ( 'C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r")
            for linhas in arquivo: # Esta primeira parte serve somente para incrementar uma variável que vai dar o código para cada produto, baseado no número de linhas no estoque
                linhas = linhas.strip()
                b += 1
            arquivo.close()
            print ('Qual o nome do produto?') # Recebo as informações do novo produto
            nome = input()
            print ('Quanto temos desse produto?')
            quantidade = input()
            print ('Qual o valor individual do produto?')
            valor = input()
            arquivo = open ( 'C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r")
            conteudo = arquivo.readlines()
            novo_produto = "\nCodigo: {0} Produto: {1} Quantidade: {2} Valor: {3}" .format(b+1, nome, quantidade, valor)
            conteudo.append(novo_produto)
            print(novo_produto)
            arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "w")
            arquivo.writelines(conteudo)
            arquivo.close()
            print ('Item adicionado no estoque')
            print('Deseja adicionar um novo item?(S/N)')
            w = input()
            if w in 'N/n':
                break
            else:
                continue
    elif x == '3':
        print ("Temos os seguintes produtos em estoque, qual deseja remover?:\n")
        estoque = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r")
        print('Codigo do produto         Produto')
        for linhas in estoque:
            linhas = linhas.strip()
            itens = linhas.split()
            z = 1
            for y in itens:
                if z <= 8:
                    dados.append(itens[z])
                    z += 2
                    y = y.strip()
                else:
                    break
            print('         ', dados[0], '               ', dados[1])
            dados = []
        estoque.close()
        print ('Qual o código do produto que deseja deletar? (Digitar somente o numero)\n')
        codigo_produto = input ()
        print ('Tem certeza que deseja deletar o produto?(S/N)\n')
        confirmacao = input()
        if confirmacao in 'S/s':
            arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r")
            linhas = arquivo.readlines()
            arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "w")
            for linha in linhas:
                itens = linha.split()
                print (itens[1])
                if itens[1] != codigo_produto:
                    arquivo.write(linha)
            print ('Produto deletado com sucesso \n')
            arquivo.close()
        else:
            break
    elif x == '4':
        print ("Temos os seguintes produtos em estoque, qual deseja editar?(Digite somente o Codigo do produto):\n")
        estoque = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r")
        print('Codigo do produto         Produto')
        for linhas in estoque:
            linhas = linhas.strip()
            itens = linhas.split()
            z = 1
            for y in itens:
                if z <= 8:
                    dados.append(itens[z])
                    z += 2
                    y = y.strip()
                else:
                    break
            print('         ', dados[0], '               ', dados[1])
            dados = []
        estoque.close()
        produto_editar = input()
        print ('Qual o dado que deseja alterar?\n')
        print ('1 - Nome do produto')
        print ('2 - Quantidade')
        print ('3 - Valor\n')
        dado_editar = input ()
        if dado_editar == '1':
            print ('Qual será o novo nome do produto?\n')
            novo_nome = input()
            print ('Confirmar alteração?(S/N)\n')
            confirmacao_nome = input()
            if confirmacao_nome in 'S/s':
                itens =[]
                dados = []
                arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r")
                for linha in arquivo:
                    itens = linha.split()
                    if itens[1] == produto_editar:
                        dados = itens
                        conteudo = arquivo.readlines()
                        produto_editado = "\nCodigo: {0} Produto: {1} Quantidade: {2} Valor: {3}".format(dados[1], novo_nome, dados[5],dados[7])
                        conteudo.append(produto_editado)
                        arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "w")
                        arquivo.writelines(conteudo)
                    else:
                        arquivo.write(linha)
                        continue
                dados [3] = novo_nome
                print (dados)
                print ('Produto atualizado com sucesso')
                arquivo.close()
                break

            else:
                break
        elif dado_editar == '2':
            print ('Qual será a nova quantidade?\n')
            nova_quantidade = input()
            print ('Confirmar alteração?(S/N)\n')
            confirmacao_quantidade = input()
            if confirmacao_quantidade in 'S/s':
                itens =[]
                dados = []
                arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r")
                for linha in arquivo:
                    itens = linha.split()
                    if itens[1] == produto_editar:
                        dados = itens
                        conteudo = arquivo.readlines()
                        produto_editado = "\nCodigo: {0} Produto: {1} Quantidade: {2} Valor: {3}".format(dados[1], dados[3], nova_quantidade,dados[7])
                        conteudo.append(produto_editado)
                        arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "w")
                        arquivo.writelines(conteudo)
                    else:
                        arquivo.write(linha)
                        continue
                dados[5] = nova_quantidade
                print (dados)
                print ('Produto atualizado com sucesso')
                arquivo.close()
                break
            else:
                break
        elif dado_editar == '3':
            print ('Qual será o novo valor?\n')
            novo_valor = input()
            print ('Confirmar alteração?(S/N)\n')
            confirmacao_valor = input()
            if confirmacao_valor in 'S/s':
                itens = []
                dados = []
                arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "r")
                for linha in arquivo:
                    itens = linha.split()
                    if itens[1] == produto_editar:
                        dados = itens
                        conteudo = arquivo.readlines()
                        produto_editado = "\nCodigo: {0} Produto: {1} Quantidade: {2} Valor: {3}".format(dados[1],dados[3],dados[5],novo_valor)
                        conteudo.append(produto_editado)
                        arquivo = open('C:\Programas ( antiga área de trabalho )\Faculdade\Estoque.txt', "w")
                        arquivo.writelines(conteudo)
                    else:
                        arquivo.write(linha)
                        continue
                dados[7] = novo_valor
                print(dados)
                print ('Produto atualizado com sucesso')
                arquivo.close()
                break
            else:
                break
    else:
        break
