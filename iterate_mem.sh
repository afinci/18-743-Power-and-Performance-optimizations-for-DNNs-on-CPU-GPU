for gpu_freq in 998 537 76
do
    for cpu_freq in 1734 921 102
    do
        for net in ResNet-152 googlenet alexnet
        do
            for cpu in consumer automotive office
            do
                python eval_mem.py logs/util_${net}-deploy_${cpu}_${gpu_freq}_${cpu_freq}.log
            done
        done
    done
done