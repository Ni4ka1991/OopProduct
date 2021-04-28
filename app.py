#!/usr/bin/env python3

#  MAIN MODULE #####
from os import system
from data import *


class Product:
 pass

def newProduct( dictProduct ):
    product = Product()
    product.name     = dictProduct["name"]
    product.price    = dictProduct["price"]
    product.quantity = dictProduct["quantity"]
    return product

def printProduct( product ):
    print( "#"*10 )
    print( product.name, product.price, product.quantity )
    print( "#"*10 )


system( "clear" )

food1 = newProduct( first_dish )
food2 = newProduct( second_dish )


printProduct( food1 )
printProduct( food2 )

def compareProducts(prod1, prod2 ):
    if prod1.price != prod2.price:
       cheap = min( prod1.price, prod2.price )
       print( "Cheaper dish >>> ", prod1.name ) if cheap == prod1.price else print( "Cheaper dish >>> ", prod2.name )

    else:
       print("The selected dishes have the same price.")

compareProducts( food1, food2 )

