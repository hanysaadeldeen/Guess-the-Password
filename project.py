import random

class Gemstone:
    def __init__(self, color=None, weight=None, value=None):

        self.color = color
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Gemstone(color={self.color}, weight={self.weight}, value={self.value})"

def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        color = random.choice(["red", "blue", "green"])
        weight = random.uniform(0.1, 10.0)
        value = random.randint(1, 100)
        gene_stone = Gemstone(color, weight, value)
        population.append(gene_stone)   
    return population

def select_best_stones(population, num_selected):
    sorted_population = sorted(population, key=lambda x: x.value, reverse=True)
    print(sorted_population[:num_selected])
    return sorted_population[:num_selected]

def crossover(gemstone1, gemstone2):
    
    color = gemstone1.color if random.random() < 0.5 else gemstone2.color
    weight = (gemstone1.weight + gemstone2.weight) / 2
    value = (gemstone1.value + gemstone2.value) / 2 
    return Gemstone(color, weight, value)

def mutate(gemstone):

    mutation_factor = random.uniform(0.9, 1.1) 
    gemstone.weight *= mutation_factor
    gemstone.value = max(1, gemstone.value + random.randint(-10, 10))


def evolve_genestones(population_size, num_generations):                                
    population = initialize_population(population_size)
    for generation in range(num_generations):
        selected_gemstones = select_best_stones(population, population_size // 2)
        new_population = []
        for i in range(len(selected_gemstones) - 1):
            child_genstone = crossover(selected_gemstones[i], selected_gemstones[i+1])
            mutate(child_genstone)
            new_population.append(child_genstone)
        population = new_population
        print(f"Generation {generation+1}: {population}")

evolve_genestones(24,11)



