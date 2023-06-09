import sys
import os
from subprocess import DEVNULL, STDOUT, check_call

dir_path = os.path.dirname(os.path.realpath(__file__))
result_folder = os.fsencode(dir_path + '/output/results')
source_folder = os.fsencode(dir_path + '/output/results/source')


def get_start():
    return "\\documentclass{article}\n\
\\usepackage[utf8]{inputenc}\n\n\
\\usepackage{tikz}\n\
\\usepackage{pgfplots}\n\
\\pagenumbering{gobble}\n\n\
\\begin{document}\n"

def get_end():
    return "\\end{document}"

def get_table2():
    table_file = open(source_folder.decode("utf-8") + "/source-table2-models-info.tex", mode='r')
    table_contents = table_file.read()

    with open(source_folder.decode("utf-8") + "/table2-models-info.tex", "w") as text_file:
        print(get_start(), file=text_file)
        print(table_contents, file=text_file)
        print(get_end(), file=text_file)

        text_file.close()

    table_file.close()

    source_file = source_folder.decode("utf-8") + "/table2-models-info.tex"
    result_table_folder = result_folder.decode("utf-8") + "/table2"

    os.makedirs(result_table_folder, exist_ok=True)
    check_call(['pdflatex', f'--output-directory={result_table_folder}', source_file], stdout=DEVNULL, stderr=STDOUT)

    print(f"PDF for table2 generated to {result_table_folder}")


def get_table3_q1():
    table_file = open(source_folder.decode("utf-8") + "/source-table3-q1.tex", mode='r')
    table_contents = table_file.read()

    with open(source_folder.decode("utf-8") + "/table3-q1.tex", "w") as text_file:
        print(get_start(), file=text_file)
        print(table_contents, file=text_file)
        print(get_end(), file=text_file)

        text_file.close()

    table_file.close()

    source_file = source_folder.decode("utf-8") + "/table3-q1.tex"
    result_table_folder = result_folder.decode("utf-8") + "/table3-q1"

    os.makedirs(result_table_folder, exist_ok=True)
    check_call(['pdflatex', f'--output-directory={result_table_folder}', source_file], stdout=DEVNULL, stderr=STDOUT)

    print(f"PDF for table3-q1 generated to {result_table_folder}")

        

def get_table3_q2():
    table_file = open(source_folder.decode("utf-8") + "/source-table3-q2.tex", mode='r')
    table_contents = table_file.read()

    with open(source_folder.decode("utf-8") + "/table3-q2.tex", "w") as text_file:
        print(get_start(), file=text_file)
        print(table_contents, file=text_file)
        print(get_end(), file=text_file)

        text_file.close()

    table_file.close()

    source_file = source_folder.decode("utf-8") + "/table3-q2.tex"
    result_table_folder = result_folder.decode("utf-8") + "/table3-q2"

    os.makedirs(result_table_folder, exist_ok=True)
    check_call(['pdflatex', f'--output-directory={result_table_folder}', source_file], stdout=DEVNULL, stderr=STDOUT)

    print(f"PDF for table3-q2 generated to {result_table_folder}")



def get_table4():
    table_file = open(source_folder.decode("utf-8") + "/source-table4-FSC-size.tex", mode='r')
    table_contents = table_file.read()

    with open(source_folder.decode("utf-8") + "/table4-FSC-size.tex", "w") as text_file:
        print(get_start(), file=text_file)
        print(table_contents, file=text_file)
        print(get_end(), file=text_file)

        text_file.close()

    table_file.close()

    source_file = source_folder.decode("utf-8") + "/table4-FSC-size.tex"
    result_table_folder = result_folder.decode("utf-8") + "/table4"

    os.makedirs(result_table_folder, exist_ok=True)
    check_call(['pdflatex', f'--output-directory={result_table_folder}', source_file], stdout=DEVNULL, stderr=STDOUT)

    print(f"PDF for table4 generated to {result_table_folder}")


def get_string_if_file_exists(path):
    try:
        source_file = open(path, mode='r')
        source_string = source_file.read()
        source_file.close()
        return source_string
    except:
        return ""


