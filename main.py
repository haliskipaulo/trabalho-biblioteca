import sqlite3
import os
import csv


# === CRIAR ESTRUTURA DE PASTAS ===
def criar_pastas():
    os.makedirs('TrabalhoPythonLivraria/data', exist_ok=True)
    os.makedirs('TrabalhoPythonLivraria/backups', exist_ok=True)
    os.makedirs('TrabalhoPythonLivraria/exports', exist_ok=True)





# === BD AQUI EMBAIXO =====

def create_db():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')
    consulta = conn.cursor() #cursor para para interagir com o  banco
    consulta.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER,
            preco FLOAT
        )
    ''')
    conn.commit()
    conn.close()




# === ADICIONAR UM NOVO LIVRO AQUI EMBAIXO =====

def adicionar_livro():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')
    consulta = conn.cursor()

    titulo = input('Digite o título do livro: ')
    autor = input('Digite o nome do autor do livro: ')
    ano_publicacao = int(input('Digite o ano de publicação: '))
    preco = float(input('Digite o preço do livro: '))

    consulta.execute('''INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)''', (titulo, autor,ano_publicacao, preco))
    conn.commit()
    conn.close()    
    # Usado ? no lugar de $s e tals, pois o proprio sql substitui os valores. E é mais seguro, mesmo nesse caso n precisando





# === EXIBIR TODOS OS LIVROS AQUI EMBAIXO =====

def exibir_livros():       
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')  # Conectando ao banco de dados
    consulta = conn.cursor()  #cursor para para interagir com o  banco      
    consulta.execute('SELECT * FROM livros')       
    livros = consulta.fetchall()    #recupera os dados recolhidos pelo select do SQL, armazenando em livros
    conn.close()

    for row in livros:
        print(row)





# === ATUALIZAR O PREÇO DE UM NOVO LIVRO AQUI EMBAIXO =====

def atualizar_preco():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')
    consulta = conn.cursor()
    id_livro = input("Digite o ID do livro que deseja modificar o preço: ")
    novo_preco = float(input("Digite o novo preço do livro: "))
    consulta.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id_livro))

    conn.commit()

    print("Preço atualizado")

# === REMOVER UM LIVRO AQUI EMBAIXO =====

def remover_livro():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')  # Conectando ao banco de dados    
    consulta = conn.cursor()  #cursor para para interagir com o  banco   

    id = int(input('Digite o ID do livro para remover: '))

    consulta.execute('DELETE FROM livros WHERE id = ?',(id,))
    print(f'Livro removido com sucesso.')
    conn.commit()
    conn.close()    



# ===  BUSCAR UM LIVRO POR AUTOR AQUI EMBAIXO =====

def buscar_livros_nome_de_autor():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')  # Conectando ao banco de dados
    consulta = conn.cursor()    

    autor = input('Digite o nome do autor: ')

    consulta.execute('SELECT * FROM livros WHERE autor = ?', (autor,)) # o ? é onde o nome do autor vai estar
    livros = consulta.fetchall()  # Pega todos os resultados
    conn.close()

    if livros:
        for row in livros:
            print(row)  # Imprime a linha 
    else:
        print("Nenhum livro encontrado para o autor: ", autor)



# === EXPORTAR DADOS CSV AQUI EMBAIXO =====

def exportar_csv():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')  # Conectando ao banco de dados
    consulta = conn.cursor()
    consulta.execute("SELECT * FROM livros")
    colunas = [descricao[0] for descricao in consulta.description]

    with open("TrabalhoPythonLivraria/exports/dados.csv", "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(colunas)
        writer.writerows(consulta.fetchall())

    conn.close()


# === IMPORTAR DADOS CSV AQUI EMBAIXO =====

def importar_csv():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')
    consulta = conn.cursor()

    with open("TrabalhoPythonLivraria/exports/dados.csv", "r", newline="") as arquivo:
        reader = csv.reader(arquivo)
        next(reader)

        for row in reader:
            consulta.execute('''
                INSERT INTO livros (titulo, autor, ano_publicacao, preco)
                VALUES (?, ?, ?, ?)
''', (row[1], row[2], row[3], row[4]))
    
    conn.commit()
    conn.close()

# === FAZER BACKUP PARA O BD AQUI EMBAIXO =====

def backup():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')  # Conectando ao banco de dados
    consulta = conn.cursor()
    consulta.execute("SELECT * FROM livros")
    colunas = [descricao[0] for descricao in consulta.description]

    with open("TrabalhoPythonLivraria/backups/dados.csv", "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(colunas)
        writer.writerows(consulta.fetchall())

    conn.close()



# === MAIN =====

criar_pastas()  
create_db()  



while True:

    print()
    print()
    print("===== MENU LIVRARIA ===== ")
    print('1. Adicionar novo livro')
    print('2. Exibir todos os livros')
    print('3. Atualizar preço de um livro')
    print('4. Remover um livro')
    print('5. Buscar livros por autor')
    print('6. Exportar dados para CSV')
    print('7. Importar dados de CSV')
    print('8. Sair')
        
        
    opcao = input('Escolha uma opção: ')
        
    if opcao == '1':
        adicionar_livro()    
           
    elif opcao == '2':
        exibir_livros()
            
    elif opcao == '3':
        atualizar_preco()
        
    elif opcao == '4':
        remover_livro()
            
    elif opcao == '5':        
        buscar_livros_nome_de_autor()
            
    elif opcao == '6':
        exportar_csv()
            
    elif opcao == '7':
        importar_csv()
            
    elif opcao == '8':
        backup()      
        print('==== Saindo... ====')
        print('==== Volte Sempre ====')
        print()
        break

    else:
        print('Opção inválida.')