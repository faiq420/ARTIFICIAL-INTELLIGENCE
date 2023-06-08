# import operator
# import math
import random
# import numpy as np
from deap import algorithms, base, creator, tools, gp

# def division_operator(numerator, denominator):
#    if denominator == 0:
#       return 1
#    return numerator / denominator

# def eval_func(individual, points):
#    func = toolbox.compile(expr=individual)
#    mse = [(func(x) - math.sin(x))**2 for x in points]
#    return math.fsum(mse) / len(points),

# def create_toolbox():
#    pset = gp.PrimitiveSet("MAIN", 1)
#    pset.addPrimitive(operator.add, 2)
#    pset.addPrimitive(operator.sub, 2)
#    pset.addPrimitive(operator.mul, 2)
#    pset.addPrimitive(division_operator, 2)
#    pset.addPrimitive(operator.neg, 1)
#    pset.addPrimitive(math.cos, 1)
#    pset.addPrimitive(math.sin, 1)
#    pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))
#    pset.renameArguments(ARG0='x')

#    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
#    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

#    toolbox = base.Toolbox()
#    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
#    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
#    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#    toolbox.register("compile", gp.compile, pset=pset)
#    toolbox.register("evaluate", eval_func, points=[x/10. for x in range(-10,10)])
#    toolbox.register("select", tools.selTournament, tournsize=3)
#    toolbox.register("mate", gp.cxOnePoint)
#    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
#    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
#    toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
#    toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

#    return toolbox

# if __name__ == "__main__":
#    random.seed(7)
#    toolbox = create_toolbox()
#    population = toolbox.population(n=450)
#    hall_of_fame = tools.HallOfFame(1)
#    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
#    stats_size = tools.Statistics(len)
#    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
#    mstats.register("avg", np.mean)
#    mstats.register("std", np.std)
#    mstats.register("min", np.min)
#    mstats.register("max", np.max)

#    probab_crossover = 0.4
#    probab_mutate = 0.2
#    number_gen = 10

#    population, log = algorithms.eaSimple(population, toolbox,probab_crossover, probab_mutate, number_gen,stats=mstats, halloffame=hall_of_fame, verbose=True)



def eval_func(individual):
    target_sum = 15
    return len(individual) - abs(sum(individual) - target_sum),


def create_toolbox(num_bits):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat,
                     creator.Individual, toolbox.attr_bool, num_bits)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", eval_func)

    toolbox.register("mate", tools.cxTwoPoint)

    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)

    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox


if __name__ == "__main__":
    num_bits = 45
    toolbox = create_toolbox(num_bits)
    random.seed(7)
    population = toolbox.population(n=500)
    probab_crossing, probab_mutating = 0.5, 0.2
    num_generations = 10
    print('\nEvolution process starts')
    fitnesses = list(map(toolbox.evaluate, population))

    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit
    print('\nEvaluated', len(population), 'individuals')

    for g in range(num_generations):
        print("\n- Generation", g)
        offspring = toolbox.select(population, len(population))
        offspring = list(map(toolbox.clone, offspring))

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < probab_crossing:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < probab_mutating:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = list(map(toolbox.evaluate, invalid_ind))

        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        print('Evaluated', len(invalid_ind), 'individuals')

        population[:] = offspring
        fits = [ind.fitness.values[0] for ind in population]
        length = len(population)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5
        print('Min =', min(fits), ', Max =', max(fits))
        print('Average =', round(mean, 2),
              ', Standard deviation =', round(std, 2))

    print("\nEvolution ends")

    best_ind = tools.selBest(population, 1)[0]
    print('\nBest individual:\n', best_ind)
    print('\nNumber of ones:', sum(best_ind))