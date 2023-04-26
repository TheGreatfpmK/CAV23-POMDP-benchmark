import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
result_folder = os.fsencode(dir_path + '/results/source')



def get_4x3_header():
    return "\\begin{tikzpicture}\n\\begin{axis}[\n\
    title={4x3-95},\n\
    xlabel={Time [min]},\n\
    ylabel={Value [Rmax]},\n\
    xmin=0, xmax=15,\n\
    ymin=1.7, ymax=1.9,\n\
    xtick={0,2,4,6,8,10,12,14},\n\
    ytick={1.7,1.74,1.78,1.82,1.86,1.9},\n\
    xtick pos=left,\n\
    ytick pos=left,\n\
    restrict y to domain=1.5:2.1,\n\
    ymajorgrids=true,\n\
    grid style=dashed,\n\
    height=8cm,\n\
    width=12cm,\n\
    legend style ={ at={(1.03,1)},\n\
        anchor=north west, draw=black, \n\
        fill=white,align=left},\n]\n"


def get_milos_header():
    return "\\begin{tikzpicture}\n\\begin{axis}[\n\
    title={Milos-97},\n\
    xlabel={Time [min]},\n\
    ylabel={Value [Rmax]},\n\
    xmin=0, xmax=15,\n\
    ymin=31, ymax=43,\n\
    xtick={0,2,4,6,8,10,12,14},\n\
    ytick={31,33,35,37,39,41,43},\n\
    xtick pos=left,\n\
    ytick pos=left,\n\
    restrict y to domain=25:50,\n\
    ymajorgrids=true,\n\
    grid style=dashed,\n\
    height=8cm,\n\
    width=12cm,\n\
    legend style ={ at={(1.03,1)},\n\
        anchor=north west, draw=black, \n\
        fill=white,align=left},\n]\n"


def get_refuel_header():
    return "\\begin{tikzpicture}\n\\begin{axis}[\n\
    title={Refuel-20},\n\
    xlabel={Time [min]},\n\
    ylabel={Value [Pmax]},\n\
    xmin=0, xmax=15,\n\
    ymin=0, ymax=0.25,\n\
    xtick={0,2,4,6,8,10,12,14},\n\
    ytick={0,0.05,0.1,0.15,0.2,0.25},\n\
    xtick pos=left,\n\
    ytick pos=left,\n\
    restrict y to domain=0:0.4,\n\
    ymajorgrids=true,\n\
    grid style=dashed,\n\
    height=8cm,\n\
    width=12cm,\n\
    legend style ={ at={(1.03,1)},\n\
        anchor=north west, draw=black, \n\
        fill=white,align=left},\n]\n"


def get_query_header():
    return "\\begin{tikzpicture}\n\\begin{axis}[\n\
    title={Query-s3},\n\
    xlabel={Time [min]},\n\
    ylabel={Value [Rmax]},\n\
    xmin=0, xmax=15,\n\
    ymin=415, ymax=515,\n\
    xtick={0,2,4,6,8,10,12,14},\n\
    ytick={415,435,455,475,495,515},\n\
    xtick pos=left,\n\
    ytick pos=left,\n\
    restrict y to domain=400:530,\n\
    ymajorgrids=true,\n\
    grid style=dashed,\n\
    height=8cm,\n\
    width=12cm,\n\
    legend style ={ at={(1.03,1)},\n\
        anchor=north west, draw=black, \n\
        fill=white,align=left},\n]\n"


def get_lanes_header():
    return "\\begin{tikzpicture}\n\\begin{axis}[\n\
    title={Lanes+},\n\
    xlabel={Time [min]},\n\
    ylabel={Value [Rmin]},\n\
    xmin=0, xmax=15,\n\
    ymin=4000, ymax=20000,\n\
    xtick={0,2,4,6,8,10,12,14},\n\
    ytick={4000,8000,12000,16000,20000},\n\
    xtick pos=left,\n\
    ytick pos=left,\n\
    restrict y to domain=2000:22000,\n\
    ymajorgrids=true,\n\
    y dir=reverse,\n\
    grid style=dashed,\n\
    height=8cm,\n\
    width=12cm,\n\
    legend style ={ at={(1.03,1)},\n\
        anchor=north west, draw=black, \n\
        fill=white,align=left},\n]\n"


