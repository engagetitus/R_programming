# Lesson 2: Basic Operations

* R as a calculator: Basic arithmetic operations (+, -, *, /, ^, %%, %/%).
* Understanding operator precedence.
* Introduction to comments (`#`).
* Creating and running your first R scripts.

## **Phase 1: Introduction to R and Fundamentals**

### **Module 1.1: Getting Started with R**

---

### **Lesson 2: Basic Operations**

This lesson focuses on the fundamental operators in R, which are essential for performing calculations and making logical comparisons. We'll cover arithmetic, relational, and logical operators, along with R's approach to vectorized operations.

---

#### **Arithmetic Operators**

Arithmetic operators are used to perform basic mathematical calculations. R follows standard order of operations (PEMDAS/BODMAS).

| Operator | Description      | Example       |
| :------- | :--------------- | :------------ |
| `+`      | Addition         | `5 + 3`       |
| `-`      | Subtraction      | `10 - 2`      |
| `*`      | Multiplication   | `4 * 7`       |
| `/`      | Division         | `15 / 3`      |
| `^`      | Exponentiation   | `2^3` (2 to the power of 3) |
| `**`     | Exponentiation   | `2**3` (Alternative for `^`) |
| `%%`     | Modulus          | `10 %% 3` (Remainder of 10 divided by 3) |
| `%/%`    | Integer Division | `10 %/% 3` (Quotient of 10 divided by 3, discards remainder) |

**Code Snippets:**

```r
# Addition
result_add <- 15 + 7
print(result_add)

# Subtraction
result_sub <- 25 - 12
print(result_sub)

# Multiplication
result_mult <- 6 * 8
print(result_mult)

# Division
result_div <- 100 / 20
print(result_div)

# Exponentiation
result_exp1 <- 3^4 # 3 to the power of 4 (3 * 3 * 3 * 3)
print(result_exp1)

result_exp2 <- 2**5 # 2 to the power of 5 (2 * 2 * 2 * 2 * 2)
print(result_exp2)

# Modulus (remainder)
result_mod <- 17 %% 5
print(result_mod)

# Integer Division (quotient)
result_int_div <- 17 %/% 5
print(result_int_div)

# Operator Precedence
# Multiplication/Division before Addition/Subtraction
# Exponentiation is highest precedence
complex_calc <- 5 + 3 * 2^2 / 2
print(complex_calc) # 5 + 3 * 4 / 2 = 5 + 12 / 2 = 5 + 6 = 11

# Using parentheses to override precedence
complex_calc_paren <- (5 + 3) * 2^2 / 2
print(complex_calc_paren) # 8 * 4 / 2 = 32 / 2 = 16
```

**Output:**

```bash
[1] 22
[1] 13
[1] 48
[1] 5
[1] 81
[1] 32
[1] 2
[1] 3
[1] 11
[1] 16
```

---

#### **Relational Operators**

Relational operators (also known as comparison operators) are used to compare two values. They always return a **logical** value: `TRUE` or `FALSE`.

| Operator | Description             | Example       |
| :------- | :---------------------- | :------------ |
| `==`     | Equal to                | `5 == 5`      |
| `!=`     | Not equal to            | `10 != 5`     |
| `<`      | Less than               | `7 < 10`      |
| `>`      | Greater than            | `12 > 8`      |
| `<=`     | Less than or equal to   | `5 <= 5`      |
| `>=`     | Greater than or equal to | `10 >= 8`     |

**Code Snippets:**

```r
# Equal to
is_equal <- (10 == 10)
print(is_equal)

is_not_equal_val <- (10 == 5)
print(is_not_equal_val)

# Not equal to
is_not_equal <- (10 != 5)
print(is_not_equal)

is_equal_val <- (10 != 10)
print(is_equal_val)

# Less than
is_less <- (7 < 10)
print(is_less)

# Greater than
is_greater <- (15 > 8)
print(is_greater)

# Less than or equal to
is_le <- (5 <= 5)
print(is_le)

is_le_false <- (6 <= 5)
print(is_le_false)

# Greater than or equal to
is_ge <- (12 >= 10)
print(is_ge)

is_ge_false <- (9 >= 10)
print(is_ge_false)
```

**Output:**

```
[1] TRUE
[1] FALSE
[1] TRUE
[1] FALSE
[1] TRUE
[1] TRUE
[1] TRUE
[1] FALSE
[1] TRUE
[1] FALSE
```

**Key Point:** Be careful not to confuse the assignment operator (`=`) with the equality operator (`==`). Using `=` for comparison is a common error in R that can lead to unexpected behavior.

---

#### **Logical Operators**

Logical operators are used to combine logical conditions (expressions that evaluate to `TRUE` or `FALSE`).

