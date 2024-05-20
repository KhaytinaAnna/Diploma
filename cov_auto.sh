#!/bin/bash

# python3 some.py;
# echo "Done generating chatgpt responses, type any symbol to continue (next step: generate codes for cov)"
# read qw
# python3 check.py;
# echo "Done generating .py files, type any symbol to continue (next step: performing cov)"

START_TEST=${START_TEST}
END_TEST=${END_TEST} # включительно

for ((i=START_TEST; i<=END_TEST; i++)); do
    for ((j=0; j<100; j++)); do
        if [ -f "res_dataset/${i}/${i}_${j}_code.py" ]; then
            coverage run res_dataset/${i}/${i}_${j}_code.py;
            coverage html -d res_dataset/${i}/${i}_${j}_code_coverage/;
        else
            break;
        fi
    done
done

