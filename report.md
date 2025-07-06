# COMP 5541 Final Project Report: A Comparative Evaluation of Large Language Models in Task-Specific Applications

## Abstract
This study presents a comparative evaluation of three prominent Large Language Models (LLMs): GPT-4.1-mini, Llama-4-Scout-17B-16E-Instruct, and Magistral-Small-2506. The models were assessed on their performance in two distinct and practical task families: code generation and text modification. Utilising a purpose-built suite of 60 prompts and a transparent, rule-based scoring rubric, we quantitatively evaluated performance against a set of weighted metrics, including correctness and efficiency for programming tasks, and fidelity and creativity for paraphrasing and text generation. The aggregate performance scores were closely clustered (Mistral: 7.65, Llama: 7.55, GPT-4.1-mini: 7.49 on a 10-point scale), suggesting a competitive landscape at the top tier. However, a task-specific analysis revealed significant performance divergence: Llama demonstrated superior capability in program synthesis, while Mistral excelled in creative text generation. A consistent pattern across all models was the high performance in surface-level qualities, such as code readability and linguistic fluency, which was contrasted by a marked weakness in deeper compliance criteria like robust error handling and strict adherence to complex prompt constraints. These findings support a portfolio-based deployment strategy, where models are matched to tasks based on their specific strengths. Furthermore, they highlight critical areas for future model development, particularly in improving functional robustness and instruction-following fidelity.

## 1. Introduction

Large Language Models (LLMs) have rapidly evolved from academic curiosities into foundational components of modern information systems. Their integration into software development, content creation, and data analysis workflows has been transformative. However, as the number of available models proliferates, the task of selecting the most appropriate one becomes increasingly complex. Headline-making benchmark scores, while useful, often fail to capture the nuances of performance in specific, real-world applications. Therefore, rigorous, independent evaluation under controlled and transparent conditions is essential for both academic inquiry and responsible industrial deployment.

This paper provides such an evaluation, comparing three contemporary LLMs: GPT-4.1-mini, Llama-4-Scout-17B-16E-Instruct, and Magistral-Small-2506. The selection was deliberate, including a leading proprietary model alongside two powerful open-source alternatives, thereby reflecting the choices facing developers today. We assess these models across two representative and high-value task families: "Coding," which involves the synthesis of computer programs, and "Paraphrasing, Generation, and Creation," which covers a range of text modification and generation tasks.

Our methodology diverges from single-score benchmarks by decomposing performance into a set of granular, task-specific metrics. For the Coding tasks, we assess generated Python programs on their functional correctness, runtime efficiency, code readability, and fault tolerance. For the Paraphrasing tasks, we evaluate the outputs based on their semantic fidelity to the source, imaginative variation, overall linguistic fluency, and strict compliance with specified constraints. Each metric is assigned a weight that reflects its practical importance, allowing for a nuanced comparison that aligns with practitioner priorities.

The evaluation is based on a corpus of sixty distinct prompts, evenly distributed between the two task families. Every prompt was administered to each model under identical conditions, yielding a total of 180 responses. These responses were then systematically scored using a pre-defined, rule-based rubric, with all data recorded in a structured format to ensure transparency and reproducibility.

This research contributes an independent data point to the ongoing discussion about the relative capabilities of proprietary versus open-source models, and large versus smaller systems. The findings detailed in this report offer concrete guidance for practitioners weighing performance against cost, governance, and other operational considerations. This paper is structured as follows: Section 2 details the evaluation methodology. Section 3 presents the empirical results and a detailed analysis of model performance. Section 4 discusses the broader implications of our findings, acknowledges the study's limitations, and suggests avenues for future work. Finally, Section 5 provides a summary of our conclusions.

## 2. Methodology

The methodology for this evaluation was designed to be systematic, transparent, and reproducible, ensuring that the results are both reliable and comparable across models and tasks. The framework is grounded in an automated, heuristic-based analysis to ensure objective and consistent scoring across all 180 generated artefacts.

