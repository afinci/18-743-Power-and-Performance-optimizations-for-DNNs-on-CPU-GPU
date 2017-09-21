# Goal
To profile the relationship between performance and power of embedded platform under the scenario of inferencing deep neural network with CPU running on SPEC.

## GPU - Inferencing Scenarios
- Different architecture of neural network
- (Different frequency for GPU)

## CPU - Running other tasks
- Run SPEC CPU2006 (Understand the relationship between CPU utilization and how it affects the GPU speed)

- Different frequency
    - Understand how it affects utilization
    - How it affects power consumption of CPU
    - How it affects power consumption of the overall system
    - How it affects the GPU speed

# Action Item
1. Come up with 3 image classification DNN that runs on TX1
    - Change the algorithms and frequency (low-mid-high) and measure power consumption and runtime to build up Figure 1. (3x3 points scatter plot)

2. Compile SPEC CPU2006 and pick 3 benchmark to run on CPU (Branch, Memory, Compute)
    - Come up with a bi-axes plot that plots utilization and power consumption of CPU for different frequency. (3 curves)

5. For each GPU setting (3x3), plot bi-axes plot that plots speed of GPU and overall power consumption of CPU tasks in different frequency (3x3)