def get_hallway_header():
    return "\\begin{tikzpicture}\n\\begin{axis}[\n\
    title={Hallway},\n\
    xlabel={Time [min]},\n\
    ylabel={Value [Rmin]},\n\
    xmin=0, xmax=15,\n\
    ymin=12, ymax=17,\n\
    xtick={0,2,4,6,8,10,12,14},\n\
    ytick={12,13,14,15,16,17},\n\
    xtick pos=left,\n\
    ytick pos=left,\n\
    restrict y to domain=10:20,\n\
    ymajorgrids=true,\n\
    y dir=reverse,\n\
    grid style=dashed,\n\
    height=8cm,\n\
    width=12cm,\n\
    legend style ={ at={(1.03,1)},\n\
        anchor=north west, draw=black, \n\
        fill=white,align=left},\n]\n"


def get_network_header():
    return "\\begin{tikzpicture}\n\\begin{axis}[\n\
    title={Network-3-8-20},\n\
    xlabel={Time [min]},\n\
    ylabel={Value [Rmin]},\n\
    xmin=0, xmax=15,\n\
    ymin=10, ymax=12,\n\
    xtick={0,2,4,6,8,10,12,14},\n\
    ytick={10,10.4,10.8,11.2,11.6,12},\n\
    xtick pos=left,\n\
    ytick pos=left,\n\
    restrict y to domain=8:14,\n\
    ymajorgrids=true,\n\
    y dir=reverse,\n\
    grid style=dashed,\n\
    height=8cm,\n\
    width=12cm,\n\
    legend style ={ at={(1.03,1)},\n\
        anchor=north west, draw=black, \n\
        fill=white,align=left},\n]\n"


def get_end(file):
    print("\\end{axis}\n\\end{tikzpicture}\n", file=file)


def get_plots(output_file, paynt_file, saynt_file, s1_file, s2_file, s3_file, s4_file, s5_file):

    # SAYNT
    saynt_log = saynt_file.read()
    saynt_storm_coordinates = ""
    saynt_paynt_coordinates = ""

    split1 = saynt_log.split("-----------Storm-----------")
    for i in range(len(split1)):
        if i > 0:
            split2 = split1[i].split()
            val = round(float(split2[2]),5)
            time = float(split2[7][:-1])
            time = round(time/60,2)
            saynt_storm_coordinates = saynt_storm_coordinates + f"({time}, {val})"

    print("\\addplot[\n\
    color=blue,\n\
    every mark/.append style={solid, fill=blue},\n\
    mark=square*,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + saynt_storm_coordinates + "\n\
    };\n\
    \\addlegendentry{SAYNT $F_{B}$};\n", file=output_file)

    split1 = saynt_log.split("-----------PAYNT-----------")
    for i in range(len(split1)):
        if i > 0:
            split2 = split1[i].split()
            val = round(float(split2[2]),5)
            time = float(split2[7][:-1])
            time = round(time/60,2)
            saynt_paynt_coordinates = saynt_paynt_coordinates + f"({time}, {val})"
    if time < 15.0:
        saynt_paynt_coordinates = saynt_paynt_coordinates + f"(15, {val})"

    print("\\addplot[\n\
    color=green,\n\
    every mark/.append style={solid, fill=green},\n\
    mark=triangle*,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + saynt_paynt_coordinates + "\n\
    };\n\
    \\addlegendentry{SAYNT $F_{I}$};\n", file=output_file)



    #Storm
    s1_log = s1_file.read()
    s2_log = s2_file.read()
    s3_log = s3_file.read()
    s4_log = s4_file.read()
    s5_log = s5_file.read()

    s_logs = [s1_log, s2_log, s3_log, s4_log, s5_log]

    storm_coordinates = ""

    for log in s_logs:
        split1 = log.split("-----------Storm-----------")
        for i in range(len(split1)):
            if i > 0:
                split2 = split1[i].split()
                val = round(float(split2[2]),5)
                time = float(split2[7][:-1])
                time = round(time/60,2)
                storm_coordinates = storm_coordinates + f"({time}, {val})"

    print("\\addplot[\n\
    color=violet,\n\
    every mark/.append style={solid, fill=violet},\n\
    mark=diamond*,\n\
    dashed,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + storm_coordinates + "\n\
    };\n\
    \\addlegendentry{Storm};\n", file=output_file)


    #PAYNT
    paynt_log = paynt_file.read()
    paynt_coordinates = ""

    split1 = paynt_log.split("-----------PAYNT-----------")
    for i in range(len(split1)):
        if i > 0:
            split2 = split1[i].split()
            val = round(float(split2[2]),5)
            time = float(split2[7][:-1])
            time = round(time/60,2)
            paynt_coordinates = paynt_coordinates + f"({time}, {val})"
    if time < 15.0:
        paynt_coordinates = paynt_coordinates + f"(15, {val})"

    print("\\addplot[\n\
    color=orange,\n\
    every mark/.append style={solid, fill=orange},\n\
    mark=*,\n\
    dashed,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + paynt_coordinates + "\n\
    };\n\
    \\addlegendentry{PAYNT};\n", file=output_file)



