import sqlite3

MENU_FILE = 'menu.txt'
MENU_FILE_DELETE = 'menu-excluir.txt'
MENU_FILE_INSERT = 'menu-inserir.txt'
MENU_FILE_UPDATE = 'menu-update.txt'
DB_FILE = 'db/university.db'
DATE_FORMAT = '%Y-%m-%d'

CONN = sqlite3.connect(DB_FILE)


def check_option(option, valid_options):
    return True if option in valid_options else False


def load_file(file_path):
    with open(file_path) as fp:
        return fp.read()


def load_menu():
    return load_file(MENU_FILE)


def load_menu_delete():
    return load_file(MENU_FILE_DELETE)


def load_menu_insert():
    return load_file(MENU_FILE_INSERT)


def load_menu_update():
    return load_file(MENU_FILE_UPDATE)


def insert():
    option_mapping = {'1.1': insert_department, '0': exit}
    print(load_menu_insert())
    option = input('Escolha uma das opções acima: ')

    return_ = False
    if check_option(option, option_mapping.keys()):
        func = option_mapping[option]
        return_ = func()
    else:
        print(f'Opção "{option}" inválida.\n')
    return return_


# def delete():
#     option_mapping = {'3.1': delete_department, '0': exit}
#     print(load_menu_delete())
#     option = input('Escolha uma das opções acima: ')
#
#     return_ = False
#     if check_option(option, option_mapping.keys()):
#         func = option_mapping[option]
#         return_ = func()
#     else:
#         print(f'Opção "{option}" inválida.\n')
#     return return_


def update():
    option_mapping = {'2.1': update_department, '0': exit}
    print(load_menu_update())
    option = input('Escolha uma das opções acima: ')

    return_ = False
    if check_option(option, option_mapping.keys()):
        func = option_mapping[option]
        return_ = func()
    else:
        print(f'Opção "{option}" inválida.\n')
    return return_


def delete_department_query(department_id):
    """Modelo de SQL parametrizado para excluir departamentos."""
    return (
        f'DELETE FROM Departamento '
        f'WHERE       id = {department_id}')


def insert_department_query(name, start_date, manager_id):
    """Modelo de SQL parametrizado para inserir departamento.

        - manager_id é optional
        - start_date é optional
    """
    manager_id = manager_id or 'NULL'  # Opcional
    # Eh preciso tomar cuidado com as aspas.
    start_date = f"'{start_date}'" if start_date else 'NULL'  # Opcional
    return (
        f'INSERT INTO Departamento '
        f'(nome, gerente_data_inicio, gerente_id) '
        f"VALUES ('{name}', {start_date}, {manager_id})")


def update_department_query(department_id, name, start_date, manager_id):
    """Modelo de SQL parametrizado para atualizar departamento

        - manager_id é optional
        - start_date é optional
    """
    manager_id = manager_id or 'NULL'  # Opcional
    # Eh preciso tomar cuidado com as aspas.
    print(f'"{start_date}"')
    start_date = f"'{start_date}'" if start_date else 'NULL'  # Opcional
    return (  # Cuidado com as 'aspas' na query. pois pode dar erro.
        f'UPDATE Departamento '
        f"SET    nome = '{name}', gerente_data_inicio = {start_date},"
        f'       gerente_id = {manager_id} '
        f"WHERE  id = {department_id}")


def read_department():
    name = input('Nome do departamento: ')
    start_date = input('Data de início do gerente: ')
    manager_id = input('Id do gerente: ')  # Pode ser campo em branco (opcional).
    print(f'\nNome do departamento: {name}')
    print(f'Data de início do gerente: {start_date}')
    print(f'Id do gerente: {manager_id}')
    return name, start_date, manager_id


def insert_department():
    """Um departamento necessariamente precisa de:
        Id: gerado automaticamente pelo banco.
        Nome
        Start date
        Manager id
    """
    name, start_date, manager_id = read_department()
    cursor = CONN.cursor()
    if manager_id:  # Checa se existe a string "manager_id".
        if employee_exists(manager_id):  # Checa se o "manager_id" existe no banco.
            query = insert_department_query(name, start_date, manager_id)
            cursor.execute(query)
            CONN.commit()  # Salva no banco.
            return True
        else:
            print(
                'Identificador do gerente invalido, '
                'tente inserir o departamento novamente.\n')
            return False
    else:  # Se nao existe manager_id, campo eh opcional.
        query = insert_department_query(name, start_date, manager_id)
        cursor.execute(query)
        CONN.commit()
        return True


def update_department():
    """Um departamento necessariamente precisa de:
        Id: gerado automaticamente pelo banco. Nao deve ser atualizado.
        Nome
        Start date
        Manager id
    """

    department_id = input('ID do departamento a ser atualizado: ')
    if not department_exists(department_id):
        print(
            'Identificador do departamento invalido, '
            'tente atualizar o departamento novamente.\n')

    name, start_date, manager_id = read_department()
    cursor = CONN.cursor()

    if manager_id:  # Checa se existe a string "manager_id".
        if employee_exists(manager_id):  # Checa se o "manager_id" existe no banco.
            query = update_department_query(department_id, name, start_date, manager_id)
            cursor.execute(query)
            CONN.commit()  # Salva no banco.
            return True
        else:
            print(
                'Identificador do gerente invalido, '
                'tente inserir o departamento novamente.\n')
            return False
    else:  # Se nao existe manager_id, campo eh opcional.
        query = update_department_query(department_id, name, start_date, manager_id)
        cursor.execute(query)
        CONN.commit()
        return True


def employee_exists(employee_id):
    """Procura apenas um empregado com o "employee_id".

    Retorna verdadeiro caso encontre; falso caso contrario.
    """
    cursor = CONN.cursor()
    cursor.execute(  # SQL Query
        f'SELECT E.id '
        f'FROM   Empregado E '
        f'WHERE  E.id = {employee_id}')
    # Bastar dar um "fetch", para vir uma linha.
    return True if cursor.fetchone() is not None else False


def department_exists(department_id):
    """Procura apenas um departamento com o "department_id".

    Retorna verdadeiro caso encontre; falso caso contrario.
    """
    cursor = CONN.cursor()
    cursor.execute(  # SQL Query
        f'SELECT D.id '
        f'FROM   Departamento D '
        f'WHERE  D.id = {department_id}')
    # Bastar dar um "fetch", para vir uma linha.
    return True if cursor.fetchone() is not None else False


def exit():
    return False


def main():
    # option_mapping = {'0': exit, '1': insert, '2': update, '3': delete}
    option_mapping = {'0': exit, '1': insert, '2': update}

    menu_txt = load_menu()
    return_ = True
    while return_:
        print(menu_txt)
        option = input('Escolha uma das opções acima: > ')
        if check_option(option, option_mapping.keys()):
            func = option_mapping[option]
            return_ = func()
        else:
            print(f'Opção "{option}" inválida.\n')


if __name__ == '__main__':
    main()
