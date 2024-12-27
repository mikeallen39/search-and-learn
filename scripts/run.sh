#!/bin/bash




# 定义任务参数
STEP=50
TOTAL_TASKS=20  # 总任务数
INPUT_FILES=()  # 如果有输入文件，可以在这里定义

# 循环运行任务
for TASK_ID in $(seq 1 $TOTAL_TASKS); do
    # 计算数据集的范围
    DATASET_START=$(( (TASK_ID - 1) * STEP ))
    DATASET_END=$(( DATASET_START + STEP ))

    # 运行 Python 脚本
    python test_time_compute.py \
        ../recipes/Llama-3.2-1B-Instruct/best_of_n.yaml \
        --model_path=Qwen/Qwen2.5-1.5B-Instruct \
        --cache_dir=../cache \
        --dataset_start=$DATASET_START \
        --dataset_end=$DATASET_END &
done

# 等待所有任务完成
wait
echo "All tasks completed!"