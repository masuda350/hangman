print('{movie} (dir. {director}) came out in {year}'.format(movie=input(),
                                                            director=input(),
                                                            year=input()))

# Another solution 1
movie, director, year = [input() for _ in range(3)]

print(f'{movie} (dir. {director}) came out in {year}')


# Another solution 2
def printer(title, director_name, year_out):
    print(f'{title} (dir. {director_name}) came out in {year_out}')


printer(input(), input(), input())
