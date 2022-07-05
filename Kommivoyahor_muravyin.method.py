####################################################
#####################################################Kommivoyahor muravyini algoritm
#####################################################
######################################################
import random as rn
import numpy as np
from numpy.random import choice as np_choice

V = 5
A = [[0] * V for i in range(V)]
for i in range(V):
    for j in range(V):
        A[i][j] = rn.randint(1, 20)
            
for i in range(V):
    for j in range(V):
        if i==j:
            A[i][j]=0
            
matrix = np.array(A, float)
class AntColony(object):

    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        
        
            #distances (2D numpy.array): Квадратная матрица расстояний. Предполагается, что диагональ равна np.inf
            #n_ants (int): Количество муравьев, бегущих за итерацию
            #n_best (int): Количество лучших муравьев, откладывающих феромон
            #n_iteration (int): Количество итераций
            #decay (float): Оцените, какой феромон распадается. Ценность феромона умножается на распад, поэтому 0,95 приведет к распаду, 0,5 - к гораздо более быстрому распаду.
            #alpha (int or float): по показателю феромона, более высокий альфа дает феромон больший вес. По умолчанию = 1
            #beta (int or float): экспонента на расстоянии, более высокие значения бета придают расстоянию больший вес. По умолчанию = 1
        
            #ant_colony = AntColony(german_distances, 100, 20, 2000, 0.95, alpha=1, beta=2)          
        
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        i = 0
        j = 0
        while i < len(distances):
            while j < len(distances):
                if distances[i][j] == 0:
                    distances[i][j] = np.inf #nuli zamenyaem beskonehnostiyu
                    i += 1
                    j += 1
                else:
                    continue
    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheronome(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone = self.pheromone * self.decay            
        return all_time_shortest_path

    def spread_pheronome(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)

        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move
    
distance = matrix
print('Rasstoyaniya:')
print(distance)
ant_colony = AntColony(distances = distance, n_ants = len(distance) * 2, n_best = 5, n_iterations = 100, decay = 0.95, alpha=1, beta=1)
path = ant_colony.run()
print('Krothaihii marshrut:')
print(path)