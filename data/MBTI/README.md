---
unknown: null
license: apache-2.0
---
Here are the ***behavior datasets*** used for supervised fine-tuning (SFT). And they can also be used for direct preference optimization (DPO).

The exact copy can also be found in [Github](https://github.com/PKU-YuanGroup/Machine-Mindset/edit/main/datasets/behaviour).

Prefix ***'en'*** denotes the datasets of the English version.

Prefix ***'zh'*** denotes the datasets of the Chinese version.

## Dataset introduction

There are four dimension in MBTI. And there are two opposite attributes within each dimension.

To be specific:

+ Energe: Extraversion (E) - Introversion (I)

+ Information: Sensing (S) - Intuition (N)

+ Decision: Thinking (T) - Feeling (F)

+ Execution: Judging (J) - Perceiving (P)

Based on the above, you can infer the content of the json file from its name.

The datasets follow the Alpaca format, consisting of instruction, input and output.

## How to use these datasets for behavior supervised fine-tuning (SFT)

For example, if you want to make an LLM behave like an ***ISFJ***, you need to select ***the four corresponding files*** (en_energe_introversion.json, en_information_sensing.json, en_decision_feeling.json, en_execution_judging.json). 

And use the four for SFT.

## How to use these datasets for direct preference optimization (DPO)

For example, if you want to make an LLM be ***more feeling (F) than thinking (T)*** by DPO, you need to select ***the two corresponding files*** (en_decision_feeling.json, en_decision_thinking.json). 

And then compile the two into the correct format for DPO. For the correct format, please refer to [this](https://github.com/PKU-YuanGroup/Machine-Mindset/blob/main/datasets/dpo/README.md).
