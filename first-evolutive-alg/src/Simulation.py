from src.Individual import Individual
import random

class Simulation:

    @staticmethod
    def generate_pop(pop_size:int,gene_range:int):
        population = []

        for i in range(pop_size):
            population.append(Individual(random.uniform(0,gene_range)))
        return population
    
    @staticmethod
    def evaluate_gen(population:list[Individual],eval_func):
        fits = [population[0].gene1]
        avg_fit = eval_func(population[0].gene1)
        max_fit = eval_func(population[0].gene1)
        ind_max = 0

        for ind in population[1:]:
            ind_fit = eval_func(ind.gene1)
            
            if(ind_fit > max_fit):
                max_fit = ind_fit
                ind_max = population.index(ind)

            avg_fit += ind_fit
            fits.append(ind_fit)
        
        return {
            'best_fit':max_fit,
            'avg_fit':avg_fit/len(population)
        }, ind_max, fits
    
    @classmethod
    def reproduce(cls,population:list[Individual],best:Individual,fits:list[float],method:str,mutate_agressivity:float):
        if method == 'elitism':
            new_gen = cls.elitism(population,best)
        elif method == 'to2':
            new_gen =  cls.tourn_of_2(population,fits)
        elif method == 'assexual':
            new_gen = population.copy()
        
        new_gen = cls.mutate(new_gen,mutate_agressivity)
        new_gen.append(best)
        return new_gen
    
    @staticmethod
    def elitism(population:list[Individual],best:Individual):
        new_gen=[]
        for pop in population:
            new_gen.append(Individual((pop.gene1+best.gene1)/2.0))

        return new_gen
    
    @staticmethod
    def tourn_of_2(population:list[Individual],fits:list[float]):
        new_gen=[]
        pop_size = len(population)
        for i in range(pop_size):
            dad1 = random.randint(0,pop_size-1)
            dad2 = random.randint(0,pop_size-1)

            if fits[dad1] > fits[dad2]:
                dad = population[dad1]
            else:
                dad = population[dad2]

            mom1 = random.randint(0,pop_size-1)
            mom2 = random.randint(0,pop_size-1)

            if fits[mom1] > fits[mom2]:
                mom = population[mom1]
            else:
                mom = population[mom2]

            new_gen.append(Individual((mom.gene1+dad.gene1)/2.0))
        
        return new_gen
    
    @staticmethod
    def mutate(pop:list[Individual],mutate_agressivity:float):
        for p in pop:
            mut_value = random.uniform(-1,1) * mutate_agressivity
            p.gene1 += mut_value

        return pop

            
        