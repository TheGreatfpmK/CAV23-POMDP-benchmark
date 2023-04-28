# Search and Explore: Symbiotic Policy Synthesis in POMDPs 

This artifact supplements CAV'23 paper *Search and Explore: Symbiotic Policy Synthesis in POMDPs*.

Contents of the artifact:
- paynt.tar: the Docker image containing the tools and benchmarks discussed in the paper, as well as scripts for their automatized evaluation
- paper-submission.pdf: the initial version of the paper submitted to CAV'23
- paper-final.pdf: the revised version of the paper
- LICENSE: the license file
- README.md: this readme

This artifact is hosted on Zenodo: https://doi.org/10.5281/zenodo.7874514.

The first part of this readme describes how to use the artifact to reproduce results presented in the paper. The latter part presents the tools, their installation and their usage outside the scope of this artifact.

---

## Reproducing the experiments

### Using the Docker and quick start

Load the image `paynt.tar` into your Docker environment using:
```
docker load -i paynt.tar
```

If you get a permission error, make sure to precede docker commands with `sudo` to acquire root privileges. Upon loading the image, you can run the container with:
```
docker run -v `pwd`/output:/synthesis/paynt/experiments/output --rm -it randriu/paynt
```

`--rm` creates a disposable container that will be deleted upon exit. `-v` will mount the folder `output` in your current directory to the corresponding folder within the container where the experiment results will be stored. This will allow you to view the generated pdfs and inspect logs even after the container is not running. Executing the command above will place you in `/synthesis/paynt` folder, from which exeriments can be run using
```
./experiments/benchmarks.sh 
```

The evaluating script has additional options (described below) that allow you to reproduce subsets of results presented in the paper. As a quick start, try option `-1` to reproduce Table 2, it should take about 5 minutes:
```
./experiments/benchmarks.sh -1
```
The output is created in `/synthesis/paynt/experiments/output`, which is mounted to `$PWD/output` on the host device. In particular, file `results/table2/table2-models-info.pdf` will contain the reproduced Table 2.

You can exit the container via `exit` or `^D`. Upon finishing your review, you can remove the image from the Docker environment using:
```
docker rmi randriu/paynt
```

