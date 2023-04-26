#!/bin/bash

appendix=false
overwrite=false
export=false

models=true
q1=true
q2=true
q3=true

while getopts amxoe1234 flag
do
    case "${flag}" in
        x) 
            models=false
            q1=false
            q2=false
            q3=false
            appendix=true
            ;;
        m) 
            models=true
            q1=true
            q2=true
            q3=true
            appendix=false
            ;;
        a) 
            models=true
            q1=true
            q2=true
            q3=true
            appendix=true
            ;;
        o)
            overwrite=true
            ;;
        e)
            export=true
            ;;
        1)
            appendix=false
            models=true
            q1=false
            q2=false
            q3=false
            ;;
        2)
            appendix=false
            models=false
            q1=true
            q2=false
            q3=false
            ;;
        3)
            appendix=false
            models=false
            q1=false
            q2=true
            q3=false
            ;;
        4)
            appendix=false
            models=false
            q1=false
            q2=false
            q3=true
            ;;
    esac
done

if [ "$overwrite" = true ]
then
    if [ "$export" = true ]
    then
        if [ "$models" = true ]
        then
            python3 experiments/experiments.py models True export
            python3 experiments/get-tables.py models
            python3 experiments/generate-pdf.py models
        fi
        if [ "$q1" = true ]
        then
            python3 experiments/experiments.py q1 True export
            python3 experiments/get-tables.py q1
            python3 experiments/generate-pdf.py q1
        fi
        if [ "$q2" = true ]
        then
            python3 experiments/experiments.py q2 True export
            python3 experiments/get-tables.py q2
            python3 experiments/generate-pdf.py q2
        fi
        if [ "$q3" = true ]
        then
            python3 experiments/experiments.py q3 True export
            python3 experiments/get-tables.py memory
            python3 experiments/get-graphs.py
            python3 experiments/generate-pdf.py memory
            python3 experiments/generate-pdf.py q3-figure
        fi
        if [ "$appendix" = true ]
        then
            python3 experiments/experiments.py appendix True export
            python3 experiments/get-tables.py appendix
            python3 experiments/generate-pdf.py appendix
        fi
    else
        if [ "$models" = true ]
        then
            python3 experiments/experiments.py models True
            python3 experiments/get-tables.py models
            python3 experiments/generate-pdf.py models
        fi
        if [ "$q1" = true ]
        then
            python3 experiments/experiments.py q1 True
            python3 experiments/get-tables.py q1
            python3 experiments/generate-pdf.py q1
        fi
        if [ "$q2" = true ]
        then
            python3 experiments/experiments.py q2 True
            python3 experiments/get-tables.py q2
            python3 experiments/generate-pdf.py q2
        fi
        if [ "$q3" = true ]
        then
            python3 experiments/experiments.py q3 True
            python3 experiments/get-tables.py memory
            python3 experiments/get-graphs.py
            python3 experiments/generate-pdf.py memory
            python3 experiments/generate-pdf.py q3-figure
        fi
        if [ "$appendix" = true ]
        then
            python3 experiments/experiments.py appendix True
            python3 experiments/get-tables.py appendix
            python3 experiments/generate-pdf.py appendix
        fi
    fi
else
    if [ "$export" = true ]
    then
        if [ "$models" = true ]
        then
            python3 experiments/experiments.py models False export
            python3 experiments/get-tables.py models
            python3 experiments/generate-pdf.py models
        fi
        if [ "$q1" = true ]
        then
            python3 experiments/experiments.py q1 False export
            python3 experiments/get-tables.py q1
            python3 experiments/generate-pdf.py q1
        fi
        if [ "$q2" = true ]
        then
            python3 experiments/experiments.py q2 False export
            python3 experiments/get-tables.py q2
            python3 experiments/generate-pdf.py q2
        fi
        if [ "$q3" = true ]
        then
            python3 experiments/experiments.py q3 False export
            python3 experiments/get-tables.py memory
            python3 experiments/get-graphs.py
            python3 experiments/generate-pdf.py memory
            python3 experiments/generate-pdf.py q3-figure
        fi
        if [ "$appendix" = true ]
        then
            python3 experiments/experiments.py appendix False export
            python3 experiments/get-tables.py appendix
            python3 experiments/generate-pdf.py appendix
        fi
    else
        if [ "$models" = true ]
        then
            python3 experiments/experiments.py models False
            python3 experiments/get-tables.py models
            python3 experiments/generate-pdf.py models
        fi
        if [ "$q1" = true ]
        then
            python3 experiments/experiments.py q1 False
            python3 experiments/get-tables.py q1
            python3 experiments/generate-pdf.py q1
        fi
        if [ "$q2" = true ]
        then
            python3 experiments/experiments.py q2 False
            python3 experiments/get-tables.py q2
            python3 experiments/generate-pdf.py q2
        fi
        if [ "$q3" = true ]
        then
            python3 experiments/experiments.py q3 False
            python3 experiments/get-tables.py memory
            python3 experiments/get-graphs.py
            python3 experiments/generate-pdf.py memory
            python3 experiments/generate-pdf.py q3-figure
        fi
        if [ "$appendix" = true ]
        then
            python3 experiments/experiments.py appendix False
            python3 experiments/get-tables.py appendix
            python3 experiments/generate-pdf.py appendix
        fi
    fi
fi