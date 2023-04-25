import os
import subprocess
import signal
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

# If you feel like your PC is struggling to achieve correct values in the given timeout
# because of performance issues try incresing this multiplier
# default = 1, if you set it to 2 all timeout settings will be multiplied by 2
timeout_multiplier = 1

# If true overwrite existing logs, if false only run experiments for missing log files
overwrite_logs = False

# If true FSCs will be exported alongside the log files
export_fsc = False

# SETTINGS FOR EXPERIMENTS
# use_storm = False                   # False if you want just PAYNT result
# iterative_storm = False   # False if you dont want iterative loop, otherwise (timeout, paynt_timeout, storm_timeout)
# get_storm_result = 0            # Put integer to represent number of seconds to just get storm result, False to turn off
# storm_options = "2mil"               # False to use default, otherwise one of [cutoff,clip2,clip4...]
# prune_storm = True                 # Family pruning based on storm, default False
# unfold_strategy = "cutoff"            # False to use default, otherwise one of [paynt,storm,cutoff]
# use_storm_cutoff = True            # Use Storm cutoff schedulers to prioritize family exploration, default False
# aposteriori_unfolding = False       # Enables new unfolding

# Parsing options to options string
# example options string: "--storm-pomdp --iterative-storm 600 12 12"
# if use_storm:
#     options_string = "--storm-pomdp"
#     if iterative_storm:
#         options_string += " --iterative-storm {} {} {}".format(iterative_storm[0], iterative_storm[1], iterative_storm[2])
#     if get_storm_result:
#         options_string += " --get-storm-result {}".format(get_storm_result)
#     if storm_options:
#         options_string += " --storm-options {}".format(storm_options)
#     if prune_storm:
#         options_string += " --prune-storm"
#     if unfold_strategy:
#         options_string += " --unfold-strategy-storm {}".format(unfold_strategy)
#     if use_storm_cutoff:
#         options_string += " --use-storm-cutoffs"
#     if aposteriori_unfolding:
#         options_string += " --posterior-aware"
# else:
#     options_string = ""

# CHANGE THIS TO CHANGE WHAT MODELS SHOULD BE USED
directory = os.fsencode(dir_path + '/../models/pomdp/storm-integration')
models = [ f.path for f in os.scandir(directory) if f.is_dir() ]

def run_experiment(options, logs_string, experiment_models, timeout, special={}):
    
    logs_dir = os.fsencode(dir_path + "/{}/".format(logs_string))

    print(f'\nRunning experiment {logs_string}. The logs will be saved in folder {logs_dir.decode("utf-8")}')
    print(f'The options used: "{options}"\n')

    real_timeout = int(timeout*timeout_multiplier)

    for model in models:
        model_name = os.path.basename(model).decode("utf-8")
        project_name = model.decode("utf-8")

        if model_name in special.keys():
            model_options = special[model_name]
        else:
            model_options = options

        export_command = ""
        if export_fsc:
            paynt_export_path = logs_dir.decode("utf-8") + model_name
            storm_export_path = logs_dir.decode("utf-8") + model_name
            export_command = f"--export-fsc-storm {storm_export_path} --export-fsc-paynt {paynt_export_path}"

        # THE REST OF THE MODELS
        command = "python3 paynt.py --project {} --fsc-synthesis {} {}".format(project_name, model_options, export_command)
        if model_name in ["4x3-95", "4x5x2-95", "hallway", "hallway2", "milos-aaai97", "mini-hall2", "network", "query-s2", "query-s3", "stand-tiger-95", "web-mall"]:
            command = "python3 paynt.py --project {} --fsc-synthesis {} --filetype drn {}".format(project_name, model_options, export_command)

        if model_name not in experiment_models:
            continue

        if not overwrite_logs:
            if os.path.isfile(logs_dir.decode("utf-8") + model_name + "/" + "logs.txt"):
                print(model_name, "LOG EXISTS")
                continue

        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            # TIMEOUT HERE TO TERMINATE EXPERIMENT
            # timeout should be higher than the expected running time of a given experiment
            output, error = process.communicate(timeout=real_timeout)
            output, error = process.communicate()
            process.wait()
        except subprocess.TimeoutExpired:
            process.send_signal(signal.SIGKILL)
            output, error = process.communicate()
            process.wait()

        if os.path.isfile(logs_dir.decode("utf-8") + model_name + "/" + "logs.txt"):
            print(model_name, "OVERWRITEN LOG")
            os.remove(logs_dir.decode("utf-8") + model_name + "/" + "logs.txt")
        else:
            print(model_name)

        if os.path.isfile(logs_dir.decode("utf-8") + model_name + "/" + "stderr.txt"):    
            os.remove(logs_dir.decode("utf-8") + model_name + "/" + "stderr.txt")

        os.makedirs(os.path.dirname(logs_dir.decode("utf-8") + model_name + "/" + "logs.txt"), exist_ok=True)
        with open(logs_dir.decode("utf-8") + model_name + "/" + "logs.txt", "w") as text_file:
            text_file.write(output.decode("utf-8"))

        # TODO remove after
        if error:
            with open(logs_dir.decode("utf-8") + model_name + "/" + "stderr.txt", "w") as text_file:
                text_file.write(error.decode("utf-8"))

    print(f'\nExperiment {logs_string} completed. The logs are saved in folder {logs_dir.decode("utf-8")}')