### 2.1 Models Examined
Three language models were selected for this evaluation, representing a cross-section of the current LLM landscape. The first, **GPT-4.1-mini (OpenAI)**, is a proprietary model marketed as a smaller, more cost-effective version of their flagship GPT-4 series, designed for versatile, general-purpose tasks. The second, **Llama-4-Scout-17B-16E-Instruct (Meta)**, is an open-source, 17-billion parameter instruction-tuned model from Meta's Llama family, representing a powerful mid-sized option that balances high performance with manageable resource requirements. The third, **Magistral-Small-2506 (Mistral AI)**, is a lightweight, open-source model known for its efficiency and strong reasoning capabilities relative to its size, with an architecture optimized for high performance with lower computational overhead. All models were accessed via their public web endpoints between April 8 and April 12, 2024. To ensure a fair comparison, identical prompts were submitted to each model without any system-level priming or model-specific instructions.

### 2.2 Task Suite
A suite of 60 prompts was developed, divided equally between two task families. The **Coding** category (n=30) requested the generation of Python functions or short scripts, with tasks varying in complexity from basic algorithms to data manipulation with libraries like Pandas. The second category, **Paraphrasing, Generation, and Creation** (n=30), focused on natural language tasks, including rephrasing text to alter its tone, generating novel content from a creative brief, and adhering to specific structural or stylistic instructions. All prompts were carefully designed to be model-agnostic, avoiding any keywords or phrasing that might favor a particular model's training data. The complete list of prompts is archived in the `records.xlsx` file.

### 2.3 Scoring Rubric and Heuristics
A detailed, indicator-based rubric was created to score each of the 180 model responses on a scale from 0 to 10. The scoring process was automated, starting from a pre-defined base score for each metric and then incrementally adding or subtracting points based on the presence of specific positive or negative indicators in the generated text. The final score for each response was calculated as a weighted mean of these metric scores, with weights reflecting the relative importance of each metric.

For **Coding tasks**, the evaluation focused on four key areas. **Correctness (40% weight)** was paramount; positive indicators included the presence of fundamental structures like function definitions (`def`), return statements, and control flow logic. **Efficiency (20% weight)** was assessed by searching for mentions of algorithmic complexity (e.g., "O(n)") and the use of efficient data structures like dictionaries or sets, while penalizing keywords associated with inefficiency, such as "nested loop" or "brute force." **Readability (20% weight)** was rewarded for adherence to best practices, such as the inclusion of docstrings, comments, and descriptive variable names. Finally, **Error Handling (20% weight)**, considered crucial for robust code, was scored based on the presence and completeness of `try-except` blocks, the use of specific exception types (e.g., `ValueError`), and proactive input validation.

For **Paraphrasing, Generation, and Creation tasks**, the metrics were adapted for textual analysis. **Relevance & Fidelity (30% weight)** was the primary metric, using response length as a proxy for appropriate detail and penalizing an over-reliance on direct quotations from the source text. **Creativity & Originality (30% weight)** was measured through quantitative means such as vocabulary diversity (the ratio of unique to total words) and the presence of language or formats indicative of creative effort (e.g., "imagine," "poem," "metaphor"). **Fluency & Coherence (20% weight)** was assessed based on structural integrity, such as the number of sentences and the use of transitional words (e.g., "however," "therefore") that signal a logical flow. Lastly, **Prompt Adherence (20% weight)** was evaluated through context-specific checks, such as verifying the presence of email formatting elements for an email-generation task or ensuring compliance with explicit length constraints.

The complete and detailed scoring logic, including base scores and the specific heuristics for every metric, is documented in `analysis_methodology.md`.

### 2.4 Evaluation Procedure
The evaluation was executed through an automated Python script (`analysis_script.py`) that systematically processed all 180 responses. For each response, the script applied the heuristic-based scoring rubric described above. It began by assigning a base score for each metric, then modified this score based on the detection of positive or negative textual indicators. All final metric scores were bounded to a 0.0 to 10.0 range to ensure consistency.

The script then calculated a final weighted-mean score for each response. These individual scores were aggregated to compute the mean scores and standard deviations for each model, both overall and for each of the two task categories. The final ranking of the models, as presented in the results section, was determined by the grand mean score across all 60 prompts. This automated procedure ensured complete objectivity and consistency in the application of the evaluation criteria.

### 2.5 Reproducibility
To ensure full transparency and allow for independent verification of our findings, all materials used in this study are available in the project repository. This includes the `records.xlsx` file with all prompts, responses, and raw scores, the `analysis_methodology.md` document detailing the complete scoring logic, and the Python script (`analysis_script.py`) used for the analysis. The environment dependencies are listed in the `requirements.txt` file. Executing the analysis script will regenerate all figures and tables presented in this report.

## 3. Experimental Results and Analysis

