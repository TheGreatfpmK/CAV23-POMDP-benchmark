#!/bin/bash

main=true
appendix=false
overwrite=false
export=false

while getopts amxoe flag
do
    case "${flag}" in
        x) 
            main=false
            appendix=true
            ;;
        m) 
            main=true
            appendix=false
            ;;
        a) 
            main=true
            appendix=true
            ;;
        o)
            overwrite=true
            ;;
        e)
            export=true
            ;;
    esac
done

if [ "$main" = true ]
then
    if [ "$overwrite" = true ]
    then
        if [ "$export" = true ]
        then
            python3 experiments/experiments.py models True export
        else
            python3 experiments/experiments.py models True
        fi
        python3 experiments/get-tables.py models
        python3 experiments/generate-pdf.py models

        if [ "$export" = true ]
        then
            python3 experiments/experiments.py q1 True export
        else
            python3 experiments/experiments.py q1 True
        fi
        python3 experiments/get-tables.py q1
        python3 experiments/generate-pdf.py q1

        if [ "$export" = true ]
        then
            python3 experiments/experiments.py q2 True export
        else
            python3 experiments/experiments.py q2 True
        fi
        python3 experiments/get-tables.py q2
        python3 experiments/generate-pdf.py q2

        if [ "$export" = true ]
        then
            python3 experiments/experiments.py q3 True export
        else
            python3 experiments/experiments.py q3 True
        fi
        python3 experiments/get-tables.py memory
        python3 experiments/get-graphs.py
        python3 experiments/generate-pdf.py memory
        python3 experiments/generate-pdf.py q3-figure
    else
        if [ "$export" = true ]
        then
            python3 experiments/experiments.py models False export
        else
            python3 experiments/experiments.py models False
        fi
        python3 experiments/get-tables.py models
        python3 experiments/generate-pdf.py models

        if [ "$export" = true ]
        then
            python3 experiments/experiments.py q1 False export
        else
            python3 experiments/experiments.py q1 False
        fi
        python3 experiments/get-tables.py q1
        python3 experiments/generate-pdf.py q1

        if [ "$export" = true ]
        then
            python3 experiments/experiments.py q2 False export
        else
            python3 experiments/experiments.py q2 False
        fi
        python3 experiments/get-tables.py q2
        python3 experiments/generate-pdf.py q2

        if [ "$export" = true ]
        then
            python3 experiments/experiments.py q3 False export
        else
            python3 experiments/experiments.py q3 False
        fi
        python3 experiments/get-tables.py memory
        python3 experiments/get-graphs.py
        python3 experiments/generate-pdf.py memory
        python3 experiments/generate-pdf.py q3-figure
    fi
fi

if [ "$appendix" = true ]
then
    if [ "$overwrite" = true ]
    then
        if [ "$export" = true ]
        then
            python3 experiments/experiments.py appendix True export
        else
            python3 experiments/experiments.py appendix True
        fi
        python3 experiments/get-tables.py appendix
        python3 experiments/generate-pdf.py appendix
    else
        if [ "$export" = true ]
        then
            python3 experiments/experiments.py appendix False export
        else
            python3 experiments/experiments.py appendix False
        fi
        python3 experiments/get-tables.py appendix
        python3 experiments/generate-pdf.py appendix
    fi
fi
