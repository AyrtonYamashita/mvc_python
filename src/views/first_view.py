def introduction_page():
    message = '''
        Sistema cadastral
        
        * Cadastrar usuario - 1
        * Buscar usuario - 2
        * Sair - 3
    '''

    print(message)
    command = input('Comando: ')
    return command