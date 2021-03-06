for gpu_freq in 998 537 76
do
    for cpu_freq in 1734 921 102
    do
        for net in ResNet-152 googlenet alexnet
        do
            for cpu in consumer automotive office
            do
                python eval.py logs_maxmin/pwr_tmp_${net}-deploy_${cpu}_${gpu_freq}_${cpu_freq}.log
            done
        done
    done
done