if __name__ == '__main__':
    experiment = sys.argv[1]
    overwrite = sys.argv[2]
    overwrite_logs = overwrite == "True"
    export_fsc = len(sys.argv) > 3

    if experiment == 'motivation':
        pass

    if experiment == 'models':
        experiment_models = ["4x3-95", "4x5x2-95", "hallway", "milos-aaai97", "network", "query-s3", "stand-tiger-95", "drone-4-2", "drone-8-2", "lanes-100-combined-new", "network-3-8-20", "refuel-06", "refuel-20", "rocks-12"]
        options = "--storm-pomdp --get-storm-result 0 --storm-options overapp"
        logs_string = "models-info"
        timeout=200
        run_experiment(options, logs_string, experiment_models, timeout)

    elif experiment == 'q1':
        experiment_models = ["drone-4-2", "network", "drone-8-2", "4x3-95", "query-s3", "milos-aaai97", "hallway", "rocks-12"]

        # PAYNT
        #options = ""
        #logs_string = "q1/paynt"
        #timeout = 100
        #run_experiment(options, logs_string, experiment_models, timeout)

        # Short Storm
        options = "--storm-pomdp --get-storm-result 0"
        logs_string = "q1/short-storm"
        timeout = 100
        run_experiment(options, logs_string, experiment_models, timeout)

        # Short Storm + Fi
        options = "--storm-pomdp --get-storm-result 10"
        logs_string = "q1/improved-short-storm"
        timeout = 100
        special = {"drone-8-2": "--storm-pomdp --get-storm-result 60", "rocks-12": "--storm-pomdp --get-storm-result 60"}
        run_experiment(options, logs_string, experiment_models, timeout, special)

        # Long Storm
        options = "--storm-pomdp --get-storm-result 0 --storm-options 5mil"
        logs_string = "q1/long-storm"
        timeout = 300
        special = {"rocks-12": "--storm-pomdp --get-storm-result 0 --storm-options clip4"}
        run_experiment(options, logs_string, experiment_models, timeout, special)

        # Long Storm + Fi
        options = "--storm-pomdp --get-storm-result 10 --storm-options 5mil"
        logs_string = "q1/improved-long-storm"
        timeout = 300
        special = {"drone-8-2": "--storm-pomdp --get-storm-result 60 --storm-options 5mil", "rocks-12": "--storm-pomdp --get-storm-result 60 --storm-options clip4"}
        run_experiment(options, logs_string, experiment_models, timeout, special)

        print("\nQ1 EXPERIMENT COMPLETE\n")

    elif experiment == 'q2':
        experiment_models = ["4x5x2-95", "refuel-20", "stand-tiger-95", "4x3-95", "refuel-06", "milos-aaai97", "network-3-8-20", "rocks-12"]
        
        # Storm
        #options = "--storm-pomdp --get-storm-result 0"
        #logs_string = "q2/storm"
        #timeout = 60
        #run_experiment(options, logs_string, experiment_models, timeout)

        # PAYNT
        options = ""
        logs_string = "q2/paynt"
        timeout = 300
        run_experiment(options, logs_string, experiment_models, timeout)

        # PAYNT + Fb
        options = "--storm-pomdp"
        logs_string = "q2/improved-paynt"
        timeout = 300
        special = {"rocks-12": "--storm-pomdp --use-storm-cutoffs"}
        run_experiment(options, logs_string, experiment_models, timeout, special)

        print("\nQ2 EXPERIMENT COMPLETE\n")

    elif experiment == 'q3':
        experiment_models = ["hallway", "refuel-20", "query-s3", "4x3-95", "lanes-100-combined-new", "milos-aaai97", "network-3-8-20"]
        saynt_experiment_models = ["hallway", "refuel-20", "query-s3", "4x3-95", "lanes-100-combined-new", "milos-aaai97", "network-3-8-20", "refuel-06", "drone-8-2"]

        # PAYNT
        options = ""
        logs_string = "q3/paynt"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)
        
        # Storm
        options = "--storm-pomdp --get-storm-result 0"
        logs_string = "q3/storm-1st"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        options = "--storm-pomdp --get-storm-result 0 --storm-options 2mil"
        logs_string = "q3/storm-2nd"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        options = "--storm-pomdp --get-storm-result 0 --storm-options 5mil"
        logs_string = "q3/storm-3rd"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        options = "--storm-pomdp --get-storm-result 0 --storm-options 10mil"
        logs_string = "q3/storm-4th"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        options = "--storm-pomdp --get-storm-result 0 --storm-options 20mil"
        logs_string = "q3/storm-5th"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        # SAYNT
        options = "--storm-pomdp --iterative-storm 900 60 10"
        logs_string = "q3/saynt"
        timeout = 1200
        special = {"4x3-95": "--storm-pomdp --iterative-storm 900 60 10 --posterior-aware", "milos-aaai97": "--storm-pomdp --iterative-storm 900 90 10",
                   "query-s3": "--storm-pomdp --iterative-storm 900 90 10"}
        run_experiment(options, logs_string, saynt_experiment_models, timeout, special)

        print("\nQ3 EXPERIMENT COMPLETE\n")

    elif experiment == 'appendix':
        
        experiment_models = ["4x3-95", "4x5x2-95", "drone-4-1", "drone-4-2", "drone-8-2", "hallway", "lanes-100-combined-new", "milos-aaai97", "network",
                             "network-2-8-20", "network-3-8-20", "query-s3", "refuel-06", "refuel-08", "refuel-20", "stand-tiger-95"]

        # PAYNT
        options = ""
        logs_string = "appendix/paynt"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)
        
        # Storm
        options = "--storm-pomdp --get-storm-result 0"
        logs_string = "appendix/storm-1st"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        options = "--storm-pomdp --get-storm-result 0 --storm-options 2mil"
        logs_string = "appendix/storm-2nd"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        options = "--storm-pomdp --get-storm-result 0 --storm-options 5mil"
        logs_string = "appendix/storm-3rd"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        options = "--storm-pomdp --get-storm-result 0 --storm-options 10mil"
        logs_string = "appendix/storm-4th"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        options = "--storm-pomdp --get-storm-result 0 --storm-options 20mil"
        logs_string = "appendix/storm-5th"
        timeout = 1000
        run_experiment(options, logs_string, experiment_models, timeout)

        # SAYNT
        options = "--storm-pomdp --iterative-storm 900 60 10"
        logs_string = "appendix/saynt"
        timeout = 1200
        special = {"4x3-95": "--storm-pomdp --iterative-storm 900 60 10 --posterior-aware", "milos-aaai97": "--storm-pomdp --iterative-storm 900 90 10",
                   "query-s3": "--storm-pomdp --iterative-storm 900 90 10", "drone-4-1": "--storm-pomdp --iterative-storm 900 60 10 --posterior-aware"}
        run_experiment(options, logs_string, experiment_models, timeout, special)

    else:
        print("Provide experiment set name (q1, q2, q3, appendix, models)!")
