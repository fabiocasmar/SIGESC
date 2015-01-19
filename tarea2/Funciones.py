# -*- coding: utf-8 -*
'''
Created on 18/1/2015

@author: daniel
'''
'''
Created on Jan 18, 2015

@author: Hector Goncalves
@author: Daniel Zeait
'''
from datetime import datetime#Libreria que que maneja fechas y horas 

if __name__ == '__main__':
    pass

#Lista de Fechas de inicio de la reservación
fechaIniRes = "2015 03 23 18:03"    

#Lista de Fechas en las que se termina la reservación
fechaFinRes= "2015 03 23 18:20"    
#172.8 +12.2+16.6+4.2
#73.2 99.6
#Diccionario con las tarifas asociadas a etapa diurna o nocturna
tarifa_diurna = 6.10
tarifa_nocturna = 8.30
fraccion_menor30=2.50


#funcion que determina la tarifa a ser usada dependiendo la hora de entrada
def hallarTarifa(horaI):
    if horaI.hour < 18:
        tarifa = tarifa_diurna
    else:
        tarifa = tarifa_nocturna
    return tarifa

#funcion que calcula el monto a pagar por una reservacion de estacionamiento
def calcularMonto(fechaInicio, fechaFin):
    
    #convertimos los str en fechas
    horaIni = datetime.strptime(fechaInicio, "%Y %m %d %H:%M")
    horaFin = datetime.strptime(fechaFin, "%Y %m %d %H:%M")    
    
    #calculamos la tarifa a usar
    tarifa = hallarTarifa(horaIni)
    
    #en caso de que la reserva dure mas de un dia
    total_dias = horaFin.day - horaIni.day
    monto_dias = (total_dias) * ((12*tarifa_diurna) + (12*tarifa_nocturna))
    
    #calculamos el monto a pagar por horas
    total_horas = horaFin.hour - horaIni.hour
    monto_horas = total_horas * tarifa
    
    #calculamos el monto a pagar por fracciones de hora
    total_min = abs(horaFin.minute - horaIni.minute)

    if total_min < 30:
        fraccion = fraccion_menor30
    else:
        fraccion = tarifa
    
    #en caso de manejar dos tarifas por un mismo dia
    if horaIni.hour < 18 and horaFin.hour > 18:
        monto1 = (18 - horaIni.hour) * tarifa_diurna
        monto2 = (horaFin.hour-18) * tarifa_nocturna
      
        monto_total = monto_dias + monto1 + monto2 + fraccion
    
    else:   
        monto_total = monto_dias + monto_horas + fraccion
    
    return monto_total
   
    
monto = calcularMonto(fechaIniRes,fechaFinRes)
print("El monto a pagar es:")
print(monto)




    