The Dockerfile used to create the image can be found in /synthesis/paynt/Dockerfile or at [PAYNT GitHub](https://github.com/randriu/synthesis).


### Evaluating script options

Running the benchmark script `./experiments/benchmark.sh` without additional flags will evaluate experiments from the main part of the paper (without appendix), which will take 10-12 hours. The following options allow you to reproduce subsets of experiments. In the parentheses, we provide the name of the sub-experiment as well as its time estimate.
- `-1` to reproduce Table 2 (models-info, 5 minutes)
- `-2` to reproduce Table 3(a) (q1, 30-40 minutes)
- `-3` to reproduce Table 3(b) (q2, 70-90 minutes)
- `-4` to reproduce Figure 4 (without memory usage subplot) and Table 4 (q3, 8-10 hours)
- `-x` to reproduce Table 5 from the appendix (appendix, 12-16 hours)
- `-a` to reproduce ALL the tables and figures (22-28 hours)

The script creates log files in `experiments/results/output` in sub-folders corresponding to the name of the experiment. Upon finishing the evaluation, the script automatically produces in `experiments/results/output/results` the pdf files containing tables and figures. When executing the script repeatedly, it detects whether the log files already exist, so you can run the experiments in any order and *can abort long ones without loss of progress*. To re-run the experiments, simply delete the corresponding log files or use option `-o` to force the overwrite.

The log files for PAYNT contain description of the produced (compact) FSCs. Since FSCs for Storm and SAYNT are significantly larger, we export them alongside log files only if option `-e` is specified. *NOTE: this option requires multiple GB of disk space and may significantly slow down the evaluation!*

In case the script encounters an error, it generates an error message and proceeds with the evaluation. As a result, the generated tables might be missing rows. You can check the log files to see which experiments failed, remove the corresponding log files and re-run the script if you wish so.

Given the nature of the experiments, their outcome heavily depends on the timing, so the produced tables and figures will be different, although the underlying qualitative comparison of the approaches should be preserved. The original results were obtained on a PC equipped with i5-12600k @4.9GHz and 64GB of RAM. The experiments can be run on a much more modestly equiped PCs/laptops, although it might happen that some experiments will timeout or run out of memory: you will see TO/MO in the corresponding table cell. If you feel like your PC needs more computation time to achieve comparable results to what we present in our paper, you can increase the `timeout_multiplier` variable at the top of the `experiments/experiments.py` file.

The original log files that were used when preparing the submission can be found in `experiments/original-results`.


---


## Using the tools outisde the scope of the artifact

In the paper we consider tools Storm and PAYNT, both are open source tools:

- Storm
    - source: https://github.com/moves-rwth/storm
    - documentation: https://www.stormchecker.org/
    - used version: *make realese on github*
    - StormPy (Storm Python API): https://moves-rwth.github.io/stormpy/
- PAYNT
    - source: https://github.com/randriu/synthesis
    - used version: *make realese on github*

The links contain installation process for both of the tools, if you want to run them outside of this artifact. PAYNT requires correct version of Storm and StormPy to work and provides installation guide for all of them. The used version of PAYNT is able to run Storm and contains the proposed SAYNT algorithm as well.

We provide a small overview of how to use the tools outside of the benchmark script. For full information please visit the linked documentation.

### PAYNT

PAYNT is a tool written Python3. To run PAYNT for the FSC synthesis for POMDPs use:

```
python3 paynt.py --project path/to/model/folder --fsc-synthesis
```

This assumes the model folder contains both the model description and a specification. Each time an improving FSC is found, we output it's value, size and the time it took to find it. You can use `--export-fsc-paynt "filepath"` to store the best found FSC to specified file. For more information about the settings of PAYNT visit https://github.com/randriu/synthesis.

### Storm

With the integration we propose in this paper we allow to run Storm from PAYNT. This usage doesn't provide all the possible Storm settings, but it is enough for the purposes of synthetising good FSCs for POMDPs. To use Storm through PAYNT use:

```
python3 paynt.py --project path/to/model/folder --fsc-synthesis --storm-pomdp --get-storm-result 0
```

You can adjust the main setting of Storm with `--storm-options` (for example `--storm-options 2mil` to explore 2 million states and apply cut-offs, `--storm-options 10mil` to explore 10 million states and apply cut-offs, `--storm-options clip4` to allow clipping with grid resolution 4).

#### Storm as a standalone tool

If you want to run Storm as a standalone tool visit: https://www.stormchecker.org/getting-started.html. To use Storm for POMDP analysis you need to build the `storm-pomdp` executable.

### SAYNT

SAYNT algorithm we propose in this work uses the implementation of PAYNT and Storm. It can be run from PAYNT using:

```
python3 paynt.py --project path/to/model/folder --fsc-synthesis --storm-pomdp --iterative-storm 'timeout' 'paynt_timeout' 'storm_timeout'
```

The default setting, we used for the majority of the experiments (see the paper for more details), is `--iterative-storm 900 60 10`. This means that the overall timeout is 15 minutes (900s) and in each iteration of SAYNT, we will run the inductive search for 60 seconds and belief exploration for 10 seconds. You can change these timeouts to observe the impact of the particular parts of the synthesis process. SAYNT also introduces some additional settings we do not consider in this paper. For more information visit https://github.com/randriu/synthesis.


## Models

The POMDPs considered in our experiments are located in `PAYNT_ROOT/models/pomdp/storm-integration`. We consider models from various sources:

- POMDPs from Tony Cassandra's webpage https://pomdp.org/ we converted to explicit .drn format
- POMDPs from the paper "Gethin Norman, David Parker and Xueyi Zou. Verification and Control of Partially Observable Probabilistic Systems" available at http://www.prismmodelchecker.org/files/rts-poptas/ in PRISM format
- our problem examples explained in the paper and the Lanes+ model explained in the appendix, also in the PRISM format

To learn more about the PRISM format for creating stochastic models and their specifications visit: https://www.prismmodelchecker.org/manual/ThePRISMLanguage/Introduction


### The evaluation scripts

The evaluation scripts are available at https://github.com/TheGreatfpmK/CAV23-POMDP-benchmark.

Requirements:
- Python3.8 or higher
- pdflatex (`sudo apt-get install texlive-pictures`) - we use this to generate the PDFs for convenience, if you want to use different way we also provide the .tex source files so you can convert the tables/graphs yourself

Place all of the files of the repository to folder called `experiments` in the root folder of PAYNT, i.e.,
```
cp -r DIR_POMDP_BENCHMARKS/* PAYNT_ROOT/experiments/
```

Run the experiments using
```
./experiments/benchmarks.sh 
```

See above for more options.

