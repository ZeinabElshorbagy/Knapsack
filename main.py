import random
class Chromosome:
    def __init__(self, genes):
        self.__num_of_genes = genes
        self.__chromosome = []

    def set_num_of_genes(self, genes):
        self.__num_of_genes = genes

    def set_chrom(self, chrom):
        self.__chromosome = chrom

    def get_chrom(self):
        return self.__chromosome

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

            print ("---------")



items = input("number of items")
size_of_knapsack = input("size of knapsack")

generation = Generation(4)
generation.set_generation(items)
generation.print_generation()

print ("try")





