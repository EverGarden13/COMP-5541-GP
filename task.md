COMP 5541: Machine Learning and Data Analytics
Group Project
PolyU Summer 2025
1 Task Description
In the field of artificial intelligence, large language models (LLMs) have gained significant
attention and are currently one of the most popular topics. In this project, you will work
in teams to conduct a comprehensiveevaluationof the capabilities of popular LLMs. We
have provided 12 general evaluation categories as a starting point, and you are encouraged
to select from them. Additionally, you have the freedom to propose your own evaluation
categories, providing an opportunity to explore and assess additional aspects of the LLMs
beyond the given set. By actively engaging in hands-on evaluation, you will acquire prac-
tical experience working with these models and deepen your understanding of their usage,
capabilities, and distinctions.

Semantic Understanding
Abstractive Summarization
Conversations and Dialogue
Reasoning
Knowledge and Factuality
Character Simulation
Paraphrasing, Generation, and Creation
Coding
Effectiveness of Tool Use
Multilingualism
Math and Computing
Safety
Each member of your team will need to:
Select Evaluation Categories: Each team member is required to selecttwo cate-
goriesfor evaluation. You may choose from the provided list or propose your own
categories.It is essential to ensure that there are no duplicated categories chosen
by different team members. By collectively evaluating from different perspectives,
your team will conduct a comprehensive assessment on the capabilities of LLMs.
Select LLMs: Selecta minimum of three LLMsfor LLM evaluation. You have
six optional LLM bots to consider: DeepSeek (R1), ChatGPT4 (4.1-Mini), Qwen
3 (235B), Llama-3.3 (70B), Mixtral (instruct-large), Doubao. Please make sure
that all the team members use the same LLMs. Hints: there are some websites
possibly useful for your evaluation: 1.Poe.com^1 , 2.PolyU GenAI^2 , 3.DeepSeek^3 ,
4.ChatGPT^4 , 5.Qwen3^5 , 6.DouBao^6
Design Evaluation Metrics: Developappropriate evaluation metricsfor each se-
lected category. Ensure that the metrics are relevant and can effectively measure the
performance of the LLMs in the chosen categories. You can find some examples in
Section 2.
Design Prompts: For each chosen category, you are required to design30 prompts,
based on the proposed evaluation metrics in Step 3, to evaluate the performance of
LLMs. You can find some examples in Section 2.
Analyze Performance: Use the designed prompts to gather responses from the cho-
sen LLMs and perform a comprehensive analysis of their performance under the
reasonable and appropriate metrics.
Write Project Report: Collaboratively, as a team, write a project report that consol-
Prepare Project Presentation
idates the performance of the chosen LLMs across the selected task categories
(from the above categories). Provide a detailed discussion highlighting the respective
advantages and limitations of different LLMs in relation to the evaluation categories
and metrics.
: Prepare a PPT presentation to summarize the out-
comes of this project. The presentation should effectively communicate the method-
ology employed, experimental findings obtained, and the conclusions drawn from
this project.
(^1) https://poe.com
(^2) https://genai.polyu.edu.hk
(^3) https://www.deepseek.com
(^4) https://chatgpt.com/
(^5) https://chat.qwen.ai/
(^6) https://www.doubao.com/chat/

2 Example: Coding
We have provided a variety of potential categories for evaluating LLMs. Let’s use the
Codingcategory as an example.
2.1 Evaluation Metrics
The evaluation metrics for the LLMs’ coding capability can include various aspects such
as correctness, efficiency, clarity, and adherence to coding standards. In Table 1 below, we
provide some examples for you as a reference.
2.2 Prompt Examples
Based on the proposed evaluation metrics, we can design a series of prompts that cover
various aspects of LLMs’ coding capability. These aspects may include:
Implementing Functions
Writing Unit Tests for a Given Function
Completing the Next Line of Code
Generating Comments for a Given Function or Class
Generating Variable Names
Generating Commit Messages
...
Prompt Example 1: Implementing Functions
1 Could you please help me write the code based on the provided
2 comments? Ensure that the code is correct and efficient. Please use
3 meaningful variable names , add comments for readability , and make
4 the code easy to understand. Finally , if there are any potential
5 errors , kindly include error handling code.
6
7 # Function to find the maximum element in a list
8 # Input: a list of integers lst
9 # Output: the maximum integer in lst
10 def find_max(lst):
11 # Please help me write the code here

Prompt Example 2: Writing Unit Tests
1 Could you help me write the code based on the provided comments?
2 Ensure that the code is correct and efficient. Please use meaningful
3 variable names and add comments to enhance readability. Make the
4 code easy to understand , and include error handling for any
5 potential issues.
6
7 def add(a, b):
8 return a + b
9 # Please help me write unit tests here