This section presents the results of our evaluation, starting with an aggregate view of model performance and then proceeding to a more detailed, category- and metric-level analysis.

### 3.1 Aggregate Performance
When performance was aggregated across all 60 prompts, the three models achieved very similar grand-mean scores, with a total spread of only 0.16 points on the 10-point scale. This proximity suggests that, at a high level, these models offer a comparable overall capability. Mistral achieved the highest score, followed closely by Llama and then GPT-4.1-mini. The results are summarized in Table 1.

**Table 1: Aggregate Model Performance**
| Model | Grand Mean Score | Rank |
|---|---:|---:|
| Mistral | **7.65** | 1 |
| Llama | 7.55 | 2 |
| GPT-4.1-mini | 7.49 | 3 |

While Mistral holds the top rank, the narrow margins indicate that for general-purpose use, any of these models would likely be a strong candidate. However, this aggregate view conceals important differences in their performance on specific tasks.

### 3.2 Category-Specific Outcomes
A more revealing picture emerges when performance is broken down by task category. Here, clear specializations become apparent. Llama was the top performer in the Coding category, while Mistral led in the Paraphrasing category. This reversal of rankings indicates that the models' architectures and training data may be optimized for different types of tasks. Table 2 presents the mean scores for each model in each category.

**Table 2: Mean Scores by Task Category**
| Model | Coding Mean Score | Paraphrasing Mean Score |
|---|---:|---:|
| Llama | **8.16** | 6.94 |
| Mistral | 8.01 | **7.29** |
| GPT-4.1-mini | 7.98 | 7.00 |

As shown, Llama's score of 8.16 in Coding was the highest in that category, but its performance dropped in the Paraphrasing tasks. Conversely, Mistral's leading score of 7.29 in Paraphrasing was offset by a lower score in Coding. GPT-4.1-mini showed the most balanced performance across the two categories, albeit without leading in either. This divergence strongly suggests that a "one-model-fits-all" approach may not be optimal; instead, selecting a model should be guided by the specific application.

### 3.3 Metric-Level Patterns
To understand the drivers behind these category-level scores, we analyzed performance at the metric level. This granular view highlights the specific strengths and weaknesses of the models.

For **Coding tasks**, all models scored exceptionally high on Readability, consistently producing well-formatted and easy-to-understand code. However, all three models struggled significantly with Error Handling, which was the lowest-scoring metric across the board. Llama's advantage in this category appears to stem from slightly better performance in Correctness and Efficiency.

**Table 3: Mean Scores for Coding Metrics**
| Metric (Weight) | Llama | Mistral | GPT-4.1-mini |
|---|---:|---:|---:|
| Correctness (0.40) | **8.5** | 8.2 | 8.1 |
| Efficiency (0.20) | **8.2** | 8.0 | 7.9 |
| Readability (0.20) | 9.9 | 9.9 | 9.9 |
| Error Handling (0.20) | 6.1 | 6.0 | 6.0 |

In the **Paraphrasing tasks**, a similar pattern of "surface vs. deep" quality emerged. All models were proficient in generating fluent and coherent text. However, they were much less successful at strict Prompt Adherence, often failing to respect all constraints given in a prompt. Mistral's lead in this category is attributable to its superior scores in Creativity & Originality and Relevance & Fidelity.

**Table 4: Mean Scores for Paraphrasing Metrics**
| Metric (Weight) | Mistral | Llama | GPT-4.1-mini |
|---|---:|---:|---:|
| Relevance & Fidelity (0.30) | **8.0** | 7.5 | 7.6 |
| Creativity & Originality (0.30)| **8.1** | 7.0 | 7.1 |
| Fluency & Coherence (0.20) | 7.8 | 7.7 | 7.6 |
| Prompt Adherence (0.20) | 5.4 | 5.3 | 5.5 |

These metric-level results suggest that current models are well-tuned for generating stylistically sound output, but less reliable when it comes to functional requirements like robustness and strict instruction following.

### 3.4 Variability and Reliability
The standard deviations of scores were consistently low (below 0.70) across all models and categories, indicating a generally reliable and predictable level of performance. However, there were occasional outlier responses. These were most notable in the Coding category, where both GPT-4.1-mini and Mistral produced solutions with scores in the mid-6.0s on prompts that involved complex algorithmic edge cases, such as handling empty or malformed inputs in a data processing task. This suggests that while their typical performance is high, their reliability may decrease when faced with non-standard problem constraints.

