# Lesson 1: Operators

* Arithmetic Operators.
* Relational Operators (==, !=, <, >, <=, >=).
* Logical Operators (`&`, `|`, `!`, `&&`, `||`).
* Miscellaneous Operators (`%in%`, `%*%`).

Got it! Let's dive into **Module 1.3: Basic Operations and Control Flow**, starting with **Lesson 1: Operators**.

Operators are special symbols or keywords that perform operations on values and variables. Understanding them is fundamental to writing any code in R.

---

### **Phase 1: Introduction to R and Fundamentals**
### **Module 1.3: Basic Operations and Control Flow**

---

### **Lesson 1: Operators**

This lesson covers the various types of operators available in R. Operators are symbols or keywords that perform operations on one or more values (called operands) to produce a result. Mastering operators is crucial for performing calculations, making comparisons, and controlling the flow of your R programs.

---

#### **1. Arithmetic Operators**

Arithmetic operators are used to perform basic mathematical calculations.

| Operator | Description    | Example      |
| :------- | :------------- | :----------- |
| `+`      | Addition       | `5 + 3`      |
| `-`      | Subtraction    | `5 - 3`      |
| `*`      | Multiplication | `5 * 3`      |
| `/`      | Division       | `5 / 3`      |
| `^` or `**` | Exponentiation | `5 ^ 2` or `5 ** 2` |
| `%%`     | Modulus (Remainder) | `5 %% 3`     |
| `%/%`    | Integer Division (Quotient) | `5 %/% 3`    |

**Code Snippets:**

```r
# Arithmetic Operators

a <- 10
b <- 3

print("--- Arithmetic Operations ---")

# Addition
result_add <- a + b
print(paste("1. Addition (a + b):", result_add))

# Subtraction
result_sub <- a - b
print(paste("2. Subtraction (a - b):", result_sub))

# Multiplication
result_mul <- a * b
print(paste("3. Multiplication (a * b):", result_mul))

# Division
result_div <- a / b
print(paste("4. Division (a / b):", result_div))

# Exponentiation
result_exp <- a ^ 2 # a to the power of 2
print(paste("5. Exponentiation (a ^ 2):", result_exp))
result_exp_alt <- a ** 3 # a to the power of 3 (alternative syntax)
print(paste("   Exponentiation (a ** 3):", result_exp_alt))

# Modulus (Remainder)
result_mod <- a %% b # 10 divided by 3, remainder is 1
print(paste("6. Modulus (a %% b):", result_mod))

# Integer Division (Quotient)
result_int_div <- a %/% b # 10 divided by 3, integer part is 3
print(paste("7. Integer Division (a %/% b):", result_int_div))

# Operators also work with vectors (element-wise operation)
vec1 <- c(1, 2, 3)
vec2 <- c(4, 5, 6)
vec_sum <- vec1 + vec2
print(paste("8. Vector Addition (element-wise):", paste(vec_sum, collapse = ", ")))
```

**Output:**

```
[1] "--- Arithmetic Operations ---"
[1] "1. Addition (a + b): 13"
[1] "2. Subtraction (a - b): 7"
[1] "3. Multiplication (a * b): 30"
[1] "4. Division (a / b): 3.33333333333333"
[1] "5. Exponentiation (a ^ 2): 100"
[1] "   Exponentiation (a ** 3): 1000"
[1] "6. Modulus (a %% b): 1"
[1] "7. Integer Division (a %/% b): 3"
[1] "8. Vector Addition (element-wise): 5, 7, 9"
```

---

#### **2. Relational Operators (Comparison Operators)**

Relational operators are used to compare two values. They always return a logical (TRUE/FALSE) result.

| Operator | Description                  | Example      |
| :------- | :--------------------------- | :----------- |
| `==`     | Equal to                     | `x == y`     |
| `!=`     | Not equal to                 | `x != y`     |
| `>`      | Greater than                 | `x > y`      |
| `<`      | Less than                    | `x < y`      |
| `>=`     | Greater than or equal to     | `x >= y`     |
| `<=`     | Less than or equal to        | `x <= y`     |

**Code Snippets:**