def get_plots_q(output_file, paynt_file, saynt_file, s1_file, s2_file, s3_file, s4_file, s5_file, q2_file, q11_file, q12_file, q13_file, q14_file, q15_file):

    # SAYNT
    saynt_log = saynt_file.read()
    saynt_storm_coordinates = ""
    saynt_paynt_coordinates = ""

    split1 = saynt_log.split("-----------Storm-----------")
    for i in range(len(split1)):
        if i > 0:
            split2 = split1[i].split()
            val = round(float(split2[2]),5)
            time = float(split2[7][:-1])
            time = round(time/60,2)
            saynt_storm_coordinates = saynt_storm_coordinates + f"({time}, {val})"

    print("\\addplot[\n\
    color=blue,\n\
    every mark/.append style={solid, fill=blue},\n\
    mark=square*,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + saynt_storm_coordinates + "\n\
    };\n\
    \\addlegendentry{SAYNT $F_{B}$};\n", file=output_file)

    split1 = saynt_log.split("-----------PAYNT-----------")
    for i in range(len(split1)):
        if i > 0:
            split2 = split1[i].split()
            val = round(float(split2[2]),5)
            time = float(split2[7][:-1])
            time = round(time/60,2)
            saynt_paynt_coordinates = saynt_paynt_coordinates + f"({time}, {val})"
    if time < 15.0:
        saynt_paynt_coordinates = saynt_paynt_coordinates + f"(15, {val})"

    print("\\addplot[\n\
    color=green,\n\
    every mark/.append style={solid, fill=green},\n\
    mark=triangle*,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + saynt_paynt_coordinates + "\n\
    };\n\
    \\addlegendentry{SAYNT $F_{I}$};\n", file=output_file)



    #Storm
    s1_log = s1_file.read()
    s2_log = s2_file.read()
    s3_log = s3_file.read()
    s4_log = s4_file.read()
    s5_log = s5_file.read()

    s_logs = [s1_log, s2_log, s3_log, s4_log, s5_log]

    storm_coordinates = ""

    for log in s_logs:
        split1 = log.split("-----------Storm-----------")
        for i in range(len(split1)):
            if i > 0:
                split2 = split1[i].split()
                val = round(float(split2[2]),5)
                time = float(split2[7][:-1])
                time = round(time/60,2)
                storm_coordinates = storm_coordinates + f"({time}, {val})"

    print("\\addplot[\n\
    color=violet,\n\
    every mark/.append style={solid, fill=violet},\n\
    mark=diamond*,\n\
    dashed,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + storm_coordinates + "\n\
    };\n\
    \\addlegendentry{Storm};\n", file=output_file)


    #PAYNT
    paynt_log = paynt_file.read()
    paynt_coordinates = ""

    split1 = paynt_log.split("-----------PAYNT-----------")
    for i in range(len(split1)):
        if i > 0:
            split2 = split1[i].split()
            val = round(float(split2[2]),5)
            time = float(split2[7][:-1])
            time = round(time/60,2)
            paynt_coordinates = paynt_coordinates + f"({time}, {val})"
    if time < 15.0:
        paynt_coordinates = paynt_coordinates + f"(15, {val})"

    print("\\addplot[\n\
    color=orange,\n\
    every mark/.append style={solid, fill=orange},\n\
    mark=*,\n\
    dashed,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + paynt_coordinates + "\n\
    };\n\
    \\addlegendentry{PAYNT};\n", file=output_file)


    # Q1
    s1_log = q11_file.read()
    s2_log = q12_file.read()
    s3_log = q13_file.read()
    s4_log = q14_file.read()
    s5_log = q15_file.read()

    s_logs = [s1_log, s2_log, s3_log, s4_log, s5_log]

    q1_coordinates = ""

    for log in s_logs:
        split1 = log.split("-----------Storm-----------")
        for i in range(len(split1)):
            if i > 0:
                split2 = split1[i].split()
                val = round(float(split2[2]),5)
                time = float(split2[7][:-1])
                time = round(time/60,2)
                q1_coordinates = q1_coordinates + f"({time}, {val})"

    print("\\addplot[\n\
    color=pink,\n\
    every mark/.append style={solid, fill=pink},\n\
    mark=otimes*,\n\
    dashdotdotted,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + q1_coordinates + "\n\
    };\n\
    \\addlegendentry{Q1 Storm};\n", file=output_file)


    # Q2
    q2_log = q2_file.read()
    q2_coordinates = ""

    split1 = q2_log.split("-----------PAYNT-----------")
    for i in range(len(split1)):
        if i > 0:
            split2 = split1[i].split()
            val = round(float(split2[2]),5)
            time = float(split2[7][:-1])
            time = round(time/60,2)
            q2_coordinates = q2_coordinates + f"({time}, {val})"
    if time < 15.0:
        q2_coordinates = q2_coordinates + f"(15, {val})"

    print("\\addplot[\n\
    color=yellow,\n\
    every mark/.append style={solid, fill=yellow},\n\
    mark=star,\n\
    dashdotdotted,\n\
    line width=1.5pt,mark size=2pt,]\n\
    coordinates {\n" + q2_coordinates + "\n\
    };\n\
    \\addlegendentry{Q2 PAYNT};\n", file=output_file)


