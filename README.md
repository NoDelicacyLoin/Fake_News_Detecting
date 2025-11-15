# Fake_News_Detecting

**Research Subject 1:**On FLAN-T5-small (≈80M) and BART-base (≈139M), compare finetuning techniques under a completely unified training and inference decoding configuration:

Instruction + CoT SFT (Training objective: brief reason + final label)

Instruction SFT + Soft Prompt-Tuning (Training objective: label only; freeze the model, train only m soft cue vectors)
Question: Which offers greater Macro-F1 improvement while being more cost-effective in terms of inference latency/training and storage costs (best performance-to-price ratio)?

**Research Subject 2:**Cost Assessment under Performance Alignment

Comparing costs when achieving the same Macro-F1:

FLAN-T5-small + (fine-tuning options) vs FLAN-T5-base (≈250M) Instructional zero/few-shot baseline

BART-base + (fine-tuning options) vs BART-large (≈406M) Instructional zero/few-shot baseline

Idea: Evaluating the costs and benefits of "small model + fine-tuning" compared to "large model without fine-tuning" from dimensions such as inference latency, model size, memory usage, etc.


# Research Content and Experimental Design (Summary)
Classify fake/true news with only statement text as the main component,  using the LIAR fake news dataset. 
The datasets are already labeled with 6 categories. In this research, we simplify 6 categories to T/F binary classification.

Unified Configuration (Key Items): max_input_length, max_new_tokens (uniformly set large enough to be compatible with CoT output), epochs, effective batch, random seed.

Input Template: Both groups use the same instruction template; the training objective for the CoT group is "reason + label". The Soft Prompt group is "label only".

**Comparison Matrix**:
1. T5-small: Instruction only vs Instruction + CoT vs Instruction + Soft Prompt-Tuning (m=20~50).
2. BART-base: Instruction only vs Instruction + CoT vs Instruction + Soft Prompt-Tuning (m=20~50).
3. Scale Baseline: Instruction prompting for T5-base and BART-large (zero/few samples)

# Key Evaluation Metrics

Main Metric: Macro-F1.
Secondary Metric: Accuracy.

# Expected Conclusions (Revised Version)

Under a fixed computational budget and unified decoding, evaluate the accuracy-latency tradeoff between Instruction SFT, Instruction+CoT SFT, and Instruction SFT + Soft Prompt-Tuning, providing the following:

1. When pursuing higher Macro-F1, the gains of CoT and the cost of its latency/training token increment;

2. When prioritizing engineering cost-effectiveness (small parameters, lightweight deployment, low latency), the performance of Soft Prompt-Tuning and the recommended range of m values;

3. Small model + fine-tuning vs. large model without fine-tuning: A comparison of equivalent costs under the same Macro-F1, forming engineering-ready selection recommendations (when to prioritize "efficient parameter fine-tuning" and when to consider "switching to a larger model").

