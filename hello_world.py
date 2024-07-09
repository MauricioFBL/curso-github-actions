import os


def hola_mundo(name):
    print(f'Que onda! {name}')
    
    
if __name__ == '__main__':
    try:
        name = os.environ['USERNAME']
        hola_mundo(name)
    except Exception as e:
        hola_mundo('desconocido')