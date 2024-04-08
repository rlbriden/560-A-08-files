import sys

while True:
    file_var = input('''
    What file would you like to search for?:
    a) classical pieces file
    b) national parks file
    x) to exit
    ''')
    if file_var == 'x':
        sys.exit()
    elif file_var == 'a':
        file_var = 'classical_pieces.csv'
    elif file_var == 'b':
        file_var = 'national_parks.csv'
    else:
        print('Invalid option. Please select a, b, or x')
        continue

    search_var = input(f'Enter the search term for {file_var} file: ')
    search_var = search_var.title()

    def find(file_var, search_var):
        with open(file_var, 'r') as file:
            content = file.read()

        if search_var in content:
            print(f'Your search term {search_var} exists in the {file_var} file!')
            see_entries = input('Would you like to see the entries (y or n)?')

            if see_entries.lower() == 'y':
                print(f'Here are all of the entries with the term {search_var}: ')
                with open(file_var, 'r') as file:
                    for line in file:
                        if search_var in line:
                            print(line.strip())

            elif see_entries.lower() == 'n':
                print('Goodbye')
                sys.exit()

            else:
                print('Invalid option. Please enter y or n.')
                
        else:
            print(f'{search_var} does not exist in {file_var}')
            
    find(file_var, search_var)
                            