# k neares neghbour
# coded by PR@$OON KU$#W@#@
while True:
    bodytemp = float(input('Enter the temp. of your body 🌡  \n '))

    if bodytemp > 42.5 or bodytemp < 35:
        while True:
            bodytemp = float(input('renter temp this temp. for human is not possible in °C'))
            if 42.5 > bodytemp > 35:
                break

    intervisit = int(input('Do you have any international visits? ✈️  \n write:-  \n  1 for YES \n 0 for NO \n'))
    if intervisit not in range(0, 2):
        while True:
            intervisit = int(input('Enter either 0 or 1'))
            if intervisit in range(0, 2):
                break

    Ssym = int(input(
        'How many symptoms you have out of these 🤧 \n Difficulty in breathing ,Chest pain, loss of speech or '
        'movement,\n fever ,dry cough \n'))
    if Ssym not in range(0, 7):
        while True:
            Ssym = int(input('Please enter a valid input only 6 symptoms are there'))
            if Ssym in range(0, 7):
                break
    Csym = int(input(
        'How many symptoms you have out of these  🤒\n Sore throat,loss of test 👅/smell ,headace, \n decoloration of '
        'finger  🖐 or toes👣,rashes,diarrhoea \n'))
    if Csym not in range(0, 7):
        while True:
            Csym = int(input('Please enter a valid input only 6 symptoms are there'))
            if Csym in range(0, 7):
                break

    IntCovid = int(
        input('Do you have any interaction with COVID+ patient ?🏥 \n write:-  \n  1 for YES \n 0 for NO \n'))
    if IntCovid not in range(0, 2):
        while True:
            IntCovid = int(input('Enter either 0 or 1'))
            if IntCovid in range(0, 2):
                break

    x1 = bodytemp
    x2 = intervisit
    x3 = Ssym
    x4 = Csym
    x5 = IntCovid

    dataset = [[37.0, 1, 4, 3, 0, 'highrisk'], [36.5, 0, 2, 2, 0, 'highrisk'], [36.5, 0, 0, 1, 1, 'lowrisk'],
               [37.2, 1, 2, 2, 0, 'moderate'], [36.8, 1, 5, 3, 1, 'highrisk'], [37.5, 0, 0, 0, 0, 'lowrisk'],
               [36.91, 1, 1, 0, 1, 'moderate'], [37.3, 0, 5, 3, 1, 'highrisk'], [36.3, 0, 2, 1, 1, 'lowrisk'],
               [37.1, 1, 4, 3, 1, 'highrisk'], [36.5, 0, 3, 2, 1, 'highrisk'], [37.3, 1, 1, 2, 1, 'moderate'],
               [37.0, 0, 0, 1, 1, 'lowrisk'], [36.4, 1, 0, 1, 0, 'lowrisk'], [37.6, 1, 3, 3, 0, 'highrisk'],
               [37.2, 0, 1, 0, 0, 'moderate'], [37.2, 0, 1, 0, 0, 'moderate'], [36.5, 0, 0, 1, 1, 'lowrisk'],
               [36.9, 1, 0, 0, 0, 'lowrisk'], [36.7, 0, 5, 1, 0, 'moderate'], [36.9, 1, 0, 0, 0, 'lowrisk'],
               [37.0, 1, 2, 0, 1, 'moderate'], [36.5, 0, 0, 1, 0, 'lowrisk'], [36.7, 1, 5, 6, 0, 'highrisk'],
               [37.1, 0, 2, 1, 1, 'moderate'], [36.39, 1, 1, 1, 0, 'moderate'], [37.2, 0, 0, 0, 1, 'lowrisk'],
               [37.3, 0, 2, 1, 0, 'moderate'], [37.5, 0, 1, 2, 0, 'moderate'], [36.8, 1, 0, 2, 0, 'lowrisk'],
               [36.7, 0, 4, 3, 0, 'highrisk'], [36.4, 0, 0, 1, 1, 'moderate'], [37.0, 0, 2, 3, 0, 'moderate']]
    values = []
    risk = []
    k = 0
    for a in range(len(dataset)):
        len = ((x1 - dataset[k][0]) ** 2 + (x2 - dataset[k][1]) ** 2 + (x3 - dataset[k][2]) ** 2 + (
                x4 - dataset[k][3]) ** 2 + (x5 - dataset[k][4]) ** 2) ** 0.5
        values = values + [len]
        risk = risk + [dataset[k][5]]
        k += 1
        list1 = values
    l = risk
    for i in range(k):
        key = l[i]
        key2 = list1[i]
        j = i - 1
        while j >= 0 and list1[j] > key2:
            list1[j + 1] = list1[j]
            l[j + 1] = l[j]
            j = j - 1
        else:
            l[j + 1] = key
            list1[j + 1] = key2
    n1 = 0
    n2 = 0.01
    n3 = 0.001
    print('\n \n \n')
    for w in range(0, 7):
        if l[w] == "lowrisk":
            n1 += 1
        if l[w] == 'moderate':
            n2 += 1
        if l[w] == 'highrisk':
            n3 += 1
    print('======================== RESULT =============================== \n')
    if n1 > n2 and n1 > n3:
        print('  low risk ,stay at home🏠 ')
    elif n2 > n1 and n2 > n3:
        print('  Moderate risk is there you must have a checkup')
    elif n3 > n1 and n3 > n2:
        print('  high risk urgent checkup required')
    print(
        '\n ===========================   ================================ \n \n  ©Prasoon kushwaha  2020 \n  All '
        'rights reserved \n   Department of Artificial Intelligence \n   & Machine Learning')
    x = input('\n \n  Do you want to continue...... progam👨‍💻 \n  type NO to exit a enter to continue.............')
    if x == 'no' or x == 'No' or x == 'NO' or x == 'nO':
        exit()
