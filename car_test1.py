# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 22:48:44 2018

@author: Pablo Medina Aizaga

This class has unit tests for car class

"""

import unittest


class PrimesTestCase(unittest.TestCase):
    """Tests for `car.py`."""

    def test_if_is_disponibilidad(self):
        from car import car 
        """
        Disponibiliad Unit test 
        cheking when a vehicle is able to be on the road
        
        
        """
        placa = ["AAA-0001", "AAA-0002", "AAA-0003", "AAA-0004", "AAA-0005", \
        "AAA-0006", "AAA-0007", "AAA-0008", "AAA-0009", "AAA-0000"]
        
        fecha = ["20180723","20180724", "20180725","20180726","20180727","20180728", "20180729"]
        hora = ["0600", "1200", "2000"]
        
        for i in placa:
            for j in fecha:
                for k in hora:
                    car1 = car(i, j, k)
                    self.assertTrue(car1.disponibilidad()) 
    def test_if_is_not_disponibilidad(self):
        from car import car 
        """
        Disponibiliad Unit test 
        cheking when a vehicle is not able to be on the road
        
        
        """
        placa = ["AAA-0001", "AAA-0002", "AAA-0003", "AAA-0004", "AAA-0005", \
        "AAA-0006", "AAA-0007", "AAA-0008", "AAA-0009", "AAA-0000"]
        
        fecha = ["20180723","20180724", "20180725","20180726","20180727","20180728", "20180729"]
        hora = ["0700", "0930", "1600","1930"]
        
        for i in placa[0:2]:
            for j in fecha[0:1]:
                for k in hora:
                    car1 = car(i, j, k)
                    self.assertFalse(car1.disponibilidad()) 
                    
        for i in placa[2:4]:
            for j in fecha[1:2]:
                for k in hora:
                    car1 = car(i, j, k)
                    self.assertFalse(car1.disponibilidad()) 
                    
        for i in placa[4:6]:
            for j in fecha[2:3]:
                for k in hora:
                    car1 = car(i, j, k)
                    self.assertFalse(car1.disponibilidad()) 
                    
        for i in placa[6:8]:
            for j in fecha[3:4]:
                for k in hora:
                    car1 = car(i, j, k)
                    self.assertFalse(car1.disponibilidad()) 
                
        for i in placa[8:]:
            for j in fecha[4:5]:
                for k in hora:
                    car1 = car(i, j, k)
                    self.assertFalse(car1.disponibilidad())         
        
    def test_if_is_correct_isPlateNumCorr(self):
        from car import car 
        """
        isPlateNumCor Unit test 
        cheking if the method isPlateNumCor actually works when a  wrong plate number is given
        
        """
        
        placa = ["0AA-0001", "AAA-0a02", "AAA-00030", "AAA-004", "AA-0005"]
        
        for i in placa:
                    car1 = car(i, None, None)
                    self.assertFalse(car1.isPlateNumCorr()) 
    
    def test_if_is_correct_isDateCorr(self):
        from car import car 
        """
        isDateCorr Unit test 
        cheking if the method isDatemCorr actually works when a  wrong date is given
        
        """
        
        fecha = ["2018714", "14072018", "20194501", "20183108", "201908080"]
        
        for i in fecha:
                    car1 = car(None, i, None)
                    self.assertFalse(car1.isDateCorr()) 
    
    def test_if_is_correct_isTimeCorr(self):
        from car import car 
        """
        isTimeCorr Unit test 
        cheking if the method isDatemCorr actually works when a  wrong time is given
        
        """
        
        hora = ["700", "2500", "a01901", "082100"]
        
        for i in hora:
                    car1 = car(None, None, i)
                    self.assertFalse(car1.isTimeCorr()) 

if __name__ == '__main__':
    unittest.main()