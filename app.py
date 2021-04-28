#!/usr/bin/env python3

#  MAIN MODULE #####
from os import system


class Product:
 pass

def newProduct( name, price, quantity ):
    product = Product()
    product.name     = name
    product.price    = price
    product.quantity = quantity
    return product

def printProduct( product ):
    print( "#"*10 )
    print( product.name, product.price, product.quantity )
    print( "#"*10 )

first_dish  = newProduct( "soup", 25, 3 )
second_dish = newProduct( "salad", 19, 3 )

system( "clear" )

printProduct( first_dish )
printProduct( second_dish )

def compareProducts(prod1, prod2 ):
    if prod1.price != prod2.price:
       cheap = min( prod1.price, prod2.price )
       print( "Cheaper dish >>> ", prod1.name ) if cheap == prod1.price else print( "Cheaper dish >>> ", prod2.name )

    else:
       print("The selected dishes have the same price.")

compareProducts( first_dish, second_dish )

