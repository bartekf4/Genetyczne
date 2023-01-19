import os.path
import pathlib
import random
import numpy as np
import progressbar
from evaluator.antlr_output.translate import translate
from temp import *


NAME = "I_1to5__O_roznica_-9999_9999"

#suma
# INPUT_ARRAY = ["10 10", "3 4", "5 6", "7 8", "9 10"]
# EXPECTED = [[20], [7], [11], [15], [19]]

#mediana
# INPUT_ARRAY = ["10 20 100", "15 97 105", "48 561 719", "1547 2034 19874", "111 1111 11111"]
# EXPECTED = [[20], [97], [561], [2034], [1111]]

#  Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę.
#  Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]
# INPUT_ARRAY = ["3 4 2 3 -2", "-5 3 5 3 6", "-9 -2 4 3"]
# EXPECTED = [[7], [-2], [-7]]

# Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich różnicę.
# Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]
INPUT_ARRAY = ["-9999 -9999 84 218 45 6 4 2", "5748 1254 0 0 0 0", "-8314 9866 47 41"]
EXPECTED = [[-19998], [4494], [1552]]

# INPUT_ARRAY = ["1 2"]
# EXPECTED = [[1]]

input_string = """1\n
2\n
3\n
4\n
5\n
6\n
7\n"""

input_string1 = """1\n
2\n
3\n
4\n
5\n
6\n
7\n"""

DEPTH = 12
NUM = 2
TARGET = 1

PATH = ".\\current_pop\\"
PATH_TREES = ".\\current_pop_trees\\"

PATH_ANOTHER = ".\\another_pop\\"
PATH_ANOTHER_TREES = ".\\another_pop_trees\\"

POP = ".\\population\\"

PATH_BEST = "best_individuals/"

OUTPUT_RANGE = (-20000, 20000)
OUTPUT_OUT_OF_RANGE_FINE = 1000
DIFFERENT_SIZE_FINE = 1000000

ALLOWED_FUNCTIONS = ["mse", "mae", "cod", "custom"]
FUNCTION = ALLOWED_FUNCTIONS[0]

INITIAL_POP_SIZE =30
MIN_FITNESS = 0.5
INDIVIDUALS_NEXTGEN = INITIAL_POP_SIZE

TIMEOUT = 1

TOURNAMENT_SIZE = 5
PROBABILITY_MUTATION = 0.4
PROBABILITY_CROSSOVER = 0.6


def fitness_function(input_array, output_array):
    count = 0
    penalty = 0
    desired_output = [1]
    for i in range(len(output_array)):
        if output_array[i] == 789:
            count += 1
        elif output_array[i] != 789:
            penalty += 1
    similarity = len(set(output_array).intersection(desired_output)) / len(desired_output)
    fitness = - (count + similarity - (penalty / len(output_array)))
    return fitness


F = fitness_function


def array_of_values_from_exec_output(output: str) -> list[float]:
    arr = []
    for line in output.split("\n"):
        if line == "":
            continue
        arr.append(float(line))
    return arr


def calculate_coefficient_of_determination(inputs, outputs):
    mean_expected = sum(inputs) / len(inputs)

    # Calculate the total sum of squares
    sst = sum([(expected - mean_expected) ** 2 for expected in inputs])

    # Calculate the residual sum of squares
    ssr = sum([(expected - output) ** 2 for expected, output in zip(inputs, outputs)])

    # Calculate the coefficient of determination (R²)
    r_squared = 1 - (ssr / sst)

    # Return the fitness score (higher is better)
    return r_squared


def move_individuals():
    move_and_clean_directory(src_dir=".\\another_pop\\", dst_dir=".\\current_pop\\")
    move_and_clean_directory(src_dir=".\\another_pop_trees\\", dst_dir=".\\current_pop_trees\\")
    return


def fittness(inputs, outputs):
    score = 0
    if len(outputs) != len(inputs):
        score += DIFFERENT_SIZE_FINE
        return score
    if FUNCTION == "mse":  # MSE jest wartością oczekiwaną kwadratu „błędu”, czyli różnicy między estymatorem a wartością estymowaną.
        mse = sum([(expected - output) ** 2 for expected, output in zip(inputs, outputs)]) / len(inputs)
        score += mse
    if FUNCTION == "mae":  # Mean absolute error
        mae = sum([abs(expected - output) for expected, output in zip(inputs, outputs)]) / len(
            inputs)
        score += mae
    if FUNCTION == "cod":  # statistical measurement that examines how differences in one variable can be explained by the difference in a second variable, when predicting the outcome of a given event
        cod = calculate_coefficient_of_determination(inputs, outputs)
        score += cod
    if FUNCTION == "custom":
        score += F(inputs, outputs)

    if any(output < OUTPUT_RANGE[0] or output > OUTPUT_RANGE[1] for output in outputs):
        score += OUTPUT_OUT_OF_RANGE_FINE
    return score


def get_individuals():
    individuals = []
    for filename in os.listdir(PATH):
        f = os.path.join(PATH, filename)
        if os.path.isfile(f):
            individuals.append(f)

    return individuals


def mutate(individuals_scores: dict[str, float]):
    individual = tournament(individuals_scores, num=1)[0]
    individual = os.path.basename(individual)
    src = PATH_TREES + individual + ".grt"
    dest = POP + individual + ".grt"
    # shutil.copyfile(src, dest)
    subprocess.call(f'copy {src} {dest}', shell=True, stdout=subprocess.PIPE)
    mutate_individual()
    recursive_delete(POP)
    return


