####################################################
#####################################################
#####################################################Diofantovo genetiheskii algoritm
######################################################

from random import randint
from copy import deepcopy
from math import floor
import random
 
 
class Organism:
    def __init__(self, alleles, fitness, likelihood):
        self.alleles = alleles
        self.fitness = fitness
        self.likelihood = likelihood
        self.result = 0
 
    def __unicode__(self):
        return '%s [%s - %s]' % (self.alleles, self.fitness, self.likelihood)
 
 
class CDiophantine:
    def __init__(self, coefficients, result):
        self.coefficients = coefficients
        self.result = result
 
    maxPopulation = 100
    organisms = []
 
    def GetGene(self, i):
        return self.organisms[i]
 
    def OrganismFitness(self, gene):
        gene.result = 0
        for i in range(0, len(self.coefficients)):
            gene.result += self.coefficients[i] * gene.alleles[i]
        gene.fitness = abs(gene.result - self.result)
        return gene.fitness
 
    def Fitness(self):
        for organism in self.organisms:
            organism.fitness = self.OrganismFitness(organism)
            if organism.fitness == 0:
                return organism
        return None
 
    def MultiplyFitness(self):
        coefficientSum = 0
        for organism in self.organisms:
            coefficientSum += 1 / float(organism.fitness)
        return coefficientSum
 
    def GenerateLikelihoods(self):
        last = 0
        multiplyFitness = self.MultiplyFitness()
        for organism in self.organisms:
            last = ((1 / float(organism.fitness) / multiplyFitness) * 100)
            organism.likelihood = last
 
    def Breed(self, parentOne, parentTwo):
        crossover = randint(1, len(self.coefficients) - 1)
        child = deepcopy(parentOne)
        if randint(1, 100) < 50:
            father = parentOne
            mother = parentTwo
        else:
            father = parentTwo
            mother = parentOne
        child.alleles = mother.alleles[:crossover] + father.alleles[crossover:]
        if randint(1, 100) < 5:
            for i in range(0, len(parentOne.alleles) - 1):
                child.alleles[i] = randint(0, self.result)
        return child
 
    def CreateNewOrganisms(self):
        tempPopulation = []
        for _ in self.organisms:
            temp = 0
            iterations = 0
            father = deepcopy(self.organisms[0])
            mother = deepcopy(self.organisms[1])
            while temp != 1 and father.alleles == mother.alleles:
                father = self.WeightedChoice()
                mother = self.WeightedChoice()
                iterations += 1
                temp += 1
                if iterations > 100:
                    break
            kid = self.Breed(father, mother)
            tempPopulation.append(kid)
        self.organisms = tempPopulation
 
    def WeightedChoice(self):
        list = []
        for organism in self.organisms:
            list.append((organism.likelihood, organism))
        list = sorted((random.random() * x[0], x[1]) for x in list)
        return list[-1][1]
 
    def Solve(self):
        solcount = 0
        fakeiterations = 0
        while solcount != 1:
            for i in range(0, self.maxPopulation):
                alleles = []
                for j in range(0, len(self.coefficients)):
                        alleles.append(randint(0, self.result))
                self.organisms.append(Organism(alleles, 0, 0))
            solution = self.Fitness()
            if solution:
                print (solution.alleles)
                solcount += 1
            iterations = 0
            while not solution and iterations < 200:
                self.GenerateLikelihoods()
                self.CreateNewOrganisms()
                solution = self.Fitness()
                if solution:
                    print ('Reshenii bilo naideno v', fakeiterations, 'iteracii:')
                    print(solution.alleles)
                    solcount += 1
                    break
                iterations += 1
                fakeiterations += 1
                print('Iteraciya:', fakeiterations)
 
diophantine = CDiophantine ([1,2,3,4],30)
diophantine.Solve()