import pandas as pd

#reading items file, which contains information about the movies
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols, encoding='latin-1')

index_items = items.set_index('movie id')

#print(items[items['movie title'].str.contains('Toy')])
#print(items["movie title"])

movie = input('Type a movie title:\n')

if items['movie title'].str.contains(movie).any():
    print(items[items['movie title'].str.contains(movie)])
    print('Here it goes a recommendation...')

    option = int(input('Do you want to add another movie in the list?\n 1 - Yes\n 2 - No\n'))

    while option != 2:

        if option == 1:
            movie = input('Please type another movie title:\n')
            print(items[items['movie title'].str.contains(movie)])
            print('Here it goes a recommendation...')
            rate_recomm = int(input("Do you like this movie?\n 1 - Yes\n 2 - No\n 3 - I don't know"))

            if rate_recomm == 1:
                print('Here it goes a new recommendation...')
            elif rate_recomm == 2:
                print('Here it goes a new recommendation...')
            elif rate_recomm == 3:
                print('...')
            else:
                print('Invalid option. Please choose a valid option:\n')

            option = int(input('Do you want to add another movie in the list?\n 1 - Yes\n 2 - No\n'))

        elif option == 2:
            print('Here it goes a recommendation...')
            break
        else:
            print('Invalid option. Please choose a valid option:\n')

else:
    print('Sorry, we couldn\'t find your movie. Please choose another one:\n')