def crossover(individuals_scores: dict[str, float]):
    selected = tournament(individuals_scores, num=2)
    ind1 = os.path.basename(selected[0])
    ind2 = os.path.basename(selected[1])

    src1 = PATH_TREES + ind1 + ".grt"
    src2 = PATH_TREES + ind2 + ".grt"

    dest1 = POP + ind1 + ".grt"
    dest2 = POP + ind2 + ".grt"

    # shutil.copyfile(src1, dest1)
    # shutil.copyfile(src2, dest2)

    subprocess.call(f'copy {src1} {dest1}', shell=True, stdout=subprocess.PIPE)
    subprocess.call(f'copy {src2} {dest2}', shell=True, stdout=subprocess.PIPE)
    crossover_individuals()
    recursive_delete(POP)
    return


def tournament(individuals_scores: dict[str, float], num=1) -> list[str]:
    selected = random.choices(list(individuals_scores.keys()), k=TOURNAMENT_SIZE)
    selected = sorted(selected, key=lambda x: individuals_scores[x])
    return selected[:num]


def succesion(individuals_scores: dict[str, float]):
    individual, score = get_best_individual(individuals_scores)
    src = individual
    dest = PATH_ANOTHER + os.path.basename(individual)
    # shutil.copyfile(src, dest)
    return subprocess.call(f'copy {src} {dest}', shell=True, stdout=subprocess.PIPE)


def reproduce(individuals_scores: dict[str, float]):
    succesion(individuals_scores)
    i = 1
    with progressbar.ProgressBar(max_value=INITIAL_POP_SIZE) as bar:
        while i < INITIAL_POP_SIZE:
            operation = np.random.choice(["mutate", "crossover"], 1, p=[PROBABILITY_MUTATION, PROBABILITY_CROSSOVER])
            if operation == "mutate":
                mutate(individuals_scores)
                i += 1
                bar.update(i)
            elif operation == "crossover":
                crossover(individuals_scores)
                i += 1
                bar.update(i)


def get_scores(individuals) -> dict[str, float]:
    score_dict = {}
    bar = progressbar.ProgressBar(0, len(individuals))
    counter = 0
    print("Evaluating the individuals.")
    for ind in individuals:
        with open(ind, "r") as file:
            code = translate(ind)
        with open('tmpscript.py', 'w') as file:
            file.write(code)
        try:
            score = 0
            for exp, input in zip(EXPECTED, INPUT_ARRAY):
                process_script = subprocess.Popen(["python.exe", "./tmpscript.py"], stdout=subprocess.PIPE,
                                                  stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                                  universal_newlines=True)

                for inString in input.split(' '):
                    process_script.stdin.write(inString + '\n')

                result = process_script.communicate(timeout=TIMEOUT)[0]

                # result = result.decode("utf-8")
                outputs = array_of_values_from_exec_output(result)
                score += fittness(outputs, exp)
            score_dict[ind] = score



        except Exception as e:
            score_dict[ind] = 10000000
        finally:
            counter += 1
            bar.update(counter)
            open('tmpscript.py', "w").close()
    return score_dict


def get_best_individual(scores: dict[str, float]) -> tuple[str, float]:
    best_individual = min(scores, key=scores.get)
    best_score = scores[best_individual]
    return best_individual, best_score


def select_parents(scores: dict[str, float]) -> list[str]:
    scores = sorted(scores.items(), key=lambda x: x[1])

    scores = scores[:INDIVIDUALS_NEXTGEN - 2]
    return list(dict(scores).keys())


def prepare_for_next_gen(parents: list[str]) -> None:
    parents = [os.path.basename(parent) + ".grt" for parent in parents]
    for tree in os.listdir(PATH_TREES):
        if tree not in parents:
            os.unlink(PATH_TREES + tree)


def genetic(max_iters=1):
    global best_individual, best_score

    generate_population(num=INITIAL_POP_SIZE, depth=DEPTH, output=PATH + "test%d.txt")
    generate_trees(input=PATH, output=PATH_TREES)

    for i in progressbar.progressbar(range(0, max_iters)):
        individuals = get_individuals()
        scores = get_scores(individuals)
        # parents = select_parents(scores)
        # prepare_for_next_gen(parents)

        reproduce(scores)

        # reproduce_population(input_trees=PATH_TREES, output=PATH_ANOTHER + "test%d.txt", num=INDIVIDUALS_NEXTGEN,
        #                      depth=DEPTH)
        generate_trees(input=PATH_ANOTHER, output=".\\another_pop_trees\\")

        best_individual, best_score = get_best_individual(scores)
        print(f'Population no. {i + 1}. Best individual score: {best_score}.')

        filename = f'{NAME}best_iter{i + 1}_S__{best_score}.py'

        with open(pathlib.Path(PATH_BEST, filename.__str__()), "w") as file:
            file.write(translate(best_individual))
        if best_score < MIN_FITNESS:
            return best_individual, best_score
        move_individuals()
    return best_individual, best_score


ind, best = genetic(10)
print(f"Best individual: {ind}\nScore: {best}\nInputs: {EXPECTED}\n")

recursive_delete(PATH)
recursive_delete(PATH_TREES)
recursive_delete(PATH_ANOTHER)
recursive_delete(PATH_ANOTHER_TREES)
recursive_delete(POP)
