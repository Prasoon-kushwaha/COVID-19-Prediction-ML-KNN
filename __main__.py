# k neares neghbour
# coded by PR@$OON KU$#W@#@

def calculate_distance(x1, x2, x3, x4, x5, dataset):
    distances = []
    for data in dataset:
        dist = ((x1 - data[0]) ** 2 + (x2 - data[1]) ** 2 + (x3 - data[2]) ** 2 +
                (x4 - data[3]) ** 2 + (x5 - data[4]) ** 2) ** 0.5
        distances.append(dist)
    return distances


def get_input(prompt, valid_range=None):
    while True:
        try:
            user_input = int(input(prompt))
            if valid_range is not None and user_input not in valid_range:
                raise ValueError
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")


def main():
    dataset =  [[37.0, 1, 4, 3, 0, 'highrisk'], [36.5, 0, 2, 2, 0, 'highrisk'], [36.5, 0, 0, 1, 1, 'lowrisk'],
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
 

    while True:
        bodytemp = get_input('Enter the temperature of your body 🌡  ')
        if not (35 <= bodytemp <= 42.5):
            print('Invalid temperature. Please enter a valid body temperature (35°C to 42.5°C).')
            continue

        intervisit = get_input('Do you have any international visits? ✈️  (1 for YES, 0 for NO): ', [0, 1])

        Ssym = get_input('How many symptoms do you have out of the following? 🤧 \n'
                         '1. Difficulty in breathing\n2. Chest pain\n3. Loss of speech or movement\n'
                         '4. Fever\n5. Dry cough\n', range(0, 6))

        Csym = get_input('How many symptoms do you have out of the following? 🤒 \n'
                         '1. Sore throat\n2. Loss of taste/smell\n3. Headache\n4. Discoloration of finger or toes\n'
                         '5. Rashes\n6. Diarrhea\n', range(0, 6))

        IntCovid = get_input('Have you had any interaction with a COVID+ patient? 🏥  (1 for YES, 0 for NO): ', [0, 1])

        distances = calculate_distance(bodytemp, intervisit, Ssym, Csym, IntCovid, dataset)
        sorted_distances, sorted_risk = zip(*sorted(zip(distances, [data[5] for data in dataset])))

        n1 = sorted_risk[:7].count('lowrisk')
        n2 = sorted_risk[:7].count('moderate')
        n3 = sorted_risk[:7].count('highrisk')

        print('\n======================== RESULT ===============================\n')
        if n1 > n2 and n1 > n3:
            print('Low risk, stay at home 🏠')
        elif n2 > n1 and n2 > n3:
            print('Moderate risk is there, you must have a checkup')
        elif n3 > n1 and n3 > n2:
            print('High risk, urgent checkup required')

        print('\n=========================== ================================\n')
        x = input('\nDo you want to continue the program? (Type "NO" to exit, press Enter to continue): ')
        if x.strip().lower() == 'no':
            break


if __name__ == "__main__":
    main()

