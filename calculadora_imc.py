# -*- coding: utf-8 -*-
"""Calculadora IMC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18Jfl4YaqWQO50RvuqBPLNzRYGjHuNqm8
"""

#Ramon Garcia Eduardo Isaias
val = True
while val:
  try:
    print("-----INGRESO DE DATOS-----")
    nombre = input("Ingresa tu Nombre(s)".strip())
    if not nombre:
      raise ValueError("Debes Ingresar un nombre")
    Apaterno = input("Ingresa tu Apellido paterno:  ".strip())
    if not Apaterno:
      raise ValueError("Debes Ingresar un apellido paterno")
    Amaterno = input("Ingresa tu Apellido materno:  ".strip())
    if not Amaterno:
      raise ValueError("Debes Ingresar un apellido materno")
    edad = int (input("Ingresa tu edad:  ").strip())
    if not edad:
      raise ValueError("Debes Ingresar una edad")
    if edad <=0:
      raise ValueError("debes poner una edad mayor a 0")
    Peso = float (input("Ingresa tu peso:  ").strip())
    if not Peso:
      raise ValueError("Debes Ingresar un peso")
    if Peso <=0:
      raise ValueError("debes poner un peso mayor a 0")
    Altura = float (input("Ingresa tu altura:  ").strip())
    if not Altura:
      raise ValueError("Debes Ingresar una altura")
    if Altura <=0:
      raise ValueError("debes poner una altura mayor a 0")
  #Calculo
    IMC = (Peso/(Altura*Altura))
    print("-----RESULTADOS-----")
    print(f"Nombre: ",nombre)
    print(f"Apellido Paterno: ",Apaterno)
    print(f"Apellido Materno: ",Amaterno)
    print(f"Edad: {edad} años")
    print(f"Peso: ",Peso)
    print(f"Altura: ",Altura)
    print(f"tu IMC: {IMC}")
    print("Final del programa")
    input("Presiona Enter para salir")
    val = False
  except ValueError as e:
    print(f"Error: {e}")
    print("Por favor, ingresa los datos nuevamente.")

