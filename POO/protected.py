class MinhaClasse:
  def __init__(self):
    self._atributo_protected = 42;
  
  def _metodo_protected(self):
    print("Esse método é protected!");

objeto = MinhaClasse();
objeto._metodo_protected();