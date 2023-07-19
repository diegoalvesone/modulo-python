class MinhaClasse:
  def __init__(self):
    self.__atributo_private = 42;
  
  def __metodo_private(self):
    print("Esse método é private!");
  
  def acessarMetodoPrivate(self):
    self.__metodo_private();

objeto = MinhaClasse();
objeto.__metodo_private(); #Acesso NÃO permitido

objeto.acessarMetodoPrivate();
