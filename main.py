import random

class Chromosome:
    def __init__(self, genes):
        self.__num_of_genes = genes
        self.__chromosome = []
        self.__fitnss = 0

    def set_num_of_genes(self, genes):
        self.__num_of_genes = genes

    def set_fitness(self, fitness):
        self.__fitnss = fitness

    def set_chrom(self, chrom):
        self.__chromosome = chrom

    def get_chrom(self):
        return self.__chromosome

    def get_fitness(self):
        return self.__fitnss

    def get_num_of_genes(self):
        return self.__num_of_genes

    def generate_chrom(self):
        i=0
        while i < self.__num_of_genes :
            num = random.uniform(0.0, 1.0)
            self.__chromosome.append(num)
            i+=1

    def encode_chrom(self):
        for i in range(0, len(self.__chromosome)):
            if self.__chromosome[i] < 0.5:
                self.__chromosome[i] = 1
            else:
                self.__chromosome[i] = 0

    def fitness(self, weight, benefit, size_of_knapsack):
        w = 0
        b = 0
        for i in range(0, len(weight)):
            w += weight[i] * self.__chromosome[i]
            b += benefit[i] * self.__chromosome[i]
        if w > size_of_knapsack:
            b = 0
        self.__fitnss = b
        return b

    def mutation(self):
        for index, value in enumerate(self.__chromosome):
            mutation_p = random.uniform(0.0, 1.0)
            if mutation_p > 0.1:
                continue
            else:
                self.__chromosome[index] = 1 if self.__chromosome[index] == 0 else 0


class Generation:
    def __init__(self, population):
        self.__population_size = population
        self.__chromosomes = []

    def set_population_size(self, population):
        self.__population_size = population

    def set_chromosomes(self, chroms):
        self.__chromosomes = chroms

    def get_population_size(self):
        return self.__population_size

    def get_chromosomes(self):
        return self.__chromosomes

    def add_chrom(self, chrom):
        self.__chromosomes.append(chrom)

    def set_generation(self, genes):
        for i in range(0, self.__population_size):
            chrom = Chromosome(genes)
            chrom.generate_chrom()
            chrom.encode_chrom()
            self.add_chrom(chrom)

    def print_generation(self):
        for i in range(0, self.__population_size):
            chrom = self.__chromosomes[i].get_chrom()
            for j in chrom:
                print (j)
            print (self.__chromosomes[i].get_fitness())
            print ("---------")

    def cal_fitness(self, weight, benefit, size_of_knapsack):
        for chrom in self.__chromosomes:
            chrom.fitness(weight, benefit, size_of_knapsack)

    def total_fitness(self):
        fitness = 0
        for i in self.__chromosomes:
            fitness += i.get_fitness()
        return fitness

    def roulette_wheel(self, total_fitness):
        new_parents = []
        while len(new_parents) < self.__population_size:
            pick = random.randint(0, total_fitness)
            current = 0
            for chromosome in self.__chromosomes:
                current += chromosome.get_fitness()
                if (current > pick):
                    new_parents.append(chromosome)
                    break
        return new_parents

    def cross_over(self, items, weight, benefit, size_of_knapsack):
        for index in range(0, len(self.__chromosomes), 2):
            item1 = self.__chromosomes[index]
            item2 = self.__chromosomes[index + 1]
            cross_point = random.randint(1, items - 1)
            cross_p = random.uniform(0.0, 1.0)
            if cross_p > 0.5:
                continue
            else:
                chield_one, chield_two = Chromosome(items), Chromosome(items)
                arr1 = item1.get_chrom()
                arr2 = item2.get_chrom()
                chield_one.set_chrom(arr1[:cross_point] + arr2[cross_point:])
                chield_two.set_chrom(arr2[:cross_point] + arr1[cross_point:])
                chield_one.set_fitness(chield_one.fitness(weight, benefit, size_of_knapsack))
                chield_two.set_fitness(chield_two.fitness(weight, benefit, size_of_knapsack))
                self.__chromosomes[index] = item1 if item1.get_fitness > chield_one.get_fitness else chield_one
                self.__chromosomes[index + 1] = item2 if item2.get_fitness > chield_two.get_fitness else chield_two

    def mutation(self):
        for chromosome in self.__chromosomes:
            chromosome.mutation()

    def solution(self):
        max_fitness = self.__chromosomes[0]
        for chrom in self.__chromosomes:
            if chrom.get_fitness() > max_fitness.get_fitness():
                max_fitness = chrom
        return max_fitness








items = input("number of items")
size_of_knapsack = input("size of knapsack")
weight = []
benefit = []

for i in range(0, items):
    w, b = raw_input().strip().split()
    weight.append(int(w))
    benefit.append(int(b))

print ("calculating...")

generation = Generation(100)
generation.set_generation(items)

best_of_all = 0
for i in range(0, 50):
    generation.cal_fitness(weight, benefit, size_of_knapsack)
    total_fit = generation.total_fitness()
    generation.set_chromosomes(generation.roulette_wheel(generation.total_fitness()))
    generation.cross_over(items, weight, benefit, size_of_knapsack)
    generation.mutation()
    print (i)
    sol = generation.solution()
    if sol.get_fitness() > best_of_all:
        best_of_all = sol.get_fitness()


print ("solution:done")
print (best_of_all)














