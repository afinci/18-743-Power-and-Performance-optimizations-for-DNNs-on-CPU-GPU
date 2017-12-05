for net in ResNet-152 googlenet alexnet
do
    for cpu in consumer automotive office
    do
        python eval_latency.py logs/latency_${net}-deploy_${cpu}_$1_$2.log
    done
done
