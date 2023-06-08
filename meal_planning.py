import random
from collections import Counter

# Our meal data
meals = ["Doughman Classic Box of 6", "Streetwise 3", "Mini boneless bucket", "Coca-Cola & Angwamo",
                    "Speedy Pizza Classic GH Mega Pizza", "Street Vibes Hot Ga Kenkey with Sausages and Fried Egg",
                    "Special Joint Plain rice and beans stew", "Chomp Combo Meal", "Gobe Masters Beans and Plantain",
                    "Waakye Kitchen Waakye Your Way", "By the roadside Fried Yam", "By the roadside Kenkey"]
costs = [88, 66, 55, 57.80, 84, 35, 49, 55, 34, 29.80, 20, 20]
values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

budget = 400
days = 7

def initialize_population(size):
    initial_population = []
    for i in range(size):
        current_gene = []
        for j in range(days):
            random_meal = meals[random.randint(0, len(meals) - 1)]
            current_gene.append(random_meal)
        initial_population.append(current_gene)
    return initial_population

def calculate_fitness(meal_plan):
    cost = 0
    value = 0
    for meal in meal_plan:
        cost = cost + costs[meals.index(meal)]
        value = value + values[meals.index(meal)]
    max_times_an_item_appears = 0
    counts = Counter(meal_plan)
    for item in counts:
        if counts[item] > max_times_an_item_appears:
            max_times_an_item_appears = counts[item]
    fitness = ((budget - cost) + value) - (max_times_an_item_appears * 100)
    return fitness

def select_parents(population):
    fitnesses = [calculate_fitness(meal_plan) for meal_plan in population]
    parents = random.choices(population, weights=fitnesses, k=2)
    return parents

def crossover(parents):
    point = random.randint(0, days)
    child1 = parents[0][:point] + parents[1][point:]
    child2 = parents[1][:point] + parents[0][point:]
    return [child1, child2]

def mutate(meal_plan):
    number_of_times_to_mutate = random.randint(1, 100)
    for i in range(number_of_times_to_mutate):
        point = random.randint(0, days - 1)
        meal_plan[point] = random.choice(meals)    
    return meal_plan

def genetic_algorithm(population_size, generations):
    population = initialize_population(population_size)
    
    for generation in range(generations):
        new_population = []
        
        for _ in range(population_size // 2):
            parents = select_parents(population)
            children = crossover(parents)
            
            for child in children:
                if random.random() < 0.4:  # 10% chance of mutation
                    child = mutate(child)
                
                new_population.append(child)
        
        population = new_population
    
    # Return the best meal plan we found
    best_plan = max(population, key=calculate_fitness)
    return best_plan, calculate_fitness(best_plan)

for i in range(10):
    best_plan, best_plan_value = genetic_algorithm(100, 50)
    print(f"Best meal plan: {best_plan}")
    print(f"Value of best meal plan: {best_plan_value}")
    price_of_all_food = 0
    for meal in best_plan:
        price_of_all_food = price_of_all_food + costs[meals.index(meal)]
    print(f"Cost of all food is: {price_of_all_food}")
    print("\n\n")