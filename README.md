# Search and Explore: Symbiotic Policy Synthesis in POMDPs 

This repository contains the benchmarks for the CAV'23 paper *Search and Explore: Symbiotic Policy Synthesis in POMDPs.*
This readme contains a description how to run these benchmarks to recreate the results from the paper. 
As a reference, we provide our logs in the `original-results`, in case something goes wrong.

---

## Running the benchmarks

### Requirements
- Python3.8 or higher
- pdflatex (`sudo apt-get install texlive`) - we use this to generate the PDFs for the convinience, if you want to use different way we also provide the .tex source files so you can convert the tables/graphs yourself

### Setup
Place all of the files of this repository to folder called `experiments` in the root folder of PAYNT, i.e.,
```
cp -r DIR_POMDP_BENCHMARKS/* PAYNT_ROOT/experiments/
```

### The benchmark script
Then run the benchmarks using:

```
./PAYNT_ROOT/experiments/benchmark.sh
```

The benchmark script comes with a variety of options, details for the individual experiments is given below. 
- `-a` use this flag to run experiments both from the paper and the appendix (without this flag only the main experiments run)
- `-x` use this flag to only run experiments from the appendix
- `-1` run only model information experiment (table2)
- `-2` run only Q1 experiments (table3(a))
- `-3` run only Q2 experiments (table3(b))
- `-4` run only Q3 experiments (figure4 + table4)
- `-o` with this flag overwriting of already existing logs is allowed (good if you want to rerun all the experiments), overwriting is turned off by default so if you only want to run experiments for certain values remove the logs associated with the values and rerun this script without -o flag
- `-e` allows export of the FSCs found by SAYNT to disk, *This option requires multiple GB of disk space and may significantly slow down the benchmarks!*

The script automatically runs all the experiments and creates PDFs containing tables/graphs. 
All the PDFs (and the source .tex files) will be located in `experiments/results/output` folder. 
If you used the `-e` flag you can find the exported FSCs alongside the log files.

The logs, from which the tables are created, are saved into corresponding folders. E.g., experiments to obtain information about models (table 2 of our paper) will store the logs to the folder `models-info`.

The script is pretty fail-safe meaning that it will finish and generate all the output even if some experiment fails (it will notify you with ERROR message on stdout). So if some of the generated tables are missing rows, check the output of the benchmark script to see what experiments failed, remove their log files and rerun the script if you want to.

If you feel like your PC needs more computation time to achieve comparable results to what we present in our paper you can adjust the `timeout_multiplier` variable on top of the `experiments/experiments.py` file.

### Expected runtime
- the main experiments take 9-12 hours to run
    - model information experiment (flag `-1`) takes 5 minutes
    - Q1 experiment (flag `-2`) takes 30-40 minutes
    - Q2 experiment (flag `-3`) takes 70-90 minutes
    - Q3 experiment (flag `-4`) takes 8-10 hours
- the appendix experiments on their own take 12-16 hours to run

The folder `experiments/original-results` contains our log files. The subfolders `models-info`, `q1`, `q2`, `q3`, `appendix` contain the log files generated from the tools. The subfolder `results` contains the PDFs generated from these logs.

## Tools

In the artifact we consider tools Storm and PAYNT, both are open source tools:

- Storm
    - source: https://github.com/moves-rwth/storm
    - documentation: https://www.stormchecker.org/
    - Used version: *make realese on github*
    - StormPy (Storm Python API): https://moves-rwth.github.io/stormpy/
- PAYNT
    - source: https://github.com/randriu/synthesis
    - Used version: *make realese on github*

The links contain installation process for both of the tools, if you want to run them outside of this artifact. PAYNT requires correct version of Storm and StormPy to work and provides installation guide for all of them. The used version of PAYNT is able to run Storm and contains the proposed SAYNT algorithm as well.

## Models

The POMDPs considered in our experiments are located in `PAYNT_ROOT/models/pomdp/storm-integration`. We consider models from various sources:

- POMDPs from Tony Cassandra's webpage https://pomdp.org/ we converted to explicit .drn format
- POMDPs from the paper "Gethin Norman, David Parker and Xueyi Zou. Verification and Control of Partially Observable Probabilistic Systems" available at http://www.prismmodelchecker.org/files/rts-poptas/ in PRISM format
- our problem examples explained in the paper and the Lanes+ model explained in the appendix, also in the PRISM format

To learn more about the PRISM format for creating stochastic models and their specifications visit: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction


## Details on the experiments
We provide a quick overview of the experiments here:

#### Table 2 - models-info
This experiment provides the information about all of the considered models like their number of states/actions/observation and computed over-approximation using Storm

#### Table 3 - Q1
Experiment showing the potential improvements we can achieve by using FSCs generated by inductive synthesis in Storm

#### Table 3 - Q2
Experiment showing the improvements of PAYNT when we use policies computed by Storm to steer the inductive synthesis

#### Table 4 - size of FSCs (part of Q3 experiments)
We show the difference in value/size of the FSCs produced by SAYNT

#### Figure 4 - Q3
In this experiment we compare SAYNT/PAYNT/Storm on how they find FSCs over time. The results of this experiment are presented as a series of graphs each one for each model.

#### Appendix
In the appendix we provide more values we achieved when comparing SAYNT/PAYNT/Storm. The table in appendix provides information about the best quality FSC, when it was found and it's size within a 15 minute time limit.
