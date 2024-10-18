#!/bin/bash

gcc -O2 -o  matrixmult matrixmult.c


matrix_sizes=(10 100 300 500 1000)
rounds=1 
iterations=5 


output_file="C_perf_results.csv"


echo "Matrix Size;Round;Iteration; TimeElapsed(sec); Maximum RSS (kbytes)" > $output_file


for size in "${matrix_sizes[@]}"; do
    echo "Running for matrix size: $size"
    
    
    for round in $(seq 1 $rounds); do
        echo "  Round $round"
        
       
        for iter in $(seq 1 $iterations); do
            echo "Iteration $iter"
            
            perf_result=$(perf stat -e task-clock ./matrixmult $size 2>&1)
  
            execution_time_sec=$(echo "$perf_result" | grep "seconds time elapsed" | awk '{print $1}')
            echo "Execution time: $execution_time_sec"
            time_result=$(/usr/bin/time -v ./matriz $size 2>&1)
            
          
            max_rss=$(echo "$time_result" | grep "Maximum resident set size" | awk '{print $6}')
            
            echo "MAX RSS (Memory): $max_rss kbytes"
            
            if [ -n "$execution_time_sec" ] && [ -n "$max_rss" ]; then
               
                echo "$size;$round;$iter;$execution_time_sec;$max_rss" >> $output_file
            else
                echo "Error: Could not capture memory usage or execution time for $size, round $round, iteration $iter"
            fi
        done
    done
done

echo "Results saved in $output_file"




