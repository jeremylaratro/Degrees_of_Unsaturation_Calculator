#### Degrees of Unsaturation Calculator ####
def dou():
    print("Do you have the bond-line structure or molecular formula?")
    ans = input("[a] = bond-line, [b] = formula"
          "\n here: ")
    if ans == 'a':
        print("Enter the number of rings and pi bonds")
        ring = int(input("Rings: \n"))
        pi = int(input("Pi bonds: \n"))
        degrees_of_unsaturation_bond = (ring+pi)
        print("Degrees of Unsaturation: " + str(degrees_of_unsaturation_bond))
    if ans == 'b':
        print("Enter the number of Carbons, Hydrogens, Nitrogens, and Halogens")
        c = int(input("\nCarbons: "))
        h = int(input("\nHydrogens: "))
        n = int(input("\nNitrogen: "))
        x = int(input("\nHalogens: "))
        degree_of_unsaturation_formula = int(((((2*c)+2)+n)-h-x)/2)
        print("Degrees of Unsaturation: " + str(degree_of_unsaturation_formula))
dou()