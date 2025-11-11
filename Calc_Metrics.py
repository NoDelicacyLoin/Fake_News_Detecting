import time
from sklearn.metrics import f1_score, accuracy_score

def metric_MacroF1_calc(true_labels_list, predicted_labels_list):
    """
    calc Macro-F1, main metric：
    """
    return f1_score(true_labels_list, predicted_labels_list, average="macro")

def metric_Accuracy_calc(true_labels_list, predicted_labels_list):
    """
    calc Accuracy, secondary metrics
    """
    return accuracy_score(true_labels_list, predicted_labels_list)

def metric_latency_calc(text2text_generator_pipeline, input_texts, n_samples_for_timing=300, max_new_tokens=4):
    """
    return mean each_sample_time(ms), float
    """
    total_to_measure = min(n_samples_for_timing, len(input_texts))

    # 热身：第一次生成常常包含编译/缓存，慢且不稳定，不计入统计
    warmup_output = text2text_generator_pipeline(input_texts[0], max_new_tokens=max_new_tokens)

    start_time = time.time()
    for i in range(total_to_measure):
        generated_output = text2text_generator_pipeline(input_texts[i], max_new_tokens=max_new_tokens)
        # 这里只是计时，不需要用 generated_output 的内容
    avg_ms_per_sample = (time.time() - start_time) / total_to_measure * 1000.0
    return avg_ms_per_sample

'''！！！！！！！！！！！！！！！！！'''
'''要注意万一生成式ai生成模型可能偶尔吐出别的词（比如 “barely-true”，怎么办？？
暂且来看，只会是true/false对吧？到时候真生成了乱七八糟的我再想办法,再加限制就行。
Limit max_new_token, enhance paraphrase ability'''

def map_generated_label_text_to_binary_label(generated_label):
    text_lower = str(generated_label).strip().lower()
    return 1 if ("true" in text_lower) else 0
