con_number = float(input())
unit_mesure_in = input()
unite_mesure_out = input()

if unit_mesure_in == "mm":
    if unite_mesure_out == "m":
       print(f'{con_number * 0.001:.3f}')
    elif unite_mesure_out == "cm":
        print(f'{con_number * 0.10:.3f}')

elif unit_mesure_in == "m":
    if unite_mesure_out =="mm":
        print(f'{con_number * 1000:.3f}')
    elif unite_mesure_out == "cm":
        print(f'{con_number * 100:.3f}')

elif unit_mesure_in == "cm":
    if unite_mesure_out == "m":
        print(f'{con_number * 0.01:.3f}')
    elif unite_mesure_out == "mm":
        print(f'{con_number * 10:.3f}')



