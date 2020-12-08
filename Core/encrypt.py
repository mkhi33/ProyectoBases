class Encriptacion():
 
    def encrypt(self,txt):
        mensajeEncriptado = ''
        for letra in txt :
            x = self.convertirDecimal_a_Binario(ord(letra))
            mensajeEncriptado = mensajeEncriptado + str(x) + " "
 
        return mensajeEncriptado
 
    def convertirDecimal_a_Binario(self,decimal):
        decimalEncriptado = ''
        temp1 = decimal
        temp = 0
        i = 0
        while i < 8 :
            temp = temp1 % 2
            decimalEncriptado = decimalEncriptado + str(temp)
            if temp1==decimal :
                temp1 = decimal//2
            else :
                temp1 = temp1//2
 
            i = i + 1
 
 
        return (self.invertir(decimalEncriptado))
 
 
    def invertir(self,var):
        return var[::-1]
 
 
class Desencriptacion() :
 
    def Desencriptar(self,binario):
        x = binario.split()
        palabra = ''
        for i in range (len(x)) :
            palabra = palabra + chr(self.convertirBinario_a_Decimal(int(x[i])))
 
        return palabra
 
 
 
    def convertirBinario_a_Decimal(self,binario):
        decimal = 0
        i = 0
        for iterator in self.invertir(str(binario)) :
            if(int(iterator) == 1):
                decimal = decimal + 2 ** i
 
            i = i + 1
 
        return decimal
 
    def invertir(self,var):
        return var[::-1]
 
 
 