def get_graphs():
    saynt_path = os.fsencode(dir_path + '/q3/saynt')
    paynt_path = os.fsencode(dir_path + '/q3/paynt')
    s5_path = os.fsencode(dir_path + '/q3/storm-5th')
    s4_path = os.fsencode(dir_path + '/q3/storm-4th')
    s3_path = os.fsencode(dir_path + '/q3/storm-3rd')
    s2_path = os.fsencode(dir_path + '/q3/storm-2nd')
    s1_path = os.fsencode(dir_path + '/q3/storm-1st')
    q15_path = os.fsencode(dir_path + '/q3/q1-5th')
    q14_path = os.fsencode(dir_path + '/q3/q1-4th')
    q13_path = os.fsencode(dir_path + '/q3/q1-3rd')
    q12_path = os.fsencode(dir_path + '/q3/q1-2nd')
    q11_path = os.fsencode(dir_path + '/q3/q1-1st')
    q2_path = os.fsencode(dir_path + '/q3/q2')

    models = [ f.path for f in os.scandir(paynt_path) if f.is_dir() ]

    for model in models:
        model_name = os.path.basename(model).decode("utf-8")

        try:

            saynt_file = open(saynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')

            paynt_file = open(paynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')

            s1_file = open(s1_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
            s2_file = open(s2_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
            s3_file = open(s3_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
            s4_file = open(s4_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
            s5_file = open(s5_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')

            if model_name in ["4x3-95", "query-s3", "lanes-100-combined-new"]:
                q2_file = open(q2_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                q11_file = open(q11_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                q12_file = open(q12_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                q13_file = open(q13_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                q14_file = open(q14_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                q15_file = open(q15_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')

            header = ""
            output_file_name = ""

            if model_name == "4x3-95":
                header = get_4x3_header()
                output_file_name = "source-figure4-q3-4x3-95.tex"
            elif model_name == "milos-aaai97":
                header = get_milos_header()
                output_file_name = "source-figure4-q3-milos-97.tex"
            elif model_name == "refuel-20":
                header = get_refuel_header()
                output_file_name = "source-figure4-q3-refuel-20.tex"
            elif model_name == "query-s3":
                header = get_query_header()
                output_file_name = "source-figure4-q3-query-s3.tex"
            elif model_name == "lanes-100-combined-new":
                header = get_lanes_header()
                output_file_name = "source-figure4-q3-lanes.tex"
            elif model_name == "hallway":
                header = get_hallway_header()
                output_file_name = "source-figure4-q3-hallway.tex"
            elif model_name == "network-3-8-20":
                header = get_network_header()
                output_file_name = "source-figure4-q3-network-3-8-20.tex"


            with open(result_folder.decode("utf-8") + "/" + output_file_name, "w") as text_file:
                print(header, file=text_file)
                if model_name in ["4x3-95", "query-s3", "lanes-100-combined-new"]:
                    get_plots_q(text_file, paynt_file, saynt_file, s1_file, s2_file, s3_file, s4_file, s5_file, q2_file, q11_file, q12_file, q13_file, q14_file, q15_file)
                else:
                    get_plots(text_file, paynt_file, saynt_file, s1_file, s2_file, s3_file, s4_file, s5_file)
                get_end(text_file)

                paynt_file.close()
                saynt_file.close()
                s1_file.close()
                s2_file.close()
                s3_file.close()
                s4_file.close()
                s5_file.close()

                if model_name in ["4x3-95", "query-s3", "lanes-100-combined-new"]:
                    q2_file.close()
                    q11_file.close()
                    q12_file.close()
                    q13_file.close()
                    q14_file.close()
                    q15_file.close()

                text_file.close()

        except:
            print(f"ERROR WHILE CREATING GRAPHS!!! Couldn't process logs for model {model_name} to create the graph!")
            continue


if __name__ == '__main__':

    if not os.path.isdir(dir_path + "/results"):
        os.mkdir(dir_path + "/results")

    if not os.path.isdir(dir_path + "/results/source"):
        os.mkdir(dir_path + "/results/source")

    get_graphs()