2.3 Result Analysis and Reporting
After collecting responses from the LLMs using your designed prompts, apply the specified
evaluation metrics and their respective weights to calculate the overall score for each cate-
gory. Then, compare the performances of the different models. Summarize your findings
in the project report, and analyze potential reasons for the superior or inferior performance
of different LLMs based on your understanding.
3 Team Formation Rule
We strongly encourage you to form teams consisting of 4 to 5 members for this project.
It is important to note that all teams, regardless of size, will be evaluated using the same
rubrics. If you wish to work in teams with fewer than 4 or more than 5 members, you must
seek approval by sending an email to the teaching team along with a valid justification.
Please submit your team information using the providedGoogle Sheet^7 by25 June.
Failure to submit your team information by this deadline will result in random team assign-
ments. To ensure you have sufficient time to finish this project, any change of your team
will NOT BE ALLOWED after 25 June. If you have any concerns, please reach out to the
teaching team as early as possible.
4 Submission Guideline
Submission Deadline 10 July 23:59pm. The late submission will be subjected to 30
marks deduction for every single day of delay.
Project Records and Evaluation Metrics
“records.xlsx” to record the evaluation metrics and experimental results. The first work-
sheet in this Excel file should be a summary of evaluation metric descriptions (similar to
Table 1 ). In addition to this worksheet, please create a separate worksheet for each chosen
evaluation category.
Please use the provided Excel file named
Please submit one “records.xlsx” to us for the whole group.
(^7) https://docs.google.com/spreadsheets/d/1DVWjKbRFt-JuSQ9iGe3-AT3j2UTlx8uTpSdxci_
MTZ0/edit?usp=sharing

Table 1: Example Evaluation Metrics.
Category Metric Weightage Description Justification

Coding Correctness 40% Does the gener-
ated code fulfill
the requirements
specified in the
comments?

Correctness is essen-
tial because incorrect
code is unusable.
Coding Efficiency 20% Has the code been
optimized for per-
formance?

Efficiency matters for
performance, which
can be critical in many
applications.
Coding Readability 20% Is the code easy
to read and un-
derstand, with ap-
propriate indenta-
tion and consis-
tent naming con-
ventions?

Readable code is eas-
ier to maintain and un-
derstand. This in-
cludes proper inden-
tation, naming con-
ventions, and over-
all structure. Read-
ability is crucial for
collaborative projects
and long-term mainte-
nance.
Coding Error Han-
dling

20% Does the code
handle potential
errors and edge
cases appropri-
ately?
Error Handling is nec-
essary for creating ro-
bust and reliable soft-
ware.
Project Report (Page limit: 20 pages) The report should cover all key aspects of the
project, including Introduction, Methodology, Experimental Results and Analysis, and
Conclusions. Please provide the Name and Student ID of all team members at the be-
ginning of your report.

PowerPoint Presentation Recording (Time limit:≤10 minutes) Please prepare a PPT
presentation to summarise the key outcomes of this project. When organizing the content
of your presentation, it is recommended to follow the same structure as the Project Report
for consistency.

Submission Rule Please submit a compressed folder (in zip or rar) with all your run-
ning records (Excel file), report (PDF format), PPT slides, and web link to your video
presentation. Please name the folder with your Team ID, such as “10.zip” or “10.rar”. The
compressed folder should be submitted to theblackboardand the submission entry is: As-
sessments/Group Project. Please keep the file size of all materials as small as possible (less
than 20 MB). Take note that only one team member needs to upload all materials to the
blackboard. Don’t forget to double-check if the submission is saved successfully before
leaving. Multiple submissions are allowed, and we will only mark the latest version.

Extra Note Engaging in any form of cheating or plagiarism, if detected, will lead to
a score of zero for the assignment, and all individuals involved will be reported to the
department.

5 Grading Rubrics
Group projects will be assigned a single grade, which will be applied to all team members.

Running Results:All chosen categories are thoroughly evaluated with comprehen-
sive results. Results from all LLMs are well-documented, including the chosen cat-
egories, evaluation metrics, LLM names, prompts, and responses from LLMs (
marks).
Suitability of LLM Evaluation Metrics: Evaluation metrics are highly relevant
and appropriate for the chosen category, covering a wide range of critical dimensions
(≥5). Clear and well-articulated justifications for each chosen metric, explaining
why it is critical for evaluating LLM performance (20 marks).
Quality of the Project Report: The report covers all key aspects of the project,
including Introduction (5 marks), Methodology (5 marks), Experimental Results and
Analysis (8 marks), and Conclusions (2 marks).
Quality of Presentation:The presentation comprehensively covers all key aspects
of the project report (10 marks) and effectively communicates the project’s findings
and significance to the audience (20 marks).