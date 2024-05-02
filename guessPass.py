import random
geneset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"

def generate_parent(length):
    genes=[]
    genes.extend(random.sample(geneset,length))
    return  " ".join(genes)

generate_parent(len(target))

def get_fitness(guess):
    return sum(1 for expected,actual in zip(target,guess)
                if expected==actual)


def mutate(parent):
    index =random.randrange(0,len(parent))
    childGenes=list(parent)
    newGene,alter=random.sample(geneset,2)

    if newGene==childGenes[index]:
        childGenes[index]=alter
    else :
        childGenes[index]=newGene
    return "".join(childGenes)


def display(guess):
    fitness=get_fitness(guess)
    print(f"{guess} \t {fitness}")


best_parent=generate_parent(len(target))
bets_fitenss=get_fitness(best_parent)
display(best_parent)

while True:
    child=mutate(best_parent)
    child_fitness=get_fitness(child)

    if child_fitness > bets_fitenss:
        best_parent=child
        bets_fitenss = child_fitness
        display(child)

        if child_fitness >=len(best_parent):
            break