| Operator | Description         | Example          |
| :------- | :------------------ | :--------------- |
| `&`      | Element-wise AND    | `c(TRUE, FALSE) & c(TRUE, TRUE)` |
| `|`      | Element-wise OR     | `c(TRUE, FALSE) | c(FALSE, TRUE)` |
| `!`      | Logical NOT         | `!TRUE`          |
| `&&`     | Logical AND (scalar) | `TRUE && FALSE`  |
| `||`     | Logical OR (scalar) | `TRUE || FALSE`  |

**Difference between `&`/`|` and `&&`/`||`:**

* `&` (AND) and `|` (OR) perform **element-wise** comparisons. They operate on vectors of logical values.
* `&&` (AND) and `||` (OR) perform **scalar** comparisons. They only evaluate the first element of each vector and are typically used in `if` conditions where you need a single `TRUE` or `FALSE` result.

**Code Snippets:**

```r
# Element-wise AND (`&`)
result_and_element_wise <- c(TRUE, TRUE, FALSE, FALSE) & c(TRUE, FALSE, TRUE, FALSE)
print(result_and_element_wise)

# Element-wise OR (`|`)
result_or_element_wise <- c(TRUE, TRUE, FALSE, FALSE) | c(TRUE, FALSE, TRUE, FALSE)
print(result_or_element_wise)

# Logical NOT (`!`)
result_not <- !TRUE
print(result_not)
result_not_false <- !FALSE
print(result_not_false)

# Scalar AND (`&&`) - often used in if statements
scalar_and_true <- (5 > 3) && (10 < 20)
print(scalar_and_true)

scalar_and_false <- (5 > 3) && (10 > 20)
print(scalar_and_false)

# Scalar OR (`||`) - often used in if statements
scalar_or_true <- (5 > 10) || (10 < 20)
print(scalar_or_true)

scalar_or_false <- (5 > 10) || (10 > 20)
print(scalar_or_false)

# Example with numeric values (R coerces to logical)
numeric_and <- (1 & 0) # 1 is TRUE, 0 is FALSE
print(numeric_and)

numeric_or <- (1 | 0)
print(numeric_or)
```

**Output:**

```
[1]  TRUE FALSE FALSE FALSE
[1]  TRUE  TRUE  TRUE FALSE
[1] FALSE
[1] TRUE
[1] TRUE
[1] FALSE
[1] TRUE
[1] FALSE
[1] FALSE
[1] TRUE
```

**Key Points:**

* `TRUE` and `FALSE` are case-sensitive.
* R treats `1` as `TRUE` and `0` as `FALSE` in logical contexts, but it's best practice to use `TRUE`/`FALSE` explicitly.

---

#### **Vectorized Operations (Introduction)**

One of R's most powerful features is its ability to perform operations on entire vectors or data structures without explicit loops. This is called **vectorization**, and it often leads to cleaner, more concise, and significantly faster code.

When you apply an arithmetic or relational operator to a vector, R applies the operation element-wise. If you operate on two vectors, R performs the operation on corresponding elements. If vectors are of different lengths, R will "recycle" the shorter vector's elements.

**Code Snippets:**

```r
# Scalar operation on a vector
numbers <- c(10, 20, 30, 40, 50)
doubled_numbers <- numbers * 2
print(doubled_numbers)

# Element-wise operation between two vectors of the same length
vec1 <- c(1, 2, 3)
vec2 <- c(4, 5, 6)
sum_vectors <- vec1 + vec2
print(sum_vectors)

# Element-wise operation between two vectors of different lengths (recycling)
# The shorter vector (c(10, 100)) is recycled to match the length of the longer vector.
# This means it becomes c(10, 100, 10, 100, 10)
long_vec <- c(1, 2, 3, 4, 5)
short_vec <- c(10, 100)
recycled_sum <- long_vec + short_vec
print(recycled_sum)

# Relational operator on a vector
scores <- c(85, 92, 78, 65, 95)
passed <- scores >= 70
print(passed)

# Logical operation on vectors
is_morning <- c(TRUE, FALSE, TRUE)
is_weekday <- c(TRUE, TRUE, FALSE)
go_to_work <- is_morning & is_weekday
print(go_to_work)
```

**Output:**

```
[1]  20  40  60  80 100
[1] 5 7 9
[1]  11 102  13 104  15
[1]  TRUE  TRUE  TRUE FALSE  TRUE
[1]  TRUE FALSE FALSE
```

**Key Point:** While vector recycling can be convenient, be aware that it can also lead to subtle bugs if you're not expecting it, especially if the longer vector's length is not a multiple of the shorter vector's length (R will issue a warning in such cases). Always aim for vectors of compatible lengths or explicitly handle recycling if intended.
