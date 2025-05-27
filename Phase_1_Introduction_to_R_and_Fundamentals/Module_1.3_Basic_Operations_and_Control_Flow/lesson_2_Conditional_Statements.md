# Lesson 2: Conditional Statements

* The `if` statement.
* `if-else` statements.
* `if-else if-else` ladders.
* Using `ifelse()` for vectorized conditional logic.

Okay, let's move on to **Lesson 2: Conditional Statements** within **Module 1.3: Basic Operations and Control Flow**.

Conditional statements are fundamental in programming for making decisions. They allow your R code to execute different blocks of instructions based on whether a specified condition is true or false.

---

### **Phase 1: Introduction to R and Fundamentals**
### **Module 1.3: Basic Operations and Control Flow**

---

### **Lesson 2: Conditional Statements**

This lesson delves into conditional statements, which are crucial for controlling the flow of your R programs. They enable your code to perform different actions depending on whether a logical condition evaluates to `TRUE` or `FALSE`.

---

#### **1. The `if` Statement**

The `if` statement is the simplest form of a conditional statement. It executes a block of code only if a specified condition is `TRUE`.

**Syntax:**

```R
if (condition) {
  # Code to execute if condition is TRUE
}
```

**Parameters:**

* `condition`: A logical expression that evaluates to `TRUE` or `FALSE`.

**Code Snippets:**

```r
# Example 1: Simple if statement
score <- 92

print("--- if Statement ---")
if (score >= 90) {
  print("Excellent! You got an A.")
}

# Example 2: Condition is FALSE, code inside if block is skipped
temperature <- 18 # degrees Celsius

if (temperature > 25) {
  print("It's hot outside!")
}
print("Finished checking temperature.")

# Example 3: Using a variable for the condition
is_raining <- TRUE

if (is_raining) {
  print("Remember to take an umbrella.")
}
```

**Output:**

```
[1] "--- if Statement ---"
[1] "Excellent! You got an A."
[1] "Finished checking temperature."
[1] "Remember to take an umbrella."
```

**Key Point:** If the condition evaluates to `FALSE` (or `NA`), the code inside the `if` block is simply skipped, and the program continues with the code immediately following the `if` block.

---

#### **2. The `if-else` Statement**

The `if-else` statement allows you to specify two blocks of code: one to be executed if the condition is `TRUE`, and another to be executed if the condition is `FALSE`.

**Syntax:**

```R
if (condition) {
  # Code to execute if condition is TRUE
} else {
  # Code to execute if condition is FALSE
}
```

**Code Snippets:**

```r
# Example 1: if-else for even/odd numbers
number <- 7

print("--- if-else Statement ---")
if (number %% 2 == 0) {
  print(paste(number, "is an even number."))
} else {
  print(paste(number, "is an odd number."))
}

# Example 2: if-else for eligibility
age <- 17

if (age >= 18) {
  print("You are eligible to vote.")
} else {
  print("You are not yet eligible to vote.")
}

# Example 3: Handling NA in condition
test_na <- NA
if (test_na == TRUE) { # This comparison results in NA
  print("This won't print.")
} else {
  print("This block executes because NA is not TRUE.")
}
```

**Output:**

```
[1] "--- if-else Statement ---"
[1] "7 is an odd number."
[1] "You are not yet eligible to vote."
[1] "This block executes because NA is not TRUE."
```

**Key Point:** For `if` and `if-else` statements, the `condition` must evaluate to a single `TRUE` or `FALSE`. If it evaluates to `NA`, the `else` block will be executed (or the `if` block skipped), and R will issue a warning.

---

#### **3. The `else if` Clause (Chained Conditionals)**

When you have more than two possible outcomes, you can chain multiple conditions using the `else if` clause. This allows you to check a series of conditions sequentially. The first condition that evaluates to `TRUE` will have its corresponding block of code executed, and then the entire `if-else if-else` structure is exited.

**Syntax:**

```R
if (condition1) {
  # Code if condition1 is TRUE
} else if (condition2) {
  # Code if condition1 is FALSE AND condition2 is TRUE
} else if (condition3) {
  # Code if condition1 and condition2 are FALSE AND condition3 is TRUE
} else {
  # Code if all preceding conditions are FALSE
}
```

**Code Snippets:**

```r
# Example: Grading system
student_grade <- 85

print("--- else if Clause ---")
if (student_grade >= 90) {
  print("Grade: A")
} else if (student_grade >= 80) {
  print("Grade: B")
} else if (student_grade >= 70) {
  print("Grade: C")
} else if (student_grade >= 60) {
  print("Grade: D")
} else {
  print("Grade: F")
}

# Example 2: Time of day greeting
current_hour <- 14 # 2 PM

if (current_hour < 12) {
  print("Good morning!")
} else if (current_hour >= 12 && current_hour < 18) {
  print("Good afternoon!")
} else {
  print("Good evening!")
}
```

**Output:**

```
[1] "--- else if Clause ---"
[1] "Grade: B"
[1] "Good afternoon!"
```

**Key Point:** The order of `else if` conditions matters. R evaluates them from top to bottom, and once a `TRUE` condition is found, the corresponding code block is executed, and no further `else if` or `else` blocks are checked.