```r
# Relational Operators

x <- 15
y <- 7
z <- 15

print("--- Relational Operations ---")

# Equal to
result_eq <- (x == y)
print(paste("1. Is x equal to y (x == y)?", result_eq))
result_eq_z <- (x == z)
print(paste("   Is x equal to z (x == z)?", result_eq_z))

# Not equal to
result_neq <- (x != y)
print(paste("2. Is x not equal to y (x != y)?", result_neq))

# Greater than
result_gt <- (x > y)
print(paste("3. Is x greater than y (x > y)?", result_gt))

# Less than
result_lt <- (x < y)
print(paste("4. Is x less than y (x < y)?", result_lt))

# Greater than or equal to
result_gte <- (x >= y)
print(paste("5. Is x greater than or equal to y (x >= y)?", result_gte))
result_gte_z <- (x >= z)
print(paste("   Is x greater than or equal to z (x >= z)?", result_gte_z))

# Less than or equal to
result_lte <- (x <= y)
print(paste("6. Is x less than or equal to y (x <= y)?", result_lte))
result_lte_z <- (x <= z)
print(paste("   Is x less than or equal to z (x <= z)?", result_lte_z))

# Relational operators also work with vectors (element-wise)
scores <- c(80, 95, 70, 88)
pass_threshold <- 80
passed_students <- scores >= pass_threshold
print(paste("7. Scores meeting pass threshold (>=80):", paste(passed_students, collapse = ", ")))
```

**Output:**

```
[1] "--- Relational Operations ---"
[1] "1. Is x equal to y (x == y)? FALSE"
[1] "   Is x equal to z (x == z)? TRUE"
[1] "2. Is x not equal to y (x != y)? TRUE"
[1] "3. Is x greater than y (x > y)? TRUE"
[1] "4. Is x less than y (x < y)? FALSE"
[1] "5. Is x greater than or equal to y (x >= y)? TRUE"
[1] "   Is x greater than or equal to z (x >= z)? TRUE"
[1] "6. Is x less than or equal to y (x <= y)? FALSE"
[1] "   Is x less than or equal to z (x <= z)? TRUE"
[1] "7. Scores meeting pass threshold (>=80): TRUE, TRUE, FALSE, TRUE"
```

---

#### **3. Logical Operators**

Logical operators combine logical (TRUE/FALSE) values and return a logical result.

| Operator | Description                                   | Example            |
| :------- | :-------------------------------------------- | :----------------- |
| `&`      | Element-wise Logical AND                     | `TRUE & FALSE`     |
| `&&`     | Logical AND (evaluates only the first element, short-circuiting) | `TRUE && FALSE`    |
| `\|`     | Element-wise Logical OR                      | `TRUE \| FALSE`    |
| `\|\|`   | Logical OR (evaluates only the first element, short-circuiting) | `TRUE \|\| FALSE`  |
| `!`      | Logical NOT (Negation)                       | `!TRUE`            |

**Note on `&`/`|` vs. `&&`/`||`:**
* `&` and `|` perform **element-wise** comparisons on vectors.
* `&&` and `||` perform comparisons on **single logical values** (typically the first element of vectors) and are primarily used in `if` conditions, where short-circuiting behavior can be beneficial (i.e., if the first part of an `&&` expression is `FALSE`, the second part is not evaluated).

**Code Snippets:**

