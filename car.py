# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:26:15 2018

@author: Pablo Medina Aizaga
"""

class Car:
    #this is the constructor for the class. It is called whenever a Car object is
    #created
   
    
    def __init__(self, plateNum, wDate, wTime):
        self.plateNum = plateNum
        self.wDate = wDate
        self.wTime = wTime
        self.isPlateOk = True
        self.isDateOk = True
        self.isTimeOk = True
    #accessor method which returns plate number of car
    def placa(self):
        return self.plateNum
    #accessor method which returns the date given by user
    def fecha(self):  
        from datetime import date
        
        wYear = self.wDate[0:4]
        wMonth = self.wDate[4:6]
        wDay = self.wDate[6:]
        wIsoDate = date(int(wYear),int(wMonth),int(wDay)).isoformat()
        
        return wIsoDate
   #accessor method which returns the time given by user
    def hora(self):
        from datetime import time
        
        wHour = self.wTime[0:2]
        wMinute = self.wTime[2:]
        wIsoTime = time(int(wHour),int(wMinute)).isoformat()
        
        return wIsoTime
    
    #accessor method which evaluate if the plate number is correct
    def isPlateNumCorr(self):
        if len(self.plateNum)!=8:
            self.isPlateOk = False            
                
        elif self.plateNum[3]!='-':
            self.isPlateOk = False
        
        for i in self.plateNum[0:3]:
            if i.isalpha()==False:
                self.isPlateOk = False
                break        
        try:
            int(self.plateNum[4:])
        except  ValueError:
            self.isPlateOk = False
        
        return self.isPlateOk    
       
    #accessor method which evaluate if the date is correct
    def isDateCorr(self):
        from datetime import date
        
        if len(self.wDate)>8 or len(self.wDate)<8:
            self.isDateOk = False
        
        try:
            int(self.wDate)
            
        except ValueError:            
            self.isDateOk = False            
              
        try: 
            date(int(self.wDate[0:4]),int(self.wDate[4:6]),int(self.wDate[6:]))
            
        except ValueError:
            self.isDateOk = False
    
        return self.isDateOk
    
    #accessor method which evaluate is the time is correct
    def isTimeCorr(self):
        from datetime import time
        
        if len(self.wTime)>4 or len(self.wTime)<4:
            self.isTimeOk = False
        
        try:
            int(self.wTime)
            
        except ValueError:            
            self.isTimeOk = False            
              
        try: 
            time(int(self.wTime[0:2]),int(self.wTime[2:]))
            
        except ValueError:
            self.isTimeOk = False
    
        return self.isTimeOk
    
    #this accessor method return whether or not a car is able to be on the road
    def disponibilidad(self):        
        from datetime import date
        
        wTime = int(self.wTime)
        wYear = self.wDate[0:4]
        wMonth = self.wDate[4:6]
        wDay = self.wDate[6:]
        wDate = date(int(wYear),int(wMonth),int(wDay))
        plateNum = self.plateNum[-4:]
        disponible = True
        
        if wDate.weekday()==0 and (int(plateNum[3])==1 or int(plateNum[3])==2) and ((700 <= wTime <= 930) or (1600 <= wTime <= 1930)):
            disponible = False    
            
        elif wDate.weekday()==1 and (int(plateNum[3])==3 or int(plateNum[3])==4) and ((700 <= wTime <= 930) or (1600 <= wTime <= 1930)):
            disponible = False
        
        elif wDate.weekday()==2 and (int(plateNum[3])==5 or int(plateNum[3])==6) and ((700 <= wTime <= 930) or (1600 <= wTime <= 1930)):
            disponible = False
        
        elif wDate.weekday()==3 and (int(plateNum[3])==7 or int(plateNum[3])==8) and ((700 <= wTime <= 930) or (1600 <= wTime <= 1930)):
            disponible = False
        
        elif wDate.weekday()==4 and (int(plateNum[3])==9 or int(plateNum[3])==0) and ((700 <= wTime <= 930) or (1600 <= wTime <= 1930)):
            disponible = False 
        
        return disponible
        
    
def main():
    
    while True:
        print("Ingrese el número de placa de su vehículo Ej. PLU-0778:", end=' ')
        placa = str(input())     
        car1 = Car(placa,None,None)   
        if car1.isPlateNumCorr()==True:
            break
        else:
            print("Placa Incorrecta, Intente de nuevo", end = ' ')
            
    while True:
        print('Ingrese la fecha AñoMesDía Ej. 20180503:', end = ' ')
        fecha = str(input())
        car1 = Car(placa,fecha,None)
        if car1.isDateCorr()==True:
            break
        else:
            print("Fecha incorrecta, Intente de nuevo", end = ' ')
            
    while True:
        print("Ingrese la hora de circulación en HHMM Ej. 1530:", end = ' ')
        hora = str(input())
        car1 = Car(placa,fecha,hora)
        if car1.isTimeCorr()==True:
            break
        else:
            print("Hora incorrecta, Intente de nuevo", end = ' ')
    
    print("")
    
    car1 = Car(placa, fecha, hora)
    print(car1.placa())
    print(car1.fecha())
    print(car1.hora())
    if car1.disponibilidad():
        print("El vehículo " + str(car1.placa()) + " puede circular en la fecha " + str(car1.fecha()) + " y hora " + str(car1.hora()))
    else:
        print("El vehículo " + str(car1.placa()) + " no puede circular en la fecha " + str(car1.fecha()) +  " y hora " + str(car1.hora()))
if __name__ == "__main__":
    main()
    
    
    