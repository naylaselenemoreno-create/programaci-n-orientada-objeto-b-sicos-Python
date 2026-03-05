from animal import animal 


class Gato(animal):

    peso = None
    __cantidad_patas =None


    #sobre escribir al contructor
    def __init__(self,nombre,edad,especie,color,peso):
        
        super().__init__(nombre,eda,especie,color)
        self.peso = peso 
    #gets sets =get> obtener y set =>insertaer
    def get_cantidad_patas(self):
          return self.__cantidad_patas   
    def set_cantidad_patas(self,cantidad_patas):
         self.__cantidad_patas = cantidad_patas
        
    def maullar():
        print(f"el gatito de nombre {self.nombre} de edad {self.edad} de color´{self.calor}y peso{self.peso} esta maullando")
    
    def mostrar_cantidad_patas(self):
        print(f"la cantidad de patas es{self.}")
    