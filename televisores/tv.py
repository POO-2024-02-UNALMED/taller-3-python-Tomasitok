class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        
        TV._numTV += 1

    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        self.setCanal(self._canal + 1)

    def canalDown(self):
        self.setCanal(self._canal - 1)

    def volumenUp(self):
        self.setVolumen(self._volumen + 1)

    def volumenDown(self):
        self.setVolumen(self._volumen - 1)

    def setMarca(self, marca):
        self._marca = marca
    
    def setCanal(self, canal):
        if self._estado and 1 <= canal <= 120:
            self._canal = canal

    def setPrecio(self, precio):
        self._precio = precio

    def setVolumen(self, volumen):
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen

    def setControl(self, control):
        self._control = control

    def getMarca(self):
        return self._marca
    
    def getCanal(self):
        return self._canal
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self) -> int:
        return self._volumen

    def getControl(self):
        return self._control
    
    def getEstado(self):
        return self._estado