class Lampara:
    Estados = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, esta_encendida):
        self.esta_encendida = esta_encendida

    def muestra_lampara(self):
        if self.esta_encendida:
            print(self.Estados[0])
        else:
            print(self.Estados[1])

    def encender(self):
        self.esta_encendida = True
        self.muestra_lampara()

    def apagar(self):
        self.esta_encendida = False
        self.muestra_lampara()      


def main(): 
  lamp = Lampara(esta_encendida=False)
  menu = '''MENU:
  0 > Apagar Lampara
  1 > Encender lampara
  x > Salir'''
  while True:
    print(menu)
    opcion=input("Que opcion desea: ")
    if opcion=='0':
      lamp.apagar()
    elif opcion=='1':
      lamp.encender()
    else:
      break

  
if __name__ == "__main__":
    main()