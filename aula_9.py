# arquivo = open('teste.txt', 'a')
# arquivo.write('\nTerceira linha!')
# arquivo.close()
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/Camil/Documents/BootCamp-DIO/Python/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([float(i) for i in notas]) / len(notas)
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
        
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Camil/Documents/BootCamp-DIO/Python')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Camil/Documents/BootCamp-DIO/PostgreSQL')

if __name__ == '__main__':
    #move_arquivo('media_notas.txt')
    #escrever_arquivo('Primeira linha. \n')
    aluno = '\nKatnis, 10, 9, 8.5, 6'
    atualizar_arquivo('notas.txt', aluno)
    media_notas('notas.txt')
    lista_media = media_notas('notas.txt')
    print(lista_media)
    #open('media_notas.txt', 'w')
    atualizar_arquivo('media_notas.txt', str(lista_media))