# Coding Prompts (1-10)

### Prompt 1: Basic Function (Correctness & Readability)
**Prompt:** Write a Python function `calculate_triangle_area(base, height)` that calculates and returns the area of a triangle. Include a docstring explaining what the function does.

---

### Prompt 2: Input Validation (Correctness & Error Handling)
**Prompt:** Write a Python function `get_age(birth_year)` that returns a person's age. The function should raise a `ValueError` if the `birth_year` is in the future or implies an age over 130.

---

### Prompt 3: Data Structure Efficiency (Efficiency & Correctness)
**Prompt:** Given a list of integers, write a Python function `find_duplicates(nums)` that returns a list of all numbers that appear more than once. The function should be efficient and not use a nested loop (O(n^2) solution).

---

### Prompt 4: Simple Class (Readability & Correctness)
**Prompt:** Create a Python class `Book` with an `__init__` method that assigns `title`, `author`, and `year` as attributes. The class should also have a `get_description()` method that returns a string like "The book 'Title' was written by Author in Year."

---

### Prompt 5: File I/O (Error Handling)
**Prompt:** Write a Python function `read_first_line(file_path)` that reads and returns the first line of a file. The function must handle the `FileNotFoundError` and return `None` if the file doesn't exist.

---

### Prompt 6: Algorithm Implementation (Correctness & Efficiency)
**Prompt:** Implement the binary search algorithm in Python as a function `binary_search(sorted_list, target)`. The function should return the index of the `target` if found, otherwise return -1.

---

### Prompt 7: Code Refactoring (Readability)
**Prompt:** The following Python code is functionally correct but hard to read. Refactor it to improve its readability by using clearer variable names and better structure.
```python
def proc(d):
    r = {}
    for k, v in d.items():
        if v > 18:
            r[k] = "adult"
        else:
            r[k] = "minor"
    return r
```

---

### Prompt 8: String Parsing (Correctness & Error Handling)
**Prompt:** Write a Python function `parse_log_entry(log)` that takes a log string in the format `"LEVEL:MESSAGE"` (e.g., `"INFO:User logged in"`). It should return a dictionary `{'level': 'LEVEL', 'message': 'MESSAGE'}`. It should handle cases where the format is incorrect by returning `None`.

---

### Prompt 9: Recursion (Correctness & Readability)
**Prompt:** Write a recursive Python function `factorial(n)` to calculate the factorial of a non-negative integer `n`. Ensure the code is clear and includes a base case.

---

### Prompt 10: Combined Challenge (All Metrics)
**Prompt:** Write a Python function `word_frequency(text)` that takes a string, converts it to lowercase, removes all punctuation, and returns a dictionary where keys are words and values are their frequencies. The function should be efficient and handle empty input gracefully.

### Prompt 11: Data Analysis (Correctness & Efficiency)
**Prompt:** Write a Python function `average_column(csv_path, column_name)` that reads a CSV file using pandas and returns the average value of the specified numeric column. The function must handle the case where the column does not exist by raising a `KeyError`.

---

### Prompt 12: Memoization Decorator (Efficiency & Readability)
**Prompt:** Create a Python decorator `@memoize` that caches the results of a function for given arguments to avoid redundant calculations. Demonstrate its use with a recursive Fibonacci function.

---

### Prompt 13: Async I/O (Correctness & Error Handling)
**Prompt:** Using `aiohttp`, implement an asynchronous function `fetch_all(urls)` that concurrently fetches the text content of a list of URLs and returns a dictionary mapping each URL to its response text. Handle network errors gracefully by storing `None` for failed requests.

---

### Prompt 14: Secure SQL Query (Error Handling & Readability)
**Prompt:** Write a Python function `get_user_by_id(conn, user_id)` that retrieves a user record from an SQLite database using a parameterized query to prevent SQL injection. Include proper error handling for database connection issues.

---

### Prompt 15: Unit Testing (Correctness & Readability)
**Prompt:** Write a set of `unittest` test cases for the function `binary_search(sorted_list, target)` (from Prompt 6) covering typical, boundary, and error cases.

