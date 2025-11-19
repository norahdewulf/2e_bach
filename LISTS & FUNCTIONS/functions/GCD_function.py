#grootste gemeenschappelijke deler van 2 integers(getallen)
def gcd(n1, n2):
    gcd = 1 #we beginnen bij 1 (initiele gcd)
    k = 2 #mogelijke gemeenschappelijke deler WANT een getal groter dan de inputs zijn geen goede delers

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k #gemeenschappelijke deler status updaten van het laatste geteste getal dat een deler kan zijn
        k += 1 #mogelijke delers

    print(gcd)

gcd(48, 64)