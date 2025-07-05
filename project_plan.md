# COMP 5541: LLM Evaluation Project Plan

This document outlines the plan for our group project on the comprehensive evaluation of Large Language Models (LLMs) for the COMP 5541 course.

This plan is structured based on best practices for project planning, referencing HubSpot's project plan template [1].

## 1. Project Overview

The goal of this project is to conduct a systematic and in-depth evaluation of the capabilities of several state-of-the-art LLMs. We will assess their performance across a diverse set of evaluation categories, design rigorous metrics, and analyze their strengths and weaknesses. The final output will be a comprehensive report and presentation of our findings.

## 2. Objectives

Our primary objectives are:
1.  To gain practical experience in working with and evaluating modern LLMs.
2.  To develop a deep understanding of the capabilities and limitations of different models.
3.  To design and apply a robust methodology for LLM evaluation, including metric design and prompt engineering.
4.  To collaboratively produce a high-quality project report and presentation that details our findings.
5.  To successfully meet all project requirements and deadlines as specified in the course task description.

## 3. Scope

### 3.1. Selected LLMs

As per the project requirements, all team members will use the same set of LLMs for evaluation. We will evaluate a minimum of three models to ensure a comparative analysis. Based on the available models and prioritizing cost-effectiveness, we will use the following three:

1.  **GPT-4.1-mini**: A smaller, more efficient version of the GPT-4 series, suitable for a wide range of tasks.
2.  **Llama (Llama-4-Scout-17B-16E-Instruct)**: A capable open-source model from Meta, offering a good balance of performance and resource usage.
3.  **Mistral (Magistral-Small-2506)**: A lightweight and efficient model known for its strong reasoning capabilities for its size.

This selection provides a balanced mix of proprietary and open-source models that are well-suited for extensive evaluation without incurring high costs.

### 3.2. Evaluation Categories

As a solo team member, you are required to select two evaluation categories. This plan will focus on the following two:

1.  **Coding**: To evaluate the LLMs' ability to generate correct, efficient, and readable code.
2.  **Paraphrasing, Generation, and Creation**: To assess the model's ability to rephrase text, generate novel content, and adhere to creative instructions.

## 4. Roles and Responsibilities

As the sole member of this project, you will assume all roles and responsibilities, including:

*   **Project Management**: Overseeing the project timeline, ensuring all deadlines are met, and handling the final submission.
*   **Evaluation Design**: Developing appropriate evaluation metrics and designing 30 prompts for each of the two chosen categories.
*   **Execution & Analysis**: Running the prompts, collecting responses from the LLMs, analyzing the results, and documenting everything in `records.xlsx`.
*   **Report & Presentation**: Writing the entire project report and creating and recording the final presentation.

## 5. Deliverables

As per the project guidelines, you will produce the following:

1.  **`records.xlsx`**: An Excel file containing:
    *   A worksheet describing all evaluation metrics and their justifications.
    *   A separate worksheet for each of the 2 evaluation categories, documenting prompts, LLM responses, and scores.
2.  **Project Report**: A PDF document (max 20 pages) detailing your methodology, results, analysis, and conclusions.
3.  **Presentation**: A 10-minute (max) video recording of a PowerPoint presentation summarizing the project.

## 6. Project Checklist

This checklist outlines the key tasks to be completed for the project.

### Phase 1: Planning & Setup
- [x] Finalize project plan (LLMs, Categories, Metrics)
- [x] Set up the `records.xlsx` file with worksheets for metrics and the two categories.

### Phase 2: Prompt Design & Evaluation
- [x] Design 30 prompts for the "Coding" category based on the defined metrics.
- [x] Design 30 prompts for the "Paraphrasing, Generation, and Creation" category.
- [x] Run all 60 prompts on `GPT-4.1-mini` and record results.
- [x] Run all 60 prompts on `Llama` and record results.
- [x] Run all 60 prompts on `Mistral` and record results.
- [x] Format and import all coding responses into `records.xlsx` (86/90 responses added).
- [x] Format and import all paraphrasing responses into `records.xlsx` (90/90 responses added).

### Phase 3: Analysis & Reporting
- [x] Fill in any remaining empty responses in `records.xlsx`.
- [x] Script of analysis response and calculate score of it.
- [x] Analyze the collected data in `records.xlsx`.
- [ ] Write the "Introduction" section of the report.
- [ ] Write the "Methodology" section of the report.
- [ ] Write the "Experimental Results and Analysis" section of the report.
- [ ] Write the "Conclusions" section of the report.
- [ ] Assemble and format the complete project report as a PDF.

### Phase 4: Presentation & Submission
- [ ] Create the PowerPoint presentation slides.
- [ ] Record the 10-minute video presentation.
- [ ] Review all deliverables (`records.xlsx`, report, presentation).
- [ ] Compress all files into a single `.zip` archive named according to the submission guidelines.
- [ ] Submit the final project to Blackboard.

## 7. Evaluation Metrics

This section outlines the metrics for evaluating the LLMs in the chosen categories. These will be used to score the model responses and will be detailed in the `records.xlsx` file.

### 7.1. Coding

| Metric | Weightage | Description | Justification |
| :--- | :--- | :--- | :--- |
| **Correctness** | 40% | Does the generated code fulfill the requirements specified in the comments? | Correctness is essential because incorrect code is unusable. |
| **Efficiency** | 20% | Has the code been optimized for performance? | Efficiency matters for performance, which can be critical in many applications. |
| **Readability** | 20% | Is the code easy to read and understand, with appropriate indentation and consistent naming conventions? | Readable code is easier to maintain and understand. This is crucial for collaborative projects and long-term maintenance. |
| **Error Handling** | 20% | Does the code handle potential errors and edge cases appropriately? | Error handling is necessary for creating robust and reliable software. |

### 7.2. Paraphrasing, Generation, and Creation

| Metric | Weightage | Description | Justification |
| :--- | :--- | :--- | :--- |
| **Relevance & Fidelity** | 30% | For paraphrasing, does the output accurately preserve the core meaning of the source text? For generation, is the output relevant to the prompt? | The primary purpose of paraphrasing is to rephrase without losing the original intent. For generation, relevance is the baseline for a useful response. |
| **Creativity & Originality**| 30% | Does the model produce unique, imaginative, and non-repetitive content in response to creative prompts? | This metric evaluates the model's ability to go beyond simple information retrieval and engage in true content creation. |
| **Fluency & Coherence** | 20% | Is the output text grammatically correct, well-structured, and natural-sounding? Does it flow logically? | Poor fluency and coherence make the content unusable, regardless of its creativity or relevance. It is a foundational quality. |
| **Prompt Adherence** | 20% | Does the generated content adhere to all constraints specified in the prompt (e.g., tone, style, length, format)? | A model's ability to follow instructions is crucial for its practical utility in real-world applications where specific outputs are required. |

## 8. Tools and Resources

*   **LLM Access:** Poe.com, PolyU GenAI, and direct access websites (DeepSeek, ChatGPT, etc.)
*   **Collaboration:** Google Docs/Sheets for collaborative writing and data management.
*   **Communication:** WeChat/Discord/Zoom for team meetings.
*   **Reporting:** Microsoft Word / LaTeX for the report, Microsoft PowerPoint for the presentation.

## 9. References

[1] HubSpot. "How to Create a Project Plan: The Ultimate Guide." [https://www.hubspot.com/business-templates/project-plan](https://www.hubspot.com/business-templates/project-plan) 