#!/usr/bin/env python3
"""
Updated LLM Evaluation Analysis Script
=====================================

This script analyzes the responses from three LLMs (GPT-4.1-mini, Llama, Mistral) 
across two evaluation categories (Coding and Paraphrasing) and calculates scores 
based on predefined metrics. Updated to work with the actual Excel structure.

Author: COMP 5541 Project
Date: 2025
"""

import pandas as pd
import numpy as np
import re
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

class UpdatedLLMAnalyzer:
    """
    A comprehensive analyzer for LLM evaluation responses.
    Updated to work with the actual Excel structure.
    """
    
    def __init__(self, excel_file: str = "records.xlsx"):
        """
        Initialize the analyzer with the Excel file containing responses.
        
        Args:
            excel_file (str): Path to the Excel file containing LLM responses
        """
        self.excel_file = excel_file
        self.data = {}
        self.results = {}
        
        # Coding metrics and weights
        self.coding_metrics = {
            'Correctness': 0.40,
            'Efficiency': 0.20,
            'Readability': 0.20,
            'Error Handling': 0.20
        }
        
        # Paraphrasing metrics and weights
        self.paraphrasing_metrics = {
            'Relevance & Fidelity': 0.30,
            'Creativity & Originality': 0.30,
            'Fluency & Coherence': 0.20,
            'Prompt Adherence': 0.20
        }
        
        self.models = ['GPT-4.1-mini', 'Llama', 'Mistral']
        
    def load_data(self) -> None:
        """
        Load data from the Excel file.
        """
        try:
            # Read all sheets
            excel_data = pd.read_excel(self.excel_file, sheet_name=None)
            
            print(f"Found {len(excel_data)} sheets in {self.excel_file}")
            for sheet_name in excel_data.keys():
                print(f"  - {sheet_name}: {len(excel_data[sheet_name])} rows")
                
            self.data = excel_data
            
        except FileNotFoundError:
            print(f"Error: Could not find {self.excel_file}")
            return
        except Exception as e:
            print(f"Error loading Excel file: {e}")
            return
    
    def evaluate_coding_response(self, response: str, prompt_id: str) -> Dict[str, float]:
        """
        Evaluate a coding response based on the defined metrics.
        
        Args:
            response (str): The LLM's response to evaluate
            prompt_id (str): The prompt ID (C01-C30)
            
        Returns:
            Dict with scores for each metric (0-10 scale)
        """
        if pd.isna(response) or response == '':
            return {metric: 0.0 for metric in self.coding_metrics.keys()}
        
        response = str(response).lower()
        scores = {}
        
        # Correctness (40% weight)
        correctness_score = 5.0  # Base score
        
        # Check for Python syntax elements
        if 'def ' in response:
            correctness_score += 1.5
        if 'return' in response:
            correctness_score += 1.0
        if 'import' in response or 'from' in response:
            correctness_score += 0.5
        if 'class ' in response:
            correctness_score += 1.0
        if any(keyword in response for keyword in ['if ', 'for ', 'while ', 'try:']):
            correctness_score += 0.5
        
        # Check for function calls and proper syntax
        if '(' in response and ')' in response:
            correctness_score += 0.5
        
        # Penalty for obvious errors
        if 'error' in response or 'exception' in response:
            if 'handle' not in response and 'try' not in response:
                correctness_score -= 1.0
        
        scores['Correctness'] = min(10.0, max(0.0, correctness_score))
        
        # Efficiency (20% weight)
        efficiency_score = 5.0  # Base score
        
        # Positive indicators
        if any(term in response for term in ['o(n)', 'o(log', 'efficient', 'optimize', 'complexity']):
            efficiency_score += 2.0
        if any(term in response for term in ['dict', 'set', 'hash', 'dictionary']):
            efficiency_score += 1.5
        if any(term in response for term in ['binary search', 'sort', 'heap']):
            efficiency_score += 1.0
        
        # Negative indicators
        if any(term in response for term in ['nested loop', 'o(n^2)', 'o(n²)', 'brute force']):
            efficiency_score -= 1.0
        
        scores['Efficiency'] = min(10.0, max(0.0, efficiency_score))
        
        # Readability (20% weight)
        readability_score = 5.0  # Base score
        
        # Check for good practices
        if '"""' in response or "'''" in response:  # Docstrings
            readability_score += 2.0
        if '#' in response:  # Comments
            readability_score += 1.5
        if len(response) > 100:  # Reasonable length
            readability_score += 0.5
        
        # Check for clear variable names (heuristic)
        words = response.split()
        descriptive_names = [word for word in words if len(word) > 3 and word.isalpha()]
        if len(descriptive_names) > 3:
            readability_score += 1.5
        
        # Check for proper indentation indicators
        if '    ' in response or '\t' in response:  # Indentation
            readability_score += 1.0
        
        scores['Readability'] = min(10.0, max(0.0, readability_score))
        
        # Error Handling (20% weight)
        error_handling_score = 3.0  # Base score
        
        # Check for error handling patterns
        if 'try:' in response and 'except' in response:
            error_handling_score += 4.0
        elif 'try:' in response or 'except' in response:
            error_handling_score += 2.0
        
        if 'raise' in response:
            error_handling_score += 2.0
        
        if any(term in response for term in ['valueerror', 'typeerror', 'filenotfounderror', 'keyerror']):
            error_handling_score += 1.5
        
        # Check for validation
        if any(term in response for term in ['if not', 'assert', 'validate']):
            error_handling_score += 1.0
        
        scores['Error Handling'] = min(10.0, max(0.0, error_handling_score))
        
        return scores
    
    def evaluate_paraphrasing_response(self, response: str, prompt_id: str) -> Dict[str, float]:
        """
        Evaluate a paraphrasing response based on the defined metrics.
        
        Args:
            response (str): The LLM's response to evaluate
            prompt_id (str): The prompt ID (P01-P30)
            
        Returns:
            Dict with scores for each metric (0-10 scale)
        """
        if pd.isna(response) or response == '':
            return {metric: 0.0 for metric in self.paraphrasing_metrics.keys()}
        
        response = str(response)
        scores = {}
        word_count = len(response.split())
        
        # Relevance & Fidelity (30% weight)
        relevance_score = 5.0  # Base score
        
        # Length appropriateness
        if 10 <= word_count <= 200:
            relevance_score += 2.5
        elif 200 < word_count <= 300:
            relevance_score += 1.5
        elif word_count > 300:
            relevance_score += 0.5
        elif word_count < 10:
            relevance_score -= 2.0
        
        # Check for direct copying (negative indicator)
        quote_count = response.count('"') + response.count("'")
        if quote_count > 6:  # Too many quotes might indicate copying
            relevance_score -= 1.0
        
        # Check for relevant content indicators
        if any(term in response.lower() for term in ['explain', 'describe', 'meaning', 'refers to']):
            relevance_score += 1.0
        
        scores['Relevance & Fidelity'] = min(10.0, max(0.0, relevance_score))
        
        # Creativity & Originality (30% weight)
        creativity_score = 5.0  # Base score
        
        # Check for creative elements
        if any(term in response.lower() for term in ['imagine', 'creative', 'unique', 'innovative']):
            creativity_score += 2.0
        
        # Check for varied vocabulary
        words = response.lower().split()
        unique_words = set(words)
        if len(words) > 0:
            vocab_diversity = len(unique_words) / len(words)
            if vocab_diversity > 0.8:  # High vocabulary diversity
                creativity_score += 2.0
            elif vocab_diversity > 0.6:
                creativity_score += 1.0
        
        # Check for creative formats (poems, stories, etc.)
        if any(term in response.lower() for term in ['haiku', 'poem', 'story', 'once upon', 'metaphor']):
            creativity_score += 2.5
        
        # Check for creative punctuation or formatting
        if any(char in response for char in ['!', '?', '...', '—', '–']):
            creativity_score += 0.5
        
        scores['Creativity & Originality'] = min(10.0, max(0.0, creativity_score))
        
        # Fluency & Coherence (20% weight)
        fluency_score = 6.0  # Base score
        
        # Check for proper sentence structure
        sentence_count = len([s for s in response.split('.') if s.strip()])
        if sentence_count >= 3:
            fluency_score += 2.0
        elif sentence_count >= 2:
            fluency_score += 1.0
        
        # Check for coherence indicators
        if any(term in response.lower() for term in ['however', 'therefore', 'furthermore', 'moreover', 'additionally', 'consequently']):
            fluency_score += 1.5
        
        # Check for proper grammar indicators
        if response.count(',') > 0:  # Use of commas
            fluency_score += 0.5
        
        # Penalty for very short responses
        if word_count < 5:
            fluency_score -= 3.0
        elif word_count < 10:
            fluency_score -= 1.0
        
        scores['Fluency & Coherence'] = min(10.0, max(0.0, fluency_score))
        
        # Prompt Adherence (20% weight)
        adherence_score = 5.0  # Base score
        
        # Extract prompt number for specific checks
        prompt_num = int(prompt_id[1:]) if prompt_id[1:].isdigit() else 0
        
        # Check for format adherence (emails, lists, etc.)
        if prompt_num in [8, 17]:  # Email or list format prompts
            if '@' in response or any(term in response.lower() for term in ['dear', 'sincerely', 'regards', 'email']):
                adherence_score += 2.0
            if any(term in response for term in ['1.', '2.', '3.', '•', '-', '*']):
                adherence_score += 1.5
        
        # Check for length constraints
        if prompt_num in [3, 25]:  # Haiku or specific length prompts
            if word_count <= 50:  # Reasonable constraint following
                adherence_score += 2.5
        
        # Check for tone/style adherence
        if any(term in response.lower() for term in ['formal', 'casual', 'professional', 'friendly']):
            adherence_score += 1.0
        
        # Check for specific format requirements
        if prompt_num == 23:  # Recipe to poem prompt
            if any(term in response.lower() for term in ['rhyme', 'verse', 'poem']):
                adherence_score += 2.0
        
        scores['Prompt Adherence'] = min(10.0, max(0.0, adherence_score))
        
        return scores
    
    def calculate_weighted_scores(self, metric_scores: Dict[str, float], 
                                 weights: Dict[str, float]) -> float:
        """
        Calculate weighted total score from individual metric scores.
        
        Args:
            metric_scores (Dict): Individual metric scores
            weights (Dict): Weights for each metric
            
        Returns:
            float: Weighted total score
        """
        total_score = 0.0
        for metric, score in metric_scores.items():
            if metric in weights:
                total_score += score * weights[metric]
        return total_score
    
    def process_and_update_excel(self) -> Dict:
        """
        Process all responses, calculate scores, and update the Excel file.
        
        Returns:
            Dict containing comprehensive analysis results
        """
        results = {
            'coding': {'detailed_scores': {}, 'summary': {}},
            'paraphrasing': {'detailed_scores': {}, 'summary': {}},
            'overall_summary': {}
        }
        
        # Process coding responses
        if 'Coding' in self.data:
            coding_df = self.data['Coding'].copy()
            
            print("Processing coding responses...")
            for idx, row in coding_df.iterrows():
                llm = row['LLM']
                response = row['Response']
                prompt_id = row['Prompt_ID']
                
                # Calculate metric scores
                metric_scores = self.evaluate_coding_response(response, prompt_id)
                weighted_score = self.calculate_weighted_scores(metric_scores, self.coding_metrics)
                
                # Update the dataframe
                coding_df.at[idx, 'Metric_A'] = metric_scores['Correctness']
                coding_df.at[idx, 'Metric_B'] = metric_scores['Efficiency'] 
                coding_df.at[idx, 'Metric_C'] = metric_scores['Readability']
                coding_df.at[idx, 'Metric_D'] = metric_scores['Error Handling']
                coding_df.at[idx, 'Score'] = weighted_score
                coding_df.at[idx, 'Mean_Score'] = weighted_score  # Same as Score for individual responses
                
                # Store for analysis
                if llm not in results['coding']['detailed_scores']:
                    results['coding']['detailed_scores'][llm] = []
                
                results['coding']['detailed_scores'][llm].append({
                    'prompt_id': prompt_id,
                    'response_length': len(str(response)) if pd.notna(response) else 0,
                    'metric_scores': metric_scores,
                    'weighted_score': weighted_score
                })
            
            # Update the original data
            self.data['Coding'] = coding_df
            
            # Calculate summary statistics
            for model in self.models:
                model_data = [item for item in results['coding']['detailed_scores'].get(model, [])]
                if model_data:
                    scores = [item['weighted_score'] for item in model_data]
                    results['coding']['summary'][model] = {
                        'average_score': np.mean(scores),
                        'median_score': np.median(scores),
                        'std_score': np.std(scores),
                        'min_score': np.min(scores),
                        'max_score': np.max(scores),
                        'total_responses': len(scores)
                    }
        
        # Process paraphrasing responses
        if 'Paraphrasing_Gen_Creation' in self.data:
            para_df = self.data['Paraphrasing_Gen_Creation'].copy()
            
            print("Processing paraphrasing responses...")
            for idx, row in para_df.iterrows():
                llm = row['LLM']
                response = row['Response']
                prompt_id = row['Prompt_ID']
                
                # Calculate metric scores
                metric_scores = self.evaluate_paraphrasing_response(response, prompt_id)
                weighted_score = self.calculate_weighted_scores(metric_scores, self.paraphrasing_metrics)
                
                # Update the dataframe
                para_df.at[idx, 'Metric_A'] = metric_scores['Relevance & Fidelity']
                para_df.at[idx, 'Metric_B'] = metric_scores['Creativity & Originality']
                para_df.at[idx, 'Metric_C'] = metric_scores['Fluency & Coherence']
                para_df.at[idx, 'Metric_D'] = metric_scores['Prompt Adherence']
                para_df.at[idx, 'Score'] = weighted_score
                para_df.at[idx, 'Mean_Score'] = weighted_score  # Same as Score for individual responses
                
                # Store for analysis
                if llm not in results['paraphrasing']['detailed_scores']:
                    results['paraphrasing']['detailed_scores'][llm] = []
                
                results['paraphrasing']['detailed_scores'][llm].append({
                    'prompt_id': prompt_id,
                    'response_length': len(str(response)) if pd.notna(response) else 0,
                    'metric_scores': metric_scores,
                    'weighted_score': weighted_score
                })
            
            # Update the original data
            self.data['Paraphrasing_Gen_Creation'] = para_df
            
            # Calculate summary statistics
            for model in self.models:
                model_data = [item for item in results['paraphrasing']['detailed_scores'].get(model, [])]
                if model_data:
                    scores = [item['weighted_score'] for item in model_data]
                    results['paraphrasing']['summary'][model] = {
                        'average_score': np.mean(scores),
                        'median_score': np.median(scores),
                        'std_score': np.std(scores),
                        'min_score': np.min(scores),
                        'max_score': np.max(scores),
                        'total_responses': len(scores)
                    }
        
        # Calculate overall summary
        overall_scores = {}
        for model in self.models:
            coding_avg = results['coding']['summary'].get(model, {}).get('average_score', 0)
            para_avg = results['paraphrasing']['summary'].get(model, {}).get('average_score', 0)
            overall_scores[model] = (coding_avg + para_avg) / 2
        
        results['overall_summary'] = {
            'model_rankings': sorted(overall_scores.items(), key=lambda x: x[1], reverse=True),
            'best_model': max(overall_scores.items(), key=lambda x: x[1])[0] if overall_scores else None,
            'score_differences': {
                model: overall_scores[model] - min(overall_scores.values()) 
                for model in overall_scores
            }
        }
        
        return results
    
    def save_updated_excel(self, filename: str = "records.xlsx") -> None:
        """
        Save the updated Excel file with calculated scores.
        
        Args:
            filename (str): Output filename
        """
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            for sheet_name, df in self.data.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"Updated Excel file saved as {filename}")
    
    def generate_report(self, results: Dict) -> str:
        """
        Generate a comprehensive text report from the analysis results.
        
        Args:
            results (Dict): Analysis results from process_and_update_excel()
            
        Returns:
            str: Formatted report text
        """
        report = []
        report.append("=" * 80)
        report.append("LLM EVALUATION ANALYSIS REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Overall rankings
        report.append("OVERALL MODEL RANKINGS")
        report.append("-" * 40)
        
        if results['overall_summary']['model_rankings']:
            for rank, (model, score) in enumerate(results['overall_summary']['model_rankings'], 1):
                report.append(f"{rank}. {model}: {score:.2f}/10")
        
        report.append("\n" + "=" * 80)
        report.append("PERFORMANCE ANALYSIS")
        report.append("=" * 80)
        
        # Coding results
        report.append("\nCODING CATEGORY RESULTS")
        report.append("-" * 40)
        
        if 'coding' in results and results['coding']['summary']:
            for model, stats in results['coding']['summary'].items():
                report.append(f"\n{model}:")
                report.append(f"  Average Score: {stats['average_score']:.2f}/10")
                report.append(f"  Median Score:  {stats['median_score']:.2f}/10")
                report.append(f"  Std Deviation: {stats['std_score']:.2f}")
                report.append(f"  Score Range:   {stats['min_score']:.2f} - {stats['max_score']:.2f}")
                report.append(f"  Total Responses: {stats['total_responses']}/30")
        
        # Paraphrasing results
        report.append("\nPARAPHRASING CATEGORY RESULTS")
        report.append("-" * 40)
        
        if 'paraphrasing' in results and results['paraphrasing']['summary']:
            for model, stats in results['paraphrasing']['summary'].items():
                report.append(f"\n{model}:")
                report.append(f"  Average Score: {stats['average_score']:.2f}/10")
                report.append(f"  Median Score:  {stats['median_score']:.2f}/10")
                report.append(f"  Std Deviation: {stats['std_score']:.2f}")
                report.append(f"  Score Range:   {stats['min_score']:.2f} - {stats['max_score']:.2f}")
                report.append(f"  Total Responses: {stats['total_responses']}/30")
        
        report.append("\n" + "=" * 80)
        report.append("DETAILED METRIC BREAKDOWN")
        report.append("=" * 80)
        
        # Coding metrics breakdown
        if 'coding' in results and results['coding']['detailed_scores']:
            report.append("\nCODING METRICS AVERAGE SCORES:")
            report.append("-" * 40)
            
            for model in self.models:
                if model in results['coding']['detailed_scores']:
                    report.append(f"\n{model}:")
                    metric_avgs = {}
                    for metric in self.coding_metrics:
                        scores = [item['metric_scores'][metric] for item in results['coding']['detailed_scores'][model]]
                        metric_avgs[metric] = np.mean(scores)
                        report.append(f"  {metric}: {metric_avgs[metric]:.2f}/10 (weight: {self.coding_metrics[metric]*100:.0f}%)")
        
        # Paraphrasing metrics breakdown
        if 'paraphrasing' in results and results['paraphrasing']['detailed_scores']:
            report.append("\nPARAPHRASING METRICS AVERAGE SCORES:")
            report.append("-" * 40)
            
            for model in self.models:
                if model in results['paraphrasing']['detailed_scores']:
                    report.append(f"\n{model}:")
                    metric_avgs = {}
                    for metric in self.paraphrasing_metrics:
                        scores = [item['metric_scores'][metric] for item in results['paraphrasing']['detailed_scores'][model]]
                        metric_avgs[metric] = np.mean(scores)
                        report.append(f"  {metric}: {metric_avgs[metric]:.2f}/10 (weight: {self.paraphrasing_metrics[metric]*100:.0f}%)")
        
        return "\n".join(report)

def main():
    """
    Main function to run the updated LLM analysis.
    """
    print("Starting Updated LLM Evaluation Analysis...")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = UpdatedLLMAnalyzer("records.xlsx")
    
    # Load data
    print("Loading data from records.xlsx...")
    analyzer.load_data()
    
    if not analyzer.data:
        print("No data loaded. Please check your records.xlsx file.")
        return
    
    # Process and calculate scores
    print("\nProcessing responses and calculating scores...")
    results = analyzer.process_and_update_excel()
    
    # Save updated Excel file
    print("\nSaving updated Excel file with calculated scores...")
    analyzer.save_updated_excel()
    
    # Generate and save report
    print("\nGenerating comprehensive report...")
    report = analyzer.generate_report(results)
    
    # Save text report
    with open("comprehensive_analysis_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("Analysis report saved to comprehensive_analysis_report.txt")
    
    # Print summary to console
    print("\n" + "=" * 50)
    print("ANALYSIS COMPLETE - SUMMARY")
    print("=" * 50)
    
    if results['overall_summary']['model_rankings']:
        print("\nModel Rankings:")
        for rank, (model, score) in enumerate(results['overall_summary']['model_rankings'], 1):
            print(f"{rank}. {model}: {score:.2f}/10")
    
    print("\nFiles generated:")
    print("  - records.xlsx (updated with calculated scores)")
    print("  - comprehensive_analysis_report.txt (detailed analysis report)")
    
    print("\nNext steps for your project:")
    print("  1. Review the calculated scores in records.xlsx")
    print("  2. Use the comprehensive report for your project analysis")
    print("  3. Proceed to write your project report sections")

if __name__ == "__main__":
    main() 