# Lesson 3: Loops

* The `for` loop: Iterating over sequences.
* The `while` loop: Repeating until a condition is met.
* The `repeat` loop: Infinite loops with `break`.
* Using `next` to skip iterations.
* Why vectorization is preferred over loops in R.

Let's continue to **Lesson 3: Loops** within **Module 1.3: Basic Operations and Control Flow**.

Loops are fundamental programming constructs that allow you to execute a block of code repeatedly. They are essential when you need to perform the same operation multiple times, either for a fixed number of iterations or until a certain condition is met.

---

### **Phase 1: Introduction to R and Fundamentals**
### **Module 1.3: Basic Operations and Control Flow**

---

### **Lesson 3: Loops**

This lesson covers the different types of loops available in R, which enable you to automate repetitive tasks. You'll learn about `for`, `while`, and `repeat` loops, as well as control statements like `break` and `next`. We'll also discuss the important concept of vectorization in R as an alternative to explicit loops.

---

#### **1. The `for` Loop**

The `for` loop is used to iterate over a sequence of elements (like a vector, list, or sequence of numbers), executing a block of code for each element. It's ideal when you know the number of iterations beforehand.

**Syntax:**

```R
for (variable in sequence) {
  # Code to execute for each element in the sequence
}
```

**Parameters:**

* `variable`: A temporary variable that takes on the value of each element in `sequence` during each iteration.
* `sequence`: A vector, list, or any object that can be iterated over (e.g., `1:10`, `c("a", "b")`).

**Code Snippets:**

```r
# Example 1: Iterating through numbers
print("--- for Loop: Iterating through numbers ---")
for (i in 1:5) {
  print(paste("Iteration number:", i))
}

# Example 2: Iterating through a character vector
fruits <- c("apple", "banana", "cherry")
print("--- for Loop: Iterating through fruits ---")
for (fruit in fruits) {
  print(paste("I like", fruit))
}

# Example 3: Calculating squares of numbers in a vector
numbers <- c(2, 4, 6, 8)
squared_numbers <- c() # Initialize an empty vector
print("--- for Loop: Calculating squares ---")
for (num in numbers) {
  squared_numbers <- c(squared_numbers, num^2) # Append squared value
}
print(paste("Original numbers:", paste(numbers, collapse = ", ")))
print(paste("Squared numbers:", paste(squared_numbers, collapse = ", ")))

# Example 4: Nested for loops (e.g., for matrices)
print("--- for Loop: Nested loops for a matrix ---")
my_matrix <- matrix(1:6, nrow = 2, byrow = TRUE)
print("Original Matrix:")
print(my_matrix)
for (row_idx in 1:nrow(my_matrix)) {
  for (col_idx in 1:ncol(my_matrix)) {
    print(paste("Element at [", row_idx, ",", col_idx, "]:", my_matrix[row_idx, col_idx]))
  }
}
```

**Output:**

```
[1] "--- for Loop: Iterating through numbers ---"
[1] "Iteration number: 1"
[1] "Iteration number: 2"
[1] "Iteration number: 3"
[1] "Iteration number: 4"
[1] "Iteration number: 5"
[1] "--- for Loop: Iterating through fruits ---"
[1] "I like apple"
[1] "I like banana"
[1] "I like cherry"
[1] "--- for Loop: Calculating squares ---"
[1] "Original numbers: 2, 4, 6, 8"
[1] "Squared numbers: 4, 16, 36, 64"
[1] "--- for Loop: Nested loops for a matrix ---"
[1] "Original Matrix:"
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[1] "Element at [ 1 , 1 ]: 1"
[1] "Element at [ 1 , 2 ]: 2"
[1] "Element at [ 1 , 3 ]: 3"
[1] "Element at [ 2 , 1 ]: 4"
[1] "Element at [ 2 , 2 ]: 5"
[1] "Element at [ 2 , 3 ]: 6"
```

---

#### **2. The `while` Loop**

The `while` loop repeatedly executes a block of code as long as a specified condition remains `TRUE`. It's suitable when you don't know the exact number of iterations beforehand, but rather want to loop until a condition is met.

**Syntax:**

```R
while (condition) {
  # Code to execute as long as condition is TRUE
  # Make sure to include code that eventually makes the condition FALSE
}
```

**Parameters:**

* `condition`: A logical expression that is evaluated at the beginning of each iteration.

**Code Snippets:**

```r
# Example 1: Countdown
count <- 5
print("--- while Loop: Countdown ---")
while (count > 0) {
  print(paste("Count:", count))
  count <- count - 1 # Decrement count, eventually making condition FALSE
}
print("Blast off!")

# Example 2: Summing numbers until a limit is reached
current_sum <- 0
num <- 1
limit <- 15
print("--- while Loop: Summing until limit ---")
while (current_sum < limit) {
  current_sum <- current_sum + num
  print(paste("Adding", num, ". Current sum:", current_sum))
  num <- num + 1
}
print(paste("Sum exceeded limit (", limit, "). Final sum:", current_sum))
```

**Output:**

```
[1] "--- while Loop: Countdown ---"
[1] "Count: 5"
[1] "Count: 4"
[1] "Count: 3"
[1] "Count: 2"
[1] "Count: 1"
[1] "Blast off!"
[1] "--- while Loop: Summing until limit ---"
[1] "Adding 1 . Current sum: 1"
[1] "Adding 2 . Current sum: 3"
[1] "Adding 3 . Current sum: 6"
[1] "Adding 4 . Current sum: 10"
[1] "Adding 5 . Current sum: 15"
[1] "Sum exceeded limit ( 15 ). Final sum: 15"
```

