import datetime
import sqlite3

MENU_FILE = 'menu.txt'
MENU_FILE_INSERT = 'menu-inserir.txt'
DB_FILE = 'db/university.db'
DATE_FORMAT = '%Y-%m-%d'


def check_option(option):
    """Todas opcoes do usuario que sao validas estao em: "valid_options"."""
    valid_options = {
        '0', '1', '1.1', '1.1.1', '1.2', '1.2.1', '1.3', '1.3.1', '2', '3'
    }
    if option in valid_options:
        return True
    else:
        return False
    # return True if option in valid_options else False


def load_file(file_path):
    with open(file_path) as fp:
        return fp.read()


def load_menu():
    return load_file(MENU_FILE)


def load_menu_insert():
    return load_file(MENU_FILE_INSERT)


def insert():
    option_mapping = {'1.1': insert_department}

    print(load_menu_insert())
    option = input('Escolha uma das opções acima: > ')
    if check_option(option):
        func = option_mapping[option]
        return_ = func()
    else:
        print(f'Opção "{option}" inválida.\n')

    return True


def insert_department():
    """Um departamento necessariamente precisa de:
        Nome
        Nome dos locais
        Gerente: buscar por nome
        Data de inicio: no momento da insercao
    """
    name = input('Nome do departamento: > ')
    locations = input('Locais do departamento (separados por espaço): ')
    locations = locations.split()
    rows = search_employees()
    ids = set()
    for id_, pnome, unome in rows:
        print('Id:', id_, 'Nome:', pnome, unome)
        ids.add(id_)

    if len(ids) < 1:
        print('Empregado não encontrado. Tente novamente.\n')
        return False

    id_ = input('Escolha um dos empregados acima pelo id: ')
    # Verifica se "id_" eh "numero" (isdigit)
    # e transforma o id_ para inteiro caso ele for digito.
    if id_.isdigit() and int(id_) in ids:
        start_date = datetime.datetime.today()
        start_date = start_date.strftime(DATE_FORMAT)
        print(start_date)

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute(
            f'INSERT INTO Departamento '
            f'(nome, gerente_data_inicio, gerente_id) '
            f"VALUES ('{name}', '{start_date}', {id_})")
        conn.commit()
        conn.close()
    else:
        print('Id invalido, tente inserir o departamento novamente.\n')
        return False


def search_employees():
    """Procura empregados pelo primeiro nome e ultimo nome e retorna seus ids."""
    employee_name = input('Insira o nome do empregado: > ')
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    rows = c.execute(  # SQL Query
        f'SELECT E.id, E.pnome, E.unome '
        f'FROM   Empregado E '
        f"WHERE  E.pnome LIKE '%{employee_name}%'"
        f"       OR E.unome LIKE '%{employee_name}%'")
    return rows


def exit():
    return False


def main():
    option_mapping = {'0': exit, '1': insert}

    menu_txt = load_menu()
    return_ = True
    while return_:
        print(menu_txt)
        option = input('Escolha uma das opções acima: > ')
        if check_option(option):
            func = option_mapping[option]
            return_ = func()
        else:
            print(f'Opção "{option}" inválida.\n')


if __name__ == '__main__':
    main()
