####################################################
#####################################################
#####################################################Kommivoyahor evolutioni method
######################################################
import numpy
import random
import itertools
cities = [1, 2, 3, 4, 5]
citycount = 5
routecount = (citycount * (citycount - 1)) / 2
routes = [4, 4, 7, 3, 2, 3, 5, 2, 3, 6]
tours = [['1-2', 4], ['1-3', 4], ['1-4', 7], ['1-5', 3], ['2-3', 2], ['2-4', 3], ['2-5', 5], ['3-4', 2], ['3-5', 3],
         ['4-5', 6]]
 
maxdistance = 0

for i in range(len(routes)):
    maxdistance += routes[i]
 
populationcount = random.randrange(1, 5) * 10
 
if (populationcount / 3) % 2 != 0:
    xovercount = populationcount / 3 + 1
elif (populationcount / 3) % 2 == 0:
    xovercount = populationcount / 3
 
mutationcount = (populationcount - xovercount / 2) / 2
randomtourscount = populationcount - xovercount / 2 - mutationcount
print ("population: ", populationcount, " crossovers: ", xovercount, " mutations: ", mutationcount, " random tours: ", randomtourscount)
 
population = []
citysequence = []
# we will initialize our first population using random tours method
for i in range(populationcount):
    # we make an array of the cities and append random number
    citysequence = []
    for j in range(citycount):
        citysequence.append([])
        citysequence[j].append(cities[j])
        citysequence[j].append(random.uniform(0, 1))
 
    # now we sort the citysequence array according to random number
    citysequence = sorted(citysequence, key=lambda i: i[1])
    citysequence2 = []
    for j in range(citycount):
        citysequence2.append(citysequence[j][0])
 
    population.append(citysequence2)
 

maxgeneration = int(input("Give generetion count: "))
generation = 0

while generation < maxgeneration:
    # we will create sequences through cross-over and add them to the population
    for v in range(0, int(xovercount), 2):
        parent1 = population[v]
        parent2 = population[v + 1]
        child = []
        partcount = random.randrange(2, len(parent1) - 1)
        # part 1 is the part form parent 1 that we will move to parent 2
        part1 = []
        for i in range(partcount, len(parent1)):
            part1.append(parent1[i])
 
        random.shuffle(part1)
 
        # part 2 is parent2 without the cities of the part 1
        seen = False
        part2 = []
        for i in range(len(parent2)):
            seen = False
            for j in range(len(part1)):
                if part1[j] == parent2[i]:
                    seen = True
            if seen == False:
                part2.append(parent2[i])
 
        child = [part2] + [part1]
        child = list(itertools.chain.from_iterable(child))
        population.append(child)
 
    # we will create sequences through mutation and add them to the population
    for v in range(int(xovercount) + 1, int(xovercount) + 1 + int(mutationcount)):
        # we have 2 ways to mutate, we will choose randomly one of the 2 ways
        way = random.randrange(0, 1)
        if way == 0 or way == 1:
            parent1 = population[v]
            child1 = parent1
            # first way to mutate is to pick a part of parent and suffle it
            partcount1 = random.randrange(2, 4)
            partplace1 = random.randrange(0, len(parent1) - partcount1)
            part1 = []
            for i in range(partplace1, partplace1 + partcount1):
                part1.append(parent1[i])
            random.shuffle(part1)
            for i in range(partplace1, partplace1 + partcount1):
                child1[i] = part1[i - partplace1]
 
            population.append(child1)
    
    # we will create sequences randomly and add them to the population
    for i in range(int(randomtourscount)):
        # we make an array of the cities and append random number
        citysequence = []
        for j in range(citycount):
            citysequence.append([])
            citysequence[j].append(cities[j])
            citysequence[j].append(random.uniform(0, 1))
 
        # now we sort the citysequence array according to random number
        citysequence = sorted(citysequence, key=lambda i: i[1])
        citysequence2 = []
        for j in range(citycount):
            citysequence2.append(citysequence[j][0])
 
        population.append(citysequence2)
 
    # we add the first city at the end at each tour
    for i in range(len(population)):
        population[i].append(population[i][0])
        if len(population[i]) != len(cities) + 1:
            del (population[i])[-1]
 
    # we will calculate the cost for each tour and  add the tours and distances to a 2d array for sorting
    toursdistance = []
    for i in range(len(population)):
        tourdistance = 0
        for j in range(len(population[i]) - 1):
            for v in range(len(tours)):
                if tours[v][0] == (str(population[i][j]) + "-" + str(population[i][j + 1])):
                    tourdistance = tourdistance + tours[v][1]
                elif tours[v][0] == (str(population[i][j + 1]) + "-" + str(population[i][j])):
                    tourdistance = tourdistance + tours[v][1]
        toursdistance.append(tourdistance)
 
    # we will keep only half of the population for the next generation according to best distances (elitism)
    result = (zip(population, toursdistance))
    result = sorted(result, key=lambda i: i[1])
    population = []
    print ("generation is: ", generation + 1)
    for i in range(len(result)):
        duplicate = False
        population.append(result[i][0])
        if result[i][1] < maxdistance:
            maxdistance = result[i][1]
            besttour = []
            besttour.append(result[i][0])
        elif result[i][1] == maxdistance:
            for j in range(len(besttour)):
                if besttour[j] == result[i][0]:
                    duplicate = True
            if duplicate == False:
                besttour.append(result[i][0])
 
        print ("tour ", i + 1, " is: ", result[i][0], " with length ", len(result[i][0]), " and distance is: ", result[i][1])
 
    population = population[:len(population) // 2]
    # delete last city
    for i in range(len(population)):
        population[i] = (population[i])[:-1]
 
    generation = generation + 1
print(tours)
for i in range(len(besttour)):
    print ("best tour ", besttour[i], " with distance ", maxdistance)