def get_figure4():
    string_4x3 = get_string_if_file_exists(source_folder.decode("utf-8") + "/source-figure4-q3-4x3-95.tex")
    string_lanes = get_string_if_file_exists(source_folder.decode("utf-8") + "/source-figure4-q3-lanes.tex")
    string_milos = get_string_if_file_exists(source_folder.decode("utf-8") + "/source-figure4-q3-milos-97.tex")
    string_hallway = get_string_if_file_exists(source_folder.decode("utf-8") + "/source-figure4-q3-hallway.tex")
    string_network = get_string_if_file_exists(source_folder.decode("utf-8") + "/source-figure4-q3-network-3-8-20.tex")
    string_query = get_string_if_file_exists(source_folder.decode("utf-8") + "/source-figure4-q3-query-s3.tex")
    string_refuel = get_string_if_file_exists(source_folder.decode("utf-8") + "/source-figure4-q3-refuel-20.tex")

    figure_contents = string_4x3 + string_lanes + string_milos + string_hallway + string_network + string_query + string_refuel

    with open(source_folder.decode("utf-8") + "/figure4.tex", "w") as text_file:
        print(get_start(), file=text_file)
        print(figure_contents, file=text_file)
        print(get_end(), file=text_file)

        text_file.close()

    source_file = source_folder.decode("utf-8") + "/figure4.tex"
    result_table_folder = result_folder.decode("utf-8") + "/figure4"

    os.makedirs(result_table_folder, exist_ok=True)
    check_call(['pdflatex', f'--output-directory={result_table_folder}', source_file], stdout=DEVNULL, stderr=STDOUT)

    print(f"PDF for figure4 generated to {result_table_folder}")



def get_appendix():
    table_file = open(source_folder.decode("utf-8") + "/source-appendix-C-table.tex", mode='r')
    table_contents = table_file.read()

    with open(source_folder.decode("utf-8") + "/appendix-C-table.tex", "w") as text_file:
        print(get_start(), file=text_file)
        print(table_contents, file=text_file)
        print(get_end(), file=text_file)

        text_file.close()

    table_file.close()

    source_file = source_folder.decode("utf-8") + "/appendix-C-table.tex"
    result_table_folder = result_folder.decode("utf-8") + "/appendix-C-table"

    os.makedirs(result_table_folder, exist_ok=True)
    check_call(['pdflatex', f'--output-directory={result_table_folder}', source_file], stdout=DEVNULL, stderr=STDOUT)

    print(f"PDF for appendix generated to {result_table_folder}")


def get_q3_table():
    table_file = open(source_folder.decode("utf-8") + "/source-q3-table-form.tex", mode='r')
    table_contents = table_file.read()

    with open(source_folder.decode("utf-8") + "/q3-table-form.tex", "w") as text_file:
        print(get_start(), file=text_file)
        print(table_contents, file=text_file)
        print(get_end(), file=text_file)

        text_file.close()

    table_file.close()

    source_file = source_folder.decode("utf-8") + "/q3-table-form.tex"
    result_table_folder = result_folder.decode("utf-8") + "/q3-in-table-form"

    os.makedirs(result_table_folder, exist_ok=True)
    check_call(['pdflatex', f'--output-directory={result_table_folder}', source_file], stdout=DEVNULL, stderr=STDOUT)

    print(f"PDF for q3-table generated to {result_table_folder}")


if __name__ == '__main__':
    pdf = sys.argv[1]

    if pdf == "models":
        get_table2()
    elif pdf == "q1":
        get_table3_q1()
    elif pdf == "q2":
        get_table3_q2()
    elif pdf == "memory":
        get_table4()
    elif pdf == "q3-figure":
        get_figure4()
    elif pdf == "appendix":
        get_appendix()
    elif pdf == "q3-table":
        get_q3_table()
    elif pdf == "all":
        get_table2()
        get_table3_q1()
        get_table3_q2()
        get_table4()
        get_figure4()
        get_appendix()