def gasolina(marca,precio):
    print(f"Usted selecciono {marca}. El precio es de {precio}")
    Litros=int(input("Cuantos LITROS desea poner: "))
    precio_litro=Litros*precio
    print(f"total a pagar {round(precio_litro,3)}")
    print("Compra exitosa.")

print("""
1.- Magna: $22.08
2.- Premium $24.19
3.- Diesel $22.80
4.- Salir.
    """)
i=1
while i<=3:
        
    opcion=int(input(("Selecciona Una opcion por favor: ")))
    if opcion==1:
        gasolina
    elif opcion==2:
        gasolina("Premium",24.19)
    elif opcion==3:
        gasolina("Diesel",22.80)
    elif opcion==4:
        print("Usted salio con exito de la compra.")
        break
    else:
        print(f"Opcion Invalida. Repita de nuevo por favor. Intentos {i}")
    i+=1