---

#### **4. The `ifelse()` Function (Vectorized Conditional)**

Unlike `if`, `if-else`, and `else if` statements which are typically used for single conditions, `ifelse()` is a **vectorized** function. This means it can apply a conditional logic to each element of a vector, returning a vector of results. It's very efficient for element-wise conditional operations.

**Syntax:**

```R
ifelse(test, yes, no)
```

**Parameters:**

* `test`: A logical vector or an object that can be coerced to one.
* `yes`: A vector of values to be returned if the corresponding element of `test` is `TRUE`.
* `no`: A vector of values to be returned if the corresponding element of `test` is `FALSE`.

**Return Value:**

* A vector of the same length as `test`, with elements from `yes` or `no` based on the condition.

**Code Snippets:**

```r
# Example 1: Assigning "Pass"/"Fail" based on scores
student_scores <- c(75, 90, 60, 88, 55, 100)
passing_threshold <- 70

print("--- ifelse() Function (Vectorized) ---")
results_pass_fail <- ifelse(student_scores >= passing_threshold, "Pass", "Fail")
print("Pass/Fail results:")
print(results_pass_fail)

# Example 2: Calculating bonus based on sales (numeric output)
sales_figures <- c(1200, 800, 2500, 600)
bonus_threshold <- 1000
bonus_amount <- 100
no_bonus_amount <- 0

bonuses <- ifelse(sales_figures >= bonus_threshold, bonus_amount, no_bonus_amount)
print("Bonuses awarded:")
print(bonuses)

# Example 3: Handling NA with ifelse()
data_with_na <- c(10, NA, 20, 5, NA)
filled_na_data <- ifelse(is.na(data_with_na), 0, data_with_na)
print("Data with NA replaced by 0:")
print(filled_na_data)
```

**Output:**

```
[1] "--- ifelse() Function (Vectorized) ---"
[1] "Pass/Fail results:"
[1] "Pass" "Pass" "Fail" "Pass" "Fail" "Pass"
[1] "Bonuses awarded:"
[1] 100   0 100   0
[1] "Data with NA replaced by 0:"
[1] 10  0 20  5  0
```

**Key Point:** `ifelse()` is highly efficient for element-wise conditional operations on vectors and is often preferred over writing explicit `for` loops for such tasks.

---

#### **5. The `switch()` Statement**

The `switch()` statement is useful when you need to select one of several possible actions based on the value of a single expression. It's often cleaner than a long chain of `else if` statements when dealing with a discrete set of choices.

**Syntax:**

```R
switch(EXPR, CASE1, CASE2, CASE3, ...)
```

**Parameters:**

* `EXPR`: An expression that evaluates to a character string or a number.
* `CASE1, CASE2, ...`: These can be:
    * Named arguments (e.g., `case_value = result`). If `EXPR` matches `case_value`, `result` is returned.
    * Unnamed arguments (e.g., `result`). If `EXPR` is an integer `n`, the `n`-th unnamed argument is returned.
    * A default case (named `stop` or `default`) for unmatched `EXPR`.

**Return Value:**

* The value of the expression corresponding to the matched case, or `NULL` if no match and no default.

**Code Snippets:**

```r
# Example 1: switch by string name
day_of_week <- "Tuesday"

print("--- switch() Statement ---")
action <- switch(day_of_week,
                 "Monday" = "Start weekly planning",
                 "Tuesday" = "Team meeting",
                 "Wednesday" = "Mid-week check-in",
                 "Thursday" = "Client presentation",
                 "Friday" = "Prepare for weekend",
                 "Weekend" = "Relax and recharge",
                 "Invalid Day" # Default value if no match
                 )
print(paste("Today's action:", action))

# Example 2: switch by integer position (less common for readability)
choice <- 3 # Corresponds to the 3rd argument after EXPR

operation_result <- switch(choice,
                           "Add", # 1st
                           "Subtract", # 2nd
                           "Multiply", # 3rd
                           "Divide" # 4th
                           )
print(paste("Selected operation:", operation_result))

# Example 3: switch with a default case for unmatched value
color_choice <- "Purple"

message <- switch(color_choice,
                  "Red" = "Selected Red",
                  "Blue" = "Selected Blue",
                  "Green" = "Selected Green",
                  "default" = "Color not recognized" # Default case
                  )
print(paste("Color message:", message))
```

**Output:**

```
[1] "--- switch() Statement ---"
[1] "Today's action: Team meeting"
[1] "Selected operation: Multiply"
[1] "Color message: Color not recognized"
```

**Key Point:** `switch()` is best used when you have a clear, discrete set of possible values for an expression and you want to return a single result or execute a single line of code based on that value. For more complex logic or range-based conditions, `if-else if-else` chains are more appropriate.

---

This lesson provided a detailed exploration of R's conditional statements: `if`, `if-else`, `else if`, `ifelse()`, and `switch()`. These constructs are essential for introducing logic and decision-making into your R programs, allowing them to respond dynamically to different data and conditions.

**Next, we will proceed to Lesson 3: Loops.**
```