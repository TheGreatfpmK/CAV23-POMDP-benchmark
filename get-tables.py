import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
result_folder = os.fsencode(dir_path + '/output/results/source')

def get_models_info_table():
    models_info_path = os.fsencode(dir_path + '/output/models-info')
    models = [ f.path for f in os.scandir(models_info_path) if f.is_dir() ]

    with open(result_folder.decode("utf-8") + "/" + "source-table2-models-info.tex", "w") as text_file:    
        print("\\begin{table}", file=text_file)
        print("\\begin{tabular}{|c|ccc|c|}", file=text_file)
        print("\\hline\n", file=text_file)
        print("Model & $|S|$ & $|Act|$ & $|Z|$ & Over-app. \\\\ \\hline \n", file=text_file)

        for model in models:
            try:
                model_name = os.path.basename(model).decode("utf-8")

                model_file = open(model.decode("utf-8") + "/logs.txt", mode='r')
                model_log = model_file.read()

                split1 = model_log.split("constructed explicit quotient having ")
                split2 = split1[1].split()
                states = int(split2[0])
                actions = int(split2[3])

                split1 = model_log.split("Constructed POMDP having ")
                split2 = split1[1].split()
                observations = int(split2[0])

                split1 = model_log.split(".....")
                split2 = split1[1].split()
                overapp = 0.0
                overapp = round(float(split2[0]),2)
                if str(overapp) == "inf":
                    overapp = round(float(split2[1]),2)

                print(f'{model_name} & {states} & {actions} & {observations} & {overapp} \\\\', file=text_file)

                model_file.close()
            except:
                print(f"ERROR WHILE CREATING TABLES!!! Couldn't process logs for model {model_name} for table2-models-info!")
                continue


        print("\\hline", file=text_file)
        print("\\end{tabular}", file=text_file)
        print("\\end{table}\n", file=text_file)
        text_file.close()


