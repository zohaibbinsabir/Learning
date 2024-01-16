print("----- Movie Discount -----")
movies = ["Avengers", "Spiderman", "Ironman", "Captain America", "Thor"]
print("Movies: ", movies)
def discount(movie):
    for i in range(len(movies)):
        if movie == movies[i]:
            if (i % 2 == 0):
                return 10
            else:
                return 5
    return 0

movie = input("Enter movie name: ")
print("Discount: ", discount(movie), "%")
    