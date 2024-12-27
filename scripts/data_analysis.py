import json

# 读取 JSON Lines 文件
with open('data/Qwen/Qwen2.5-1.5B-Instruct/bon_completions.jsonl', 'r') as file:
    completions = [json.loads(line) for line in file]  # 逐行解析

# 列出所有字段
fields = set()  # 使用集合去重

for problem in completions:
    fields.update(problem.keys())

# 输出所有字段
print("all fields:")
for field in fields:
    print(field)
    
    
    

# 初始化统计变量
total_questions = 0
correct_answers = 0

# 遍历每个问题
for problem in completions:
    total_questions += 1
    answer = problem.get("answer")  # 标准答案
    pred = problem.get("pred")  # 模型预测结果

    # 比较预测结果与标准答案
    if pred == answer:
        correct_answers += 1
        print(f"问题 {problem.get('unique_id')}: 正确")
    else:
        print(f"问题 {problem.get('unique_id')}: 错误 (预测: {pred}, 答案: {answer})")

# 计算准确率
accuracy = correct_answers / total_questions
print(f"\n总问题数量: {total_questions}")
print(f"正确回答数量: {correct_answers}")
print(f"准确率: {accuracy * 100:.2f}%")