def get_q1_table():
    short_s_path = os.fsencode(dir_path + '/output/q1/short-storm')
    long_s_path = os.fsencode(dir_path + '/output/q1/long-storm')
    im_short_s_path = os.fsencode(dir_path + '/output/q1/improved-short-storm')
    im_long_s_path = os.fsencode(dir_path + '/output/q1/improved-long-storm')

    models = [ f.path for f in os.scandir(short_s_path) if f.is_dir() ]

    with open(result_folder.decode("utf-8") + "/" + "source-table3-q1.tex", "w") as text_file:    
        print("\\begin{table}", file=text_file)
        print("\\begin{tabular}{|c|r|r|r|r|r|}", file=text_file)
        print("\\hline\n", file=text_file)
        print("Model & PAYNT & Short Storm & Short Storm + $F_{I}$ & Long Storm & Long Storm + $F_{I}$ \\\\ \\hline \n", file=text_file)

        for model in models:
            try:
                model_name = os.path.basename(model).decode("utf-8")

                short_s_file = open(short_s_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                short_s_log = short_s_file.read()

                long_s_file = open(long_s_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                long_s_log = long_s_file.read()

                im_short_s_file = open(im_short_s_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                im_short_s_log = im_short_s_file.read()

                im_long_s_file = open(im_long_s_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                im_long_s_log = im_long_s_file.read()


                split1 = im_short_s_log.split("-----------PAYNT-----------")
                split2 = split1[-1].split()
                p_val = round(float(split2[2]),2)
                p_time = split2[7]

                split1 = short_s_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                short_s_val = round(float(split2[2]),2)
                short_s_time = split2[7]

                split1 = long_s_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                long_s_val = round(float(split2[2]),2)
                long_s_time = split2[7]

                split1 = im_short_s_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                im_short_s_val = round(float(split2[2]),2)
                im_short_s_time = split2[7]

                split1 = im_long_s_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                im_long_s_val = round(float(split2[2]),2)
                im_long_s_time = split2[7]

                print(f'{model_name} & {p_val} & {short_s_val} & {im_short_s_val} & {long_s_val} & {im_long_s_val} \\\\', file=text_file)
                print(f' & {p_time} & {short_s_time} & {im_short_s_time} & {long_s_time} & {im_long_s_time} \\\\', file=text_file)
                print("\\hline", file=text_file)

                short_s_file.close()
                long_s_file.close()
                im_short_s_file.close()
                im_long_s_file.close()

            except:
                print(f"ERROR WHILE CREATING TABLES!!! Couldn't process logs for model {model_name} for table3-q1!")
                continue


        print("\\end{tabular}", file=text_file)
        print("\\end{table}\n", file=text_file)
        text_file.close()


def get_q2_table():
    paynt_path = os.fsencode(dir_path + '/output/q2/paynt')
    im_paynt_path = os.fsencode(dir_path + '/output/q2/improved-paynt')

    models = [ f.path for f in os.scandir(paynt_path) if f.is_dir() ]

    with open(result_folder.decode("utf-8") + "/" + "source-table3-q2.tex", "w") as text_file:    
        print("\\begin{table}", file=text_file)
        print("\\begin{tabular}{|c|r|r|r|}", file=text_file)
        print("\\hline\n", file=text_file)
        print("Model & Storm & PAYNT & PAYNT + $F_{B}$ \\\\ \\hline \n", file=text_file)

        for model in models:
            try:
                model_name = os.path.basename(model).decode("utf-8")

                paynt_file = open(paynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                paynt_log = paynt_file.read()

                im_paynt_file = open(im_paynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                im_paynt_log = im_paynt_file.read()

                split1 = im_paynt_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                s_val = round(float(split2[2]),2)
                s_time = split2[7]

                split1 = paynt_log.split("-----------PAYNT-----------")
                split2 = split1[-1].split()
                paynt_val = round(float(split2[2]),2)
                paynt_time = split2[7]

                split1 = im_paynt_log.split("-----------PAYNT-----------")
                split2 = split1[-1].split()
                im_paynt_val = round(float(split2[2]),2)
                im_paynt_time = split2[7]

                print(f'{model_name} & {s_val} & {paynt_val} & {im_paynt_val} \\\\', file=text_file)
                print(f' & {s_time} & {paynt_time} & {im_paynt_time} \\\\', file=text_file)
                print("\\hline", file=text_file)

                paynt_file.close()
                im_paynt_file.close()

            except:
                print(f"ERROR WHILE CREATING TABLES!!! Couldn't process logs for model {model_name} for table3-q2!")
                continue


        print("\\end{tabular}", file=text_file)
        print("\\end{table}\n", file=text_file)
        text_file.close()

def get_q3_table():
    saynt_path = os.fsencode(dir_path + '/output/q3/saynt')
    paynt_path = os.fsencode(dir_path + '/output/q3/paynt')
    s1_path = os.fsencode(dir_path + '/output/q3/storm-5th')
    s2_path = os.fsencode(dir_path + '/output/q3/storm-4th')
    s3_path = os.fsencode(dir_path + '/output/q3/storm-3rd')
    s4_path = os.fsencode(dir_path + '/output/q3/storm-2nd')
    s5_path = os.fsencode(dir_path + '/output/q3/storm-1st')

    models = [ f.path for f in os.scandir(paynt_path) if f.is_dir() ]

    with open(result_folder.decode("utf-8") + "/" + "source-q3-table-form.tex", "w") as text_file:    
        print("\\begin{table}", file=text_file)
        print("\\begin{tabular}{|c|rr|rr|rr|rr|}", file=text_file)
        print("\\hline\n", file=text_file)
        print("Model & PAYNT & & Storm & & SAYNT & & SAYNT & \\\\ \n", file=text_file)
        print(" & $F_{I}$ & Size & $F_{B}$ & Size & $F_{B}$ & Size & $F_{I}$ & Size \\\\ \\hline \n", file=text_file)

        for model in models:
            try:
                model_name = os.path.basename(model).decode("utf-8")

                saynt_file = open(saynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                saynt_log = saynt_file.read()

                paynt_file = open(paynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                paynt_log = paynt_file.read()

                s_file = open(s1_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                s_log = s_file.read()

                if s_log.find("-----------Storm-----------") == -1:
                    s_file.close()
                    s_file = open(s2_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                    s_log = s_file.read()

                    if s_log.find("-----------Storm-----------") == -1:
                        s_file.close()
                        s_file = open(s3_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                        s_log = s_file.read()

                        if s_log.find("-----------Storm-----------") == -1:
                            s_file.close()
                            s_file = open(s4_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                            s_log = s_file.read()

                            if s_log.find("-----------Storm-----------") == -1:
                                s_file.close()
                                s_file = open(s5_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                                s_log = s_file.read()

                split1 = paynt_log.split("-----------PAYNT-----------")
                split2 = split1[-1].split()
                paynt_val = round(float(split2[2]),2)
                paynt_time = split2[7]
                paynt_size = split2[12]

                split1 = s_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                s_val = round(float(split2[2]),2)
                s_time = split2[7]
                s_size = split2[12]

                split1 = saynt_log.split("-----------PAYNT-----------")
                split2 = split1[-1].split()
                saynt_p_val = round(float(split2[2]),2)
                saynt_p_time = split2[7]
                saynt_p_size = split2[12]

                split1 = saynt_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                saynt_s_val = round(float(split2[2]),2)
                saynt_s_time = split2[7]
                saynt_s_size = split2[12]

                print(f'{model_name} & {paynt_val} & {paynt_size} & {s_val} & {s_size} & {saynt_s_val} & {saynt_s_size} & {saynt_p_val} & {saynt_p_size} \\\\', file=text_file)
                print(f' & {paynt_time} & & {s_time} & & {saynt_s_time} & & {saynt_p_time} & \\\\', file=text_file)
                print("\\hline", file=text_file)

                saynt_file.close()
                paynt_file.close()
                s_file.close()

            except:
                print(f"ERROR WHILE CREATING TABLES!!! Couldn't process logs for model {model_name} for q3-table-form!")
                continue


        print("\\end{tabular}", file=text_file)
        print("\\end{table}\n", file=text_file)
        text_file.close()


def get_memory_table():
    saynt_path = os.fsencode(dir_path + '/output/q3/saynt')

    models = [ f.path for f in os.scandir(saynt_path) if f.is_dir() ]

    with open(result_folder.decode("utf-8") + "/" + "source-table4-FSC-size.tex", "w") as text_file:    
        print("\\begin{table}", file=text_file)
        print("\\begin{tabular}{|c|c|c|}", file=text_file)
        print("\\hline\n", file=text_file)
        print("Model & $F_{B}$ & $F_{I}$ \\\\ \\hline \n", file=text_file)

        for model in models:
            try:
                model_name = os.path.basename(model).decode("utf-8")

                if model_name not in ["hallway", "refuel-20", "query-s3", "lanes-100-combined-new", "network-3-8-20", "refuel-06", "drone-8-2"]:
                    continue

                saynt_file = open(saynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                saynt_log = saynt_file.read()

                split1 = saynt_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                s_val = round(float(split2[2]),2)
                s_size = split2[12]

                split1 = saynt_log.split("-----------PAYNT-----------")
                split2 = split1[-1].split()
                paynt_val = round(float(split2[2]),2)
                paynt_size = split2[12]

                print(f'{model_name} & {s_val}/{s_size} & {paynt_val}/{paynt_size} \\\\', file=text_file)
                print("\\hline", file=text_file)

                saynt_file.close()

            except:
                print(f"ERROR WHILE CREATING TABLES!!! Couldn't process logs for model {model_name} for table4-FSC-size!")
                continue


        print("\\end{tabular}", file=text_file)
        print("\\end{table}\n", file=text_file)
        text_file.close()


def get_appendix_table():
    saynt_path = os.fsencode(dir_path + '/output/appendix/saynt')
    paynt_path = os.fsencode(dir_path + '/output/appendix/paynt')
    s1_path = os.fsencode(dir_path + '/output/appendix/storm-5th')
    s2_path = os.fsencode(dir_path + '/output/appendix/storm-4th')
    s3_path = os.fsencode(dir_path + '/output/appendix/storm-3rd')
    s4_path = os.fsencode(dir_path + '/output/appendix/storm-2nd')
    s5_path = os.fsencode(dir_path + '/output/appendix/storm-1st')

    models = [ f.path for f in os.scandir(paynt_path) if f.is_dir() ]

    with open(result_folder.decode("utf-8") + "/" + "source-appendix-C-table.tex", "w") as text_file:    
        print("\\begin{table}", file=text_file)
        print("\\begin{tabular}{|c|rr|rr|rr|rr|}", file=text_file)
        print("\\hline\n", file=text_file)
        print("Model & PAYNT & & Storm & & SAYNT & & SAYNT & \\\\ \n", file=text_file)
        print(" & $F_{I}$ & Size & $F_{B}$ & Size & $F_{B}$ & Size & $F_{I}$ & Size \\\\ \\hline \n", file=text_file)

        for model in models:
            try:
                model_name = os.path.basename(model).decode("utf-8")

                saynt_file = open(saynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                saynt_log = saynt_file.read()

                paynt_file = open(paynt_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                paynt_log = paynt_file.read()

                s_file = open(s1_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                s_log = s_file.read()

                if s_log.find("-----------Storm-----------") == -1:
                    s_file.close()
                    s_file = open(s2_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                    s_log = s_file.read()

                    if s_log.find("-----------Storm-----------") == -1:
                        s_file.close()
                        s_file = open(s3_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                        s_log = s_file.read()

                        if s_log.find("-----------Storm-----------") == -1:
                            s_file.close()
                            s_file = open(s4_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                            s_log = s_file.read()

                            if s_log.find("-----------Storm-----------") == -1:
                                s_file.close()
                                s_file = open(s5_path.decode("utf-8") + "/" + model_name + "/logs.txt", mode='r')
                                s_log = s_file.read()

                split1 = paynt_log.split("-----------PAYNT-----------")
                split2 = split1[-1].split()
                paynt_val = round(float(split2[2]),2)
                paynt_time = split2[7]
                paynt_size = split2[12]

                split1 = s_log.split("-----------Storm-----------")
                split2 = split1[-1].split()
                s_val = round(float(split2[2]),2)
                s_time = split2[7]
                s_size = split2[12]

                split1 = saynt_log.split("-----------PAYNT-----------")
                if len(split1) > 2:
                    for i in range(len(split1)-2):
                        split2 = split1[-i-1].split()
                        saynt_p_val = round(float(split2[2]),2)
                        split3 = split1[-i-2].split()
                        saynt_p_val2 = round(float(split3[2]),2)
                        if saynt_p_val != saynt_p_val2:
                            break
                    saynt_p_time = split2[7]
                    saynt_p_size = split2[12]
                else:
                    split2 = split1[-1].split()
                    saynt_p_val = round(float(split2[2]),2)
                    saynt_p_time = split2[7]
                    saynt_p_size = split2[12]

                split1 = saynt_log.split("-----------Storm-----------")
                if len(split1) > 2:
                    for i in range(len(split1)-2):
                        split2 = split1[-i-1].split()
                        saynt_s_val = round(float(split2[2]),2)
                        split3 = split1[-i-2].split()
                        saynt_s_val2 = round(float(split3[2]),2)
                        if saynt_s_val != saynt_s_val2:
                            break
                    saynt_s_time = split2[7]
                    saynt_s_size = split2[12]
                else:
                    split2 = split1[-1].split()
                    saynt_s_val = round(float(split2[2]),2)
                    saynt_s_time = split2[7]
                    saynt_s_size = split2[12]

                print(f'{model_name} & {paynt_val} & {paynt_size} & {s_val} & {s_size} & {saynt_s_val} & {saynt_s_size} & {saynt_p_val} & {saynt_p_size} \\\\', file=text_file)
                print(f' & {paynt_time} & & {s_time} & & {saynt_s_time} & & {saynt_p_time} & \\\\', file=text_file)
                print("\\hline", file=text_file)

                saynt_file.close()
                paynt_file.close()
                s_file.close()

            except:
                print(f"ERROR WHILE CREATING TABLES!!! Couldn't process logs for model {model_name} for appendix-C-table!")
                continue


        print("\\end{tabular}", file=text_file)
        print("\\end{table}\n", file=text_file)
        text_file.close()



if __name__ == '__main__':
    table = sys.argv[1]

    if not os.path.isdir(dir_path + "/output/results"):
        os.mkdir(dir_path + "/output/results")

    if not os.path.isdir(dir_path + "/output/results/source"):
        os.mkdir(dir_path + "/output/results/source")

    if table == "models":
        get_models_info_table()

    if table == "q1":
        get_q1_table()

    if table == "q2":
        get_q2_table()

    if table == "q3-table":
        get_q3_table()

    if table == "memory":
        get_memory_table()

    if table == "appendix":
        get_appendix_table()  

    if table == "all":
        get_models_info_table()
        get_q1_table()
        get_q2_table()
        get_memory_table()
        get_appendix_table() 

