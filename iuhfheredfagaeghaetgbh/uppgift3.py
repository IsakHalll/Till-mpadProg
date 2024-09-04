import os
import csv


products = []

class Product:
     def __init__(self,id,name,desc,price,quantity):
          self.product(self)
          self.id = id
          self.name = name 
          self.desc = desc
          self.price = price
          self.quantity = quantity
          
     def check_inventory(self):
          inventory = f"{self.id, self.name, self.desc, self.price, self.quantity}"
          

          

     def add_item(self):
          pass
     def remove(self):
          pass
          
    #TODO: Skapa check_inventory (visa produkter)
    #TODO: Skapa add_item-metod för produkter
    #TODO: Skapa remove-metod för produkter
    #TODO: Skapa sparfunktion
    #TODO: (Frivillig) Skapa en metod som visar mest sålda produkt