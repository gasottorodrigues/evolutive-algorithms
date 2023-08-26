import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

from src.Simulation import Simulation

#PARAMETROS
pop_size = 100
gene_range = 200
generations = 100
mutate_agress= 20

def y(x):
    if x < 0:
        return 0
    elif x > 0 and x < 100:
        return x
    elif x <= 200:
        return 200 - x
    
    return 0

def main():

    current_best = None
    current_best_fit = -1

    simul_results = pd.DataFrame([],columns=['geracao','best_fit','avg_fit'])

    pop_idx = [x for x in range(pop_size)]
    population = Simulation.generate_pop(pop_size,gene_range)

    for gen in range(1,generations+1):
        # Avalia a Geracao Atual
        result, idx_best, fits = Simulation.evaluate_gen(population,y)
        result['geracao'] = gen
        
        # Registra os resultados num Dataframe
        gen_results = pd.DataFrame(data=result,index=[0])
        simul_results = pd.concat([simul_results,gen_results]).reset_index(drop=True)

        # Seleciona o Melhor de Todos 
        if current_best_fit < result['best_fit']:
            current_best = population[idx_best]
            current_best_fit = result['best_fit']
            population.pop(idx_best)

        # Reproduz
        population = Simulation.reproduce(population,current_best,fits,method='to2',mutate_agressivity=mutate_agress)


    simul_results.plot.line(x='geracao',y=['best_fit','avg_fit'],title='Melhor Fit e Fit Medio por Geracao', figsize=(9,6))

    input('Pressione qualquer tecla para encerrar...')

if __name__=="__main__":
    main()