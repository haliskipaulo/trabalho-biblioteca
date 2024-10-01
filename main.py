import sqlite3

# === BD AQUI EM BAIXO =====

def create_db():
    conn = sqlite3.connect('TrabalhoPythonLivraria/data/livraria.db')
    consulta = conn.cursor()
    consulta.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER,
            preco REAL
        )
    ''')
    conn.commit()
    conn.close()


# === ADICIONAR UM NOVO LIVRO AQUI EM BAIXO =====



# === EXIBIR TODOS OS LIVROS AQUI EM BAIXO =====



# === ATUALIZAR O PREÇO DE UM NOVO LIVRO AQUI EM BAIXO =====



# === REMOVER UM NOVO LIVRO AQUI EM BAIXO =====



# ===  BUSCAR UM NOVO LIVRO POR AUTOR AQUI EM BAIXO =====



# === EXPORTAR DADOS CSV AQUI EM BAIXO =====



# === IMPORTAR DADOS CSV AQUI EM BAIXO =====



# === FAZER BACKUP PARA O BDAQUI EM BAIXO =====






while True:
    
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
        
    # if opcao == '1':
           
    # elif opcao == '2':
            
    # elif opcao == '3':
        
    # elif opcao == '4':
            
    # elif opcao == '5':
            
    # elif opcao == '6':
            
    # elif opcao == '7':
            
    # elif opcao == '8':
            
    # elif opcao == '9':
            
    #     break 
    # else:
    #     print('Opção inválida.')