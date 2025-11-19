print("Find all prime numbers <= n, enter n:")
input = int(input())

#n is het getal dat we aan het checken zijn of het een priemgetal is (behoort tot outer loop)
n = 2       #priemroutine - geheel getal groter dan 1 [zie opgave]
ja = 1      #opmaakroutine

print("The prime numbers are: ")

#outer loop
#while true => while loop wordt uitgevoerd
while n <= input:
    getal = n    #getal is de variabele die w gecheckt op priem char
    m = 2        #hulpvar. bij de controle deling met rest
    x = 0        #hulpvar. die gevuld wordt indien een getal meerdere gehele delers heeft [w we niet willen]

    #STEP1 - controle op priem characteristic
    count = 0    #count hoort bij de inner loop
    while count < getal and m < getal:
        if getal % m == 0: #als true wil dit zeggen dat het getal andere gehele delers heeft dan zichzelf => g priemgetal
            x += 1
        m += 1
        count += 1

    #STEP2 - opmaak wanneer getal n een priem char heeft -
    #        als x na step1 nog steeds = 0 wil dit zeggen dat het geen andere gehele deler
    #        heeft dan zichzelf => het is een priemgetal
    if x == 0:
        if ja % 10 != 0 and ja != 0:
            print(getal, end = " ")    #zorgt voor printen op zelfde lijn
        else:
            print(getal)
        ja += 1 #ja gaat omhoog iedere keer een priemgetal geprint wordt

    #STEP3 - controle beindigd [outer loop] en nu volgend getal checken
    n += 1

#eerste print zorgt ervoor dat de laatste print op een ander lijntje komt te staan dan de getallen die we al geprint hebben
print()
print(str(ja - 1) + " prime(s) less than or equal to " + str(input))