**Caution:** Be careful with `while` loops to avoid **infinite loops**. Ensure that the condition inside the loop will eventually become `FALSE`, or your program will run indefinitely.

---

#### **3. The `repeat` Loop**

The `repeat` loop executes a block of code indefinitely until an explicit `break` statement is encountered. This means you must include a `break` statement inside the loop based on some condition, otherwise it will be an infinite loop.

**Syntax:**

```R
repeat {
  # Code to execute repeatedly
  if (condition_to_break) {
    break # Exit the loop
  }
}
```

**Code Snippets:**

```r
# Example: Simulating a dice roll until a 6 is rolled
roll <- 0
attempts <- 0
print("--- repeat Loop: Dice Roll Simulation ---")
repeat {
  attempts <- attempts + 1
  roll <- sample(1:6, 1) # Roll a single die (random number from 1 to 6)
  print(paste("Attempt", attempts, ": Rolled", roll))
  if (roll == 6) {
    print("Got a 6! Breaking the loop.")
    break # Exit the loop
  }
}
print(paste("It took", attempts, "attempts to roll a 6."))
```

**Output:** (Output will vary due to random `sample()` function)

```
[1] "--- repeat Loop: Dice Roll Simulation ---"
[1] "Attempt 1 : Rolled 3"
[1] "Attempt 2 : Rolled 1"
[1] "Attempt 3 : Rolled 6"
[1] "Got a 6! Breaking the loop."
[1] "It took 3 attempts to roll a 6."
```

**Key Point:** Always include a `break` condition within a `repeat` loop to prevent it from running forever.

---

#### **4. `break` and `next` Statements**

These control statements allow you to alter the normal execution flow of loops.

* `break`: Immediately terminates the loop and transfers control to the statement immediately following the loop.
* `next`: Skips the rest of the current iteration of the loop and proceeds to the next iteration.

**Code Snippets:**

```r
# Example 1: Using 'break' to stop a loop early
print("--- Using 'break' ---")
for (i in 1:10) {
  if (i == 6) {
    print("Found 6, breaking the loop.")
    break # Exit the loop immediately
  }
  print(paste("Current number:", i))
}

# Example 2: Using 'next' to skip an iteration
print("--- Using 'next' ---")
for (j in 1:5) {
  if (j %% 2 != 0) { # If j is odd
    print(paste(j, "is odd, skipping to next iteration."))
    next # Skip the rest of this iteration
  }
  print(paste(j, "is even. Processing it."))
}
```

**Output:**

```
[1] "--- Using 'break' ---"
[1] "Current number: 1"
[1] "Current number: 2"
[1] "Current number: 3"
[1] "Current number: 4"
[1] "Current number: 5"
[1] "Found 6, breaking the loop."
[1] "--- Using 'next' ---"
[1] "1 is odd, skipping to next iteration."
[1] "2 is even. Processing it."
[1] "3 is odd, skipping to next iteration."
[1] "4 is even. Processing it."
[1] "5 is odd, skipping to next iteration."
```

---

#### **5. Vectorization vs. Loops (Efficiency Considerations)**

In R, loops (especially `for` loops) can sometimes be slower than vectorized operations. **Vectorization** means performing operations on entire vectors or matrices at once, rather than iterating through individual elements. R is optimized for vectorized operations, making them much faster and more memory-efficient for large datasets.

Wherever possible, prefer vectorized solutions over explicit loops in R.

**Code Snippets:**

```r
# Example: Calculating the square root of many numbers

# Method 1: Using a for loop (less efficient for large vectors)
my_numbers_loop <- 1:100000
start_time_loop <- Sys.time()
sqrt_results_loop <- numeric(length(my_numbers_loop)) # Pre-allocate memory (good practice in loops)
for (i in 1:length(my_numbers_loop)) {
  sqrt_results_loop[i] <- sqrt(my_numbers_loop[i])
}
end_time_loop <- Sys.time()
time_taken_loop <- end_time_loop - start_time_loop
print("--- Vectorization vs. Loops ---")
print(paste("Time taken by for loop:", round(as.numeric(time_taken_loop), 5), "seconds"))

# Method 2: Using a vectorized function (much faster)
my_numbers_vec <- 1:100000
start_time_vec <- Sys.time()
sqrt_results_vec <- sqrt(my_numbers_vec) # Vectorized operation
end_time_vec <- Sys.time()
time_taken_vec <- end_time_vec - start_time_vec
print(paste("Time taken by vectorized operation:", round(as.numeric(time_taken_vec), 5), "seconds"))

# Verify results are the same (first few elements)
print(paste("Are results from both methods identical (first 5 elements)?", all(sqrt_results_loop[1:5] == sqrt_results_vec[1:5])))
```

**Output:** (Times will vary depending on your system, but vectorized will almost always be faster)

```
[1] "--- Vectorization vs. Loops ---"
[1] "Time taken by for loop: 0.00767 seconds"
[1] "Time taken by vectorized operation: 0.00036 seconds"
[1] "Are results from both methods identical (first 5 elements)? TRUE"
```

**Key Takeaway:** While loops are essential for certain programming logic (like simulating events until a condition is met), for tasks that can be performed element-wise on entire vectors or matrices, always prioritize R's built-in vectorized functions (`sum()`, `mean()`, `sqrt()`, `+`, `*`, etc.) or functions from optimized packages.

---

This lesson provided a detailed understanding of `for`, `while`, and `repeat` loops, along with the `break` and `next` control statements. Crucially, we also emphasized the importance of vectorization in R for performance optimization. You now have the tools to implement repetitive tasks efficiently in your R programs.

**Next, we will proceed to Module 1.4: Functions and Packages, starting with Lesson 1: Built-in Functions.**