---

### Prompt 16: Context Manager (Readability & Efficiency)
**Prompt:** Implement a context manager class `Timer` that measures the execution time of a code block using the `with` statement and prints the elapsed time in milliseconds.

---

### Prompt 17: Multithreading (Efficiency & Error Handling)
**Prompt:** Write a Python function `sum_large_numbers(numbers)` that splits a large list of integers into chunks and sums them in parallel using `ThreadPoolExecutor`. Handle any exceptions raised in worker threads.

---

### Prompt 18: Regex Validation (Correctness & Readability)
**Prompt:** Implement a function `is_valid_email(email)` that returns `True` if the input string is a valid email address according to a reasonable regex pattern, otherwise `False`.

---

### Prompt 19: Graph Traversal (Correctness & Efficiency)
**Prompt:** Given an adjacency list representation of an unweighted graph, write a function `breadth_first_search(graph, start)` that returns the list of nodes visited in BFS order.

---

### Prompt 20: Command-Line Interface (All Metrics)
**Prompt:** Create a Python script `temp_convert.py` that can be run from the command line and converts temperatures between Celsius and Fahrenheit. Use `argparse` to parse arguments, handle invalid inputs gracefully, and print the converted value.

### Prompt 21: Data Visualization (Correctness & Readability)
**Prompt:** Write a Python function `plot_data(csv_path)` that reads a CSV file with columns 'x' and 'y', creates a scatter plot of the data using matplotlib, adds proper labels, a title, and saves the plot as 'scatter.png'.

---

### Prompt 22: Object-Oriented Design (Readability & Correctness)
**Prompt:** Design a class hierarchy for a simple banking system with a base class `Account` and two derived classes `SavingsAccount` and `CheckingAccount`. Each should have appropriate methods for deposit, withdrawal, and interest calculation.

---

### Prompt 23: Generator Function (Efficiency & Readability)
**Prompt:** Implement a Python generator function `prime_generator(limit)` that yields all prime numbers up to the given limit. The implementation should be memory-efficient and use a reasonable algorithm for checking primality.

---

### Prompt 24: API Client (Error Handling & Correctness)
**Prompt:** Create a Python function `get_weather(api_key, city)` that fetches current weather data for a given city using the OpenWeatherMap API. Handle API errors, network issues, and invalid inputs appropriately.

---

### Prompt 25: Sorting Algorithm (Efficiency & Correctness)
**Prompt:** Implement the merge sort algorithm in Python as a function `merge_sort(arr)` that sorts a list of numbers in ascending order. Include the merge function and ensure the implementation is correct and efficient.

---

### Prompt 26: Functional Programming (Readability & Efficiency)
**Prompt:** Using functional programming techniques (map, filter, reduce), write a Python function `process_data(numbers)` that takes a list of integers, filters out odd numbers, squares the remaining even numbers, and returns their sum.

---

### Prompt 27: Web Scraping (Error Handling & Correctness)
**Prompt:** Write a Python function `scrape_titles(url)` using BeautifulSoup that extracts all article titles (h2 elements) from a given webpage URL. Handle connection errors and invalid HTML gracefully.

---

### Prompt 28: Cache Implementation (Efficiency & Correctness)
**Prompt:** Implement a simple LRU (Least Recently Used) cache class in Python with methods `get(key)` and `put(key, value)` that have O(1) time complexity. The cache should have a fixed capacity and evict the least recently used item when full.

---

### Prompt 29: Concurrency Control (Error Handling & Efficiency)
**Prompt:** Write a Python function `download_all(urls, destination_folder)` that downloads files from multiple URLs concurrently using a thread pool. Limit the number of concurrent downloads to 5 and implement proper error handling.

---

### Prompt 30: Complete Application (All Metrics)
**Prompt:** Create a simple command-line todo list application in Python. The application should allow users to add tasks, mark tasks as complete, list all tasks, and save/load tasks from a JSON file. Include error handling, readable code, and efficient data structures. 