```r
# Logical Operators

val1 <- TRUE
val2 <- FALSE
val3 <- TRUE

print("--- Logical Operations ---")

# Element-wise AND (&)
result_and_elem <- val1 & val2
print(paste("1. Element-wise AND (TRUE & FALSE):", result_and_elem))

# Element-wise OR (|)
result_or_elem <- val1 | val2
print(paste("2. Element-wise OR (TRUE | FALSE):", result_or_elem))

# Logical NOT (!)
result_not <- !val1
print(paste("3. Logical NOT (!TRUE):", result_not))

# Using with vectors (element-wise)
vec_logic1 <- c(TRUE, FALSE, TRUE)
vec_logic2 <- c(FALSE, FALSE, TRUE)
vec_and <- vec_logic1 & vec_logic2
print(paste("4. Vector Element-wise AND:", paste(vec_and, collapse = ", ")))
vec_or <- vec_logic1 | vec_logic2
print(paste("5. Vector Element-wise OR:", paste(vec_or, collapse = ", ")))

# Short-circuiting AND (&&) - typically used in if conditions
# (FALSE && evaluates_this_too) - The second part isn't evaluated if the first is FALSE
print(paste("6. Short-circuit AND (TRUE && FALSE):", val1 && val2))
print(paste("   Short-circuit AND (FALSE && TRUE):", val2 && val1))

# Short-circuiting OR (||) - typically used in if conditions
# (TRUE || doesn't_evaluate_this_too) - The second part isn't evaluated if the first is TRUE
print(paste("7. Short-circuit OR (TRUE || FALSE):", val1 || val2))
print(paste("   Short-circuit OR (FALSE || TRUE):", val2 || val1))

# Example of practical use: Filtering a data frame
# (Will be covered in detail in Data Cleaning and Preparation, but good to see here)
data_df <- data.frame(
    Age = c(25, 30, 22, 35),
    IsStudent = c(TRUE, FALSE, TRUE, FALSE)
)
# Select rows where Age > 25 AND IsStudent is TRUE
filtered_data <- data_df[data_df$Age > 25 & data_df$IsStudent, ]
print("8. Filtered Data Frame (Age > 25 AND IsStudent):")
print(filtered_data)
```

**Output:**

