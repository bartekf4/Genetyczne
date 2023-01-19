import os
import shutil
import subprocess


def generate_population(num=10, depth=12, output=".\\current_pop\\test%d.txt"):
    print(f'Generating population of {num} individuals to {output}')
    # widgets = [
    #     ' [', progressbar.Timer(), '] ',
    #     progressbar.Bar(),
    #     ' (', progressbar.ETA(), ') ',
    # ]

    subprocess.call(['powershell.exe',
                     '$ErrorActionPreference= "silentlycontinue" \n',
                     f'conda activate grammarinator_env\n',
                     f'grammarinator-generate.exe -l .\\bezBoolowUnlexer.py '
                     f'-p .\\bezBoolowUnparser.py -d {depth} -n {num}  -o {output} '],
                    stdin=None, stdout=None, stderr=None)
    return

def generate_trees(input="..//current_pop//", output=".//current_pop_trees//"):
    files = get_filenames(input)
    counter = 0
    ff = ""
    for file in files:
        ff += " " + file

    subprocess.run(['powershell.exe',
                    f'conda activate grammarinator_env\n grammarinator-parse {ff} -g .\\bezBoolow.g4  -r file_ -o {output}'],
                   stdout=None, stderr=None)
    return

def move_and_clean_directory(src_dir: str, dst_dir: str) -> None:
    # remove all files and directories from dst_dir
    for file in os.listdir(dst_dir):
        file_path = os.path.join(dst_dir, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    # move all files from src_dir to dst_dir
    for file in os.listdir(src_dir):
        src_path = os.path.join(src_dir, file)
        dst_path = os.path.join(dst_dir, file)
        shutil.move(src_path, dst_path)

    # remove all remaining files and directories from src_dir
    for file in os.listdir(src_dir):
        file_path = os.path.join(src_dir, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    return

def get_filenames(folder):
    filenames = []
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):  # only include regular files, not directories
            filenames.append(file_path)
    return filenames


def reproduce_population(input_trees=".\\current_pop_trees\\", output=".\\another_pop\\test%d.txt",
                         num=10, depth=12):
    subprocess.run(['powershell.exe',
                    "conda activate grammarinator_env\ngrammarinator-generate.exe "
                    f"-l .\\bezBoolowUnlexer.py -p .\\bezBoolowUnparser.py -d {depth} -n {num} "
                    f" --population {input_trees} -o {output} "],
                   stdout=None, stderr=None)
    return

def mutate_individual(input_trees=".\\population\\", output=".\\another_pop\\test%d.txt",
                      num=1, depth=12):
    subprocess.run(['powershell.exe',
                    "conda activate grammarinator_env\ngrammarinator-generate.exe "
                    f"-l .\\bezBoolowUnlexer.py -p .\\bezBoolowUnparser.py -d {depth} -n {num} "
                    f" --population {input_trees} -o {output}   --no-recombine"],
                   stdout=None, stderr=None)
    return

def crossover_individuals(input_trees=".\\population\\", output=".\\another_pop\\test%d.txt",
                          num=2, depth=12):
    subprocess.run(['powershell.exe',
                    "conda activate grammarinator_env\ngrammarinator-generate.exe "
                    f"-l .\\bezBoolowUnlexer.py -p .\\bezBoolowUnparser.py -d {depth} -n {num} "
                    f" --population {input_trees} -o {output}  --no-mutate"],
                   stdout=None, stderr=None)
    return

def recursive_delete(dir):
    files = os.listdir(dir)
    for file in files:
        file_path = os.path.join(dir, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                recursive_delete(file_path)
        except Exception as e:
            print(e)
    return