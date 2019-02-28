# tiny genetic algorithm by moshe sipper, www.moshesipper.com
import random

POP_SIZE        = 6     # population size
GENOME_SIZE     = 5     # number of bits per individual in the population
GENERATIONS     = 100   # maximal number of generations to run GA
TOURNAMENT_SIZE = 3     # size of tournament for tournament selection
PROB_MUTATION   = 0.1   # bitwise probability of mutation

def init_population(): # population comprises bitstrings
    return([(''.join(random.choice("01") for i in range(GENOME_SIZE))) 
                        for i in range(POP_SIZE)])

def fitness(individual): # fitness = number of 1s in individual
    return str(individual).count("1")
                
def selection(population): # select one individual using tournament selection
    tournament = [random.choice(population) for i in range(TOURNAMENT_SIZE)]
    fitnesses = [fitness(tournament[i]) for i in range(TOURNAMENT_SIZE)]
    return tournament[fitnesses.index(max(fitnesses))] 

def crossover(parent1,parent2): # single-point crossover
    parent1,parent2=str(parent1),str(parent2)
    xo_point=random.randint(1, GENOME_SIZE-1)
    return([
            parent1[0:xo_point]+parent2[xo_point:GENOME_SIZE],
            parent2[0:xo_point]+parent1[xo_point:GENOME_SIZE] ])

def bitflip(bit): # used in mutation 
    bit=str(bit)
    if bit == "0":
        return "1"
    else:
        return "0"
    
def mutation(individual): # bitwise mutation with probability PROB_MUTATION
    individual=str(individual)
    for i in range(GENOME_SIZE):
        if random.random() < PROB_MUTATION:
            individual = individual[:i] + bitflip(i) + individual[i+1:]
    return(individual)        
            
def print_population(population):            
    fitnesses=[fitness(population[i]) for i in range(POP_SIZE)]
    print(list(zip(population,fitnesses)))

            
# begin GA run            
random.seed() # initialize internal state of random number generator
population=init_population() # generation 0
    
for gen in range(GENERATIONS):
    print("Generation ",gen)
    print_population(population)
    if max([fitness(population[i]) for i in range(POP_SIZE)]) == GENOME_SIZE:
        break;
    nextgen_population=[]
    for i in range(int(POP_SIZE/2)):
        parent1=selection(population)
        parent2=selection(population)
        offspring=crossover(parent1,parent2)
        nextgen_population.append(mutation(offspring[0]))
        nextgen_population.append(mutation(offspring[1]))
    population=nextgen_population
