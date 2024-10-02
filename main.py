import sqlite3
import os


# === CRIAR ESTRUTURA DE PASTAS ===
def criar_pastas():
    os.makedirs('TrabalhoPythonLivraria/data', exist_ok=True)
    os.makedirs('TrabalhoPythonLivraria/backups', exist_ok=True)
    os.makedirs('TrabalhoPythonLivraria/exports', exist_ok=True)





# === BD AQUI EM BAIXO =====

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





# === ADICIONAR UM NOVO LIVRO AQUI EM BAIXO =====

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





# === EXIBIR TODOS OS LIVROS AQUI EM BAIXO =====

def exibir_livros():       
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')  # Conectando ao banco de dados
    consulta = conn.cursor()  #cursor para para interagir com o  banco      
    consulta.execute('SELECT * FROM livros')       
    livros = consulta.fetchall()    #recupera os dados recolhidos pelo select do SQL, armazenando em livros
    conn.close()

    for row in livros:
        print(row)





# === ATUALIZAR O PREÇO DE UM NOVO LIVRO AQUI EM BAIXO =====



# === REMOVER UM LIVRO AQUI EM BAIXO =====

def remorver_livro():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')  # Conectando ao banco de dados    
    consulta = conn.cursor()  #cursor para para interagir com o  banco   

    id = int(input('Digite o ID do livro para remover: '))

    consulta.execute('DELETE FROM livros WHERE id = ?',(id,))
    print(f'Livro removido com sucesso.')
    conn.commit()
    conn.close()    



# ===  BUSCAR UM LIVRO POR AUTOR AQUI EM BAIXO =====

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



# === EXPORTAR DADOS CSV AQUI EM BAIXO =====



# === IMPORTAR DADOS CSV AQUI EM BAIXO =====



# === FAZER BACKUP PARA O BDAQUI EM BAIXO =====




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
    print('8. Fazer backup do banco de dados')
    print('9. Sair')
        
        
    opcao = input('Escolha uma opção: ')
        
    if opcao == '1':
        adicionar_livro()    
           
    elif opcao == '2':
        exibir_livros()
            
    # elif opcao == '3':
        
    elif opcao == '4':
        remorver_livro()
            
    elif opcao == '5':        
        buscar_livros_nome_de_autor()
            
    # elif opcao == '6':
            
    # elif opcao == '7':
            
    # elif opcao == '8':
            
    elif opcao == '9':           
        print('==== Saindo... ====')
        print('==== Volte Sempre ====')
        print()
        break

    else:
        print('Opção inválida.')