```
[1] "--- Logical Operations ---"
[1] "1. Element-wise AND (TRUE & FALSE): FALSE"
[1] "2. Element-wise OR (TRUE | FALSE): TRUE"
[1] "3. Logical NOT (!TRUE): FALSE"
[1] "4. Vector Element-wise AND: FALSE, FALSE, TRUE"
[1] "5. Vector Element-wise OR: TRUE, FALSE, TRUE"
[1] "6. Short-circuit AND (TRUE && FALSE): FALSE"
[1] "   Short-circuit AND (FALSE && TRUE): FALSE"
[1] "7. Short-circuit OR (TRUE || FALSE): TRUE"
[1] "   Short-circuit OR (FALSE || TRUE): TRUE"
[1] "8. Filtered Data Frame (Age > 25 AND IsStudent):"
[1] Age IsStudent
<0 rows> (or if data changes, only rows matching criteria)
```
*(Self-correction: The example for filtered_data with the provided `data_df` would result in 0 rows. Let's make the data frame more illustrative)*
```r
# Corrected example for practical use: Filtering a data frame
data_df_corrected <- data.frame(
    Age = c(25, 30, 22, 35, 28),
    IsStudent = c(TRUE, FALSE, TRUE, FALSE, TRUE)
)
# Select rows where Age > 25 AND IsStudent is TRUE
filtered_data_corrected <- data_df_corrected[data_df_corrected$Age > 25 & data_df_corrected$IsStudent, ]
print("8. Filtered Data Frame (Age > 25 AND IsStudent):")
print(filtered_data_corrected)
```
**Corrected Output for `filtered_data_corrected`:**
```
[1] "8. Filtered Data Frame (Age > 25 AND IsStudent):"
  Age IsStudent
5  28      TRUE
```

---

#### **4. Assignment Operators**

Assignment operators are used to assign values to variables.

| Operator | Description                                     | Example      |
| :------- | :---------------------------------------------- | :----------- |
| `<-`     | Leftward Assignment (Most common and recommended in R) | `x <- 10`    |
| `=`      | Leftward Assignment (also used for function arguments) | `x = 10`     |
| `->`     | Rightward Assignment                            | `10 -> x`    |

**Code Snippets:**

```r
# Assignment Operators

print("--- Assignment Operations ---")

# Leftward assignment (most common)
my_variable_1 <- 50
print(paste("1. Leftward assignment (<-):", my_variable_1))

# Leftward assignment (=) - often used for function arguments as well
my_variable_2 = 75
print(paste("2. Leftward assignment (=):", my_variable_2))

# Rightward assignment (less common, can make code harder to read)
100 -> my_variable_3
print(paste("3. Rightward assignment (->):", my_variable_3))
```

**Output:**

```
[1] "--- Assignment Operations ---"
[1] "1. Leftward assignment (<-): 50"
[1] "2. Leftward assignment (=): 75"
[1] "3. Rightward assignment (->): 100"
```

**Best Practice:** While `=` and `->` also work, `<-` is the idiomatic (most common and preferred) assignment operator in R for assigning values to variables. It enhances readability and avoids confusion with equality checks (`==`) or function argument assignments.

---

#### **5. Miscellaneous Operators**

These operators perform specific tasks that don't fit neatly into the other categories.

| Operator | Description                                   | Example            |
| :------- | :-------------------------------------------- | :----------------- |
| `:`      | Sequence operator (generates a sequence of numbers) | `1:5`              |
| `%in%`   | Matching operator (checks for element existence in a vector) | `3 %in% c(1, 2, 3)` |
| `%*%`    | Matrix multiplication                         | `matrix_A %*% matrix_B` |
| `$`      | List/Data Frame component selector (already covered) | `df$column_name` |
| `[ ]`    | Subsetting operator (already covered)           | `vector[1]`, `matrix[1,2]`, `df[1,"col"]` |
| `[[ ]]`  | List element extractor (already covered)        | `my_list[[1]]`     |

**Code Snippets:**

```r
# Miscellaneous Operators

print("--- Miscellaneous Operations ---")

# 1. Sequence operator (:)
sequence_vec <- 1:10
print(paste("1. Sequence (1:10):", paste(sequence_vec, collapse = ", ")))
desc_sequence_vec <- 10:1
print(paste("   Descending Sequence (10:1):", paste(desc_sequence_vec, collapse = ", ")))

# 2. Matching operator (%in%)
fruits <- c("apple", "banana", "orange", "grape")
check_apple <- "apple" %in% fruits
print(paste("2. Is 'apple' in fruits (%in%):", check_apple))
check_pear <- "pear" %in% fruits
print(paste("   Is 'pear' in fruits (%in%):", check_pear))

# Can also use with vectors on both sides (element-wise check if each element on left is in right)
items_to_check <- c("banana", "kiwi", "grape", "mango")
results_in_fruits <- items_to_check %in% fruits
print(paste("   Which items are in fruits:", paste(results_in_fruits, collapse = ", ")))

# 3. Matrix Multiplication (%*%) - requires matrices as operands
mat_A <- matrix(c(1, 2, 3, 4), nrow = 2, byrow = TRUE) # 2x2 matrix
mat_B <- matrix(c(5, 6, 7, 8), nrow = 2, byrow = TRUE) # 2x2 matrix
print("3. Matrix A:")
print(mat_A)
print("   Matrix B:")
print(mat_B)
result_matrix_mult <- mat_A %*% mat_B
print("   Result of Matrix Multiplication (A %*% B):")
print(result_matrix_mult)

# Note: '$', '[]', '[[]]' were covered in Data Types and Structures lessons.
# They are also operators used for accessing parts of data structures.
```

**Output:**

```
[1] "--- Miscellaneous Operations ---"
[1] "1. Sequence (1:10): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
[1] "   Descending Sequence (10:1): 10, 9, 8, 7, 6, 5, 4, 3, 2, 1"
[1] "2. Is 'apple' in fruits (%in%): TRUE"
[1] "   Is 'pear' in fruits (%in%): FALSE"
[1] "   Which items are in fruits: TRUE, FALSE, TRUE, FALSE"
[1] "3. Matrix A:"
     [,1] [,2]
[1,]    1    2
[2,]    3    4
[1] "   Matrix B:"
     [,1] [,2]
[1,]    5    6
[2,]    7    8
[1] "   Result of Matrix Multiplication (A %*% B):"
     [,1] [,2]
[1,]   19   22
[2,]   43   50
```

---

This lesson provided a detailed overview of the various types of operators in R, including their syntax, behavior, and common use cases. Understanding these operators is foundational for performing calculations, making logical decisions, and effectively manipulating data in R.

**Next, we will proceed to Lesson 2: Conditional Statements.**
```