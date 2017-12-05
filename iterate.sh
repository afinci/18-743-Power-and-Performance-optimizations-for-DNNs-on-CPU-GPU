for net in ResNet-152 googlenet alexnet
do
    for cpu in consumer automotive office
    do
        python eval.py logs/pwr_tmp_${net}-deploy_${cpu}_$1_$2.log
    done
done