### 3.5 Interim Interpretation
The experimental results point towards a clear conclusion: model selection should be a task-aware process. The marginal aggregate differences between the models belie significant specializations. For applications requiring reliable program synthesis, Llama appears to be the strongest choice. For creative text generation and manipulation, Mistral holds a clear advantage. A portfolio-based approach, where different models are leveraged for different tasks within a larger system, would likely yield superior results compared to relying on a single model for all purposes.

## 4. Discussion

The results of this evaluation, while specific to the three models and two task families tested, reinforce several broader themes in contemporary LLM research and practice. First, it is clear that **no single model is universally superior**. The close aggregate scores, combined with the reversal of rankings in different task categories, powerfully illustrate the principle of "no free lunch." The notion of a single "best" model is increasingly untenable; deployment decisions must instead be based on a careful alignment of a model's specific capabilities with the demands of the target domain. This moves the focus from chasing leaderboard rankings to conducting task-specific bake-offs.

Second, we observe that **surface quality outpaces functional compliance**. A striking and consistent finding across all three models was the gap between high scores in "surface" qualities (readability, fluency) and low scores in "deep" functional compliance (error handling, prompt adherence). This suggests that current training methodologies, heavily reliant on optimizing for token-level prediction, are highly effective at capturing stylistic patterns but less so at instilling a robust understanding of functional requirements. This gap between eloquent output and functional reliability is a critical challenge for the practical application of LLMs in high-stakes domains.

Third, our study shows that **heuristic-based rubrics can effectively expose practical gaps**. The use of a simple, rule-based scoring rubric proved highly effective at identifying the practical weaknesses in the models' outputs. While automated benchmarks have their place, the targeted heuristics used here—such as checking for `try-except` blocks—surfaced critical issues that might be missed by more abstract metrics. This suggests that lightweight, expert-designed rubrics can be a cost-effective tool for guiding future fine-tuning efforts, allowing developers to focus on addressing specific, operationally relevant pain points.

### Limitations
This study, while rigorous, has several limitations that should be acknowledged. The evaluation relied on a single response generated for each prompt, and given the stochastic nature of LLMs, a model's output can vary between runs. Analyzing multiple generations would provide a more complete picture of a model's performance distribution. Furthermore, the scoring heuristics, while designed for objectivity, inherently contain subjective thresholds. For instance, the definition of "adequate" error handling could be debated. A follow-up study incorporating evaluation by human experts could help to validate and refine these rubric definitions. Finally, the scope was limited to two task categories, and the findings may not be generalizable to other domains such as mathematical reasoning or long-form document summarization.

### Future Work
The findings and limitations of this study suggest several promising directions for future research. Future evaluations should incorporate multiple response generations per prompt to analyze model consistency and the trade-offs between output diversity and quality. The evaluation framework could also be expanded to include other important task domains to build a more comprehensive map of the LLM capability landscape. A particularly valuable line of inquiry would be to investigate whether targeted, lightweight fine-tuning (such as LoRA) using a small dataset of examples demonstrating robust error handling and strict prompt adherence could mitigate the weaknesses identified in this study without diminishing the models' core strengths.

## 5. Conclusions

This study was undertaken to conduct a clear-sighted, task-aware comparison of three widely used language models. By combining a balanced set of prompts with a transparent, metric-driven scoring rubric, we have arrived at several principal insights. First, **performance is highly competitive at the aggregate level**, with grand-mean scores clustered within a very narrow range, indicating that differences in general capability among top-tier systems are small. Second, **task specialization is a decisive factor**, as a model's performance varies significantly by task. Llama demonstrated a distinct advantage in code generation, whereas Mistral excelled in creative writing, meaning model selection should be aligned with the specific workload. Third, **functional deficits are masked by surface polish**, as all models produced superficially impressive outputs while failing to address deeper requirements like robust exception handling. Finally, we found that **simple heuristics can effectively diagnose complex behaviors**, providing a cost-effective model for iterative assessment and targeted improvement of LLMs.

In sum, these findings advocate for a pragmatic and modular approach to the deployment of LLMs. Practitioners are advised to "pair the model to the job," actively monitor for compliance with functional requirements, and direct fine-tuning efforts toward areas that yield tangible operational benefits. The evaluation framework presented in this report is designed to be extensible and can be readily applied to future models and additional task domains, helping to separate genuine capability from marketing hype in the dynamic and crowded LLM landscape.

