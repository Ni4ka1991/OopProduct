#!/usr/bin/env python3

#  MAIN MODULE #####
from os import system
from data import *


class Product:
 pass

def newProduct( dictProduct, item ):
    product = Product()
    product.name     = menu[item]["name"]
    product.price    = menu[item]["price"]
    product.quantity = menu[item]["quantity"]
    return product

def printProduct( product ):
    print( "#"*10 )
    print( product.name, product.price, product.quantity )
    print( "#"*10 )


system( "clear" )

food1 = newProduct( menu, 0 )
food2 = newProduct( menu, 1 )


printProduct( food1 )
printProduct( food2 )

def compareProducts(prod1, prod2 ):
    if prod1.price != prod2.price:
       cheap = min( prod1.price, prod2.price )
       print( "Cheaper dish >>> ", prod1.name ) if cheap == prod1.price else print( "Cheaper dish >>> ", prod2.name )

    else:
       print("The selected dishes have the same price.")

compareProducts( food1, food2 )

