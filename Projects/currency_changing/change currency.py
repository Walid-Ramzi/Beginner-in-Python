def main():
    DA = 'da'
    USD = 'usd'
    EUR = 'eur'
    a = input('what do you want to change(§§§/currency): ').split('/')
    print(a)
    b = str(input('To : '))
    if a[1] == DA :
        if b == EUR:
            EUR = 0.002 * float(a[0])
            print('your sarf is', EUR ,'eur')
        elif b == USD:
             USD = 0.0016 * float(a[0])
             print('your sarf is', USD, 'dollar')
    elif a[1] == EUR :
        if b == DA :
             DA = 200 * float(a[0])
             print('your sarf is', DA, 'dinnar')
        elif b == USD:
            USD = 1.5*float(a[0])
            print('your sarf is', USD, 'dollar')
    elif a[1] == USD:
        if b == DA :
             DA = 160 * float(a[0])
             print('your sarf is', DA, 'dinnar')
        elif b == EUR :
            EUR =  float(a[0])/1.5
            print('your sarf is', EUR, 'eur')

while True:
    main()
    print()

