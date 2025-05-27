# Lesson 1: Atomic Vectors

* Introduction to vectors: The fundamental data structure in R.
* Numeric, Integer, Character, Logical, Complex data types.
* Creating vectors using `c()`.
* Vector indexing and slicing.
* Vectorized operations.

## **Phase 1: Introduction to R and Fundamentals**

### **Module 1.2: Data Types and Structures**

---

### **Lesson 1: Atomic Vectors**

This lesson introduces you to atomic vectors, the most fundamental data structure in R. Understanding atomic vectors is key because nearly all data in R is built upon them. You'll learn about the different atomic data types, how to create vectors, and how to access their elements.

---

---

#### **Introduction to Vectors: The Fundamental Data Structure**

In R, a **vector** is a sequence of data elements of the *same basic type*. It's the simplest and most common data structure. Unlike some other languages where a single value might be treated as a scalar, in R, even a single number or character is considered a vector of length one.

R is "vectorized" by nature, meaning operations are often applied to entire vectors rather than individual elements, leading to highly efficient code.

---

#### **Atomic Data Types**

R supports six **atomic data types** (also called "modes"). Atomic vectors can only contain elements of one of these types.

1. **Logical:** Boolean values (`TRUE`, `FALSE`).
2. **Integer:** Whole numbers (`L` suffix, e.g., `5L`).
3. **Numeric (or Double):** Real numbers, including decimals. This is the default numeric type.
4. **Character:** Text strings.
5. **Complex:** Complex numbers (with an imaginary component).
6. **Raw:** Raw bytes (rarely used in typical data analysis).

**Detailed Explanation and Examples:**

* **Logical:** Represents `TRUE` or `FALSE` values. They are internally stored as `1` for `TRUE` and `0` for `FALSE`.

    **Code Snippets:**

    ```r
    # Creating logical vectors
    is_sunny <- TRUE
    is_raining <- FALSE
    are_equal <- (10 == 10)
    can_vote <- (18 > 20)

    print(is_sunny)
    print(is_raining)
    print(are_equal)
    print(can_vote)

    # Check class and type
    print(class(is_sunny))
    print(typeof(is_sunny))
    ```

    **Output:**

    ```bash
    [1] TRUE
    [1] FALSE
    [1] TRUE
    [1] FALSE
    [1] "logical"
    [1] "logical"
    ```

* **Integer:** Represents whole numbers. To explicitly create an integer, append an `L` suffix to the number. Without `L`, R defaults to `numeric` (double).

    **Code Snippets:**

    ```r
    # Creating integer vectors
    num_students <- 30L
    year <- 2024L

    print(num_students)
    print(year)

    # Check class and type
    print(class(num_students))
    print(typeof(num_students))
    ```

    **Output:**

    ```bash
    [1] 30
    [1] 2024
    [1] "integer"
    [1] "integer"
    ```

* **Numeric (or Double):** This is the default numeric type in R for real numbers, including those with decimal points. Even numbers without a decimal point are typically stored as numeric unless explicitly declared as integer.

    **Code Snippets:**

    ```r
    # Creating numeric vectors
    temperature <- 23.5
    price <- 99.99
    integer_as_numeric <- 5 # No L suffix, so it's numeric
    very_large_number <- 1.23e+05 # Scientific notation

    print(temperature)
    print(price)
    print(integer_as_numeric)
    print(very_large_number)

    # Check class and type
    print(class(temperature))
    print(typeof(temperature))
    print(class(integer_as_numeric))
    print(typeof(integer_as_numeric))
    ```

    **Output:**

    ```bash
    [1] 23.5
    [1] 99.99
    [1] 5
    [1] 123000
    [1] "numeric"
    [1] "double"
    [1] "numeric"
    [1] "double"
    ```

* **Character:** Represents text strings. They are enclosed in single (`'`) or double (`"`) quotes.

    **Code Snippets:**

    ```r
    # Creating character vectors
    city <- "Nairobi"
    greeting <- 'Hello World!'
    sentence <- "R is a powerful tool for data analysis."

    print(city)
    print(greeting)
    print(sentence)

    # Check class and type
    print(class(city))
    print(typeof(city))
    ```

    **Output:**

    ```bash
    [1] "Nairobi"
    [1] "Hello World!"
    [1] "R is a powerful tool for data analysis."
    [1] "character"
    [1] "character"
    ```

* **Complex:** Represents complex numbers, which have a real and an imaginary component (denoted by `i`).

    **Code Snippets:**

    ```r
    # Creating complex vectors
    complex_num <- 2 + 3i
    another_complex <- 1i

    print(complex_num)
    print(another_complex)

    # Check class and type
    print(class(complex_num))
    print(typeof(complex_num))
    ```

    **Output:**

    ```bash
    [1] 2+3i
    [1] 0+1i
    [1] "complex"
    [1] "complex"
    ```

* **Raw:** Used to store raw bytes. Rarely encountered in typical data analysis unless dealing with low-level data manipulation.

    **Code Snippets:**

    ```r
    # Creating raw vector
    raw_data <- charToRaw("Hello")
    print(raw_data)

    # Check class and type
    print(class(raw_data))
    print(typeof(raw_data))
    ```

    **Output:**

    ```bash
    [1] 48 65 6c 6c 6f
    [1] "raw"
    [1] "raw"
    ```

---

#### **Creating Vectors using `c()`**

The most common way to create a vector in R is using the `c()` function, which stands for "combine" or "concatenate". You pass the elements you want in your vector as arguments to `c()`.

**Syntax:**

```r
vector_name <- c(element1, element2, element3, ...)
```

**Parameters:**

* `element1, element2, ...`: The individual values (of the same atomic type) that you want to combine into a vector.

* `vector_name`: The variable name you choose to store your newly created vector.

```r
print("--- Creating Vectors using c() ---")

# 1. Creating a numeric vector
numeric_vector <- c(10, 20, 30, 40, 50)
print("Numeric Vector:")
print(numeric_vector)
print(paste("Class of numeric_vector:", class(numeric_vector)))

# 2. Creating a character vector
character_vector <- c("apple", "banana", "cherry")
print("Character Vector:")
print(character_vector)
print(paste("Class of character_vector:", class(character_vector)))

# 3. Creating a logical vector
logical_vector <- c(TRUE, FALSE, TRUE, TRUE)
print("Logical Vector:")
print(logical_vector)
print(paste("Class of logical_vector:", class(logical_vector)))

# 4. Creating a vector with mixed data types (R will coerce to a common type)
# In this case, numbers and logical values will be coerced to character type.
mixed_vector <- c(1, "hello", TRUE, 3.14)
print("Mixed Vector (coerced):")
print(mixed_vector)
print(paste("Class of mixed_vector (after coercion):", class(mixed_vector)))

# 5. Creating an empty vector (useful for pre-allocating or building vectors)
empty_numeric_vector <- numeric() # Creates an empty numeric vector
print("Empty Numeric Vector:")
print(empty_numeric_vector)
print(paste("Length of empty_numeric_vector:", length(empty_numeric_vector)))

empty_character_vector <- character(0) # Another way to create an empty vector
print("Empty Character Vector:")
print(empty_character_vector)
print(paste("Length of empty_character_vector:", length(empty_character_vector)))

# You can also combine existing vectors using c()
vector_a <- c(1, 2)
vector_b <- c(3, 4)
combined_vector <- c(vector_a, vector_b, 5)
print("Combined Vector (from existing vectors):")
print(combined_vector)
```

**Expected Output**

```bash
[1] "--- Creating Vectors using c() ---"
[1] "Numeric Vector:"
[1] 10 20 30 40 50
[1] "Class of numeric_vector: numeric"
[1] "Character Vector:"
[1] "apple"  "banana" "cherry"
[1] "Class of character_vector: character"
[1] "Logical Vector:"
[1]  TRUE FALSE  TRUE  TRUE
[1] "Class of logical_vector: logical"
[1] "Mixed Vector (coerced):"
[1] "1"     "hello" "TRUE"  "3.14"
[1] "Class of mixed_vector (after coercion): character"
[1] "Empty Numeric Vector:"
numeric(0)
[1] "Length of empty_numeric_vector: 0"
[1] "Empty Character Vector:"
character(0)
[1] "Length of empty_character_vector: 0"
[1] "Combined Vector (from existing vectors):"
[1] 1 2 3 4 5
```

**Return Value:**

* An atomic vector containing the combined elements.

**Code Snippets:**

```r
# Create a numeric vector
ages <- c(25, 30, 22, 35, 28)
print(ages)
print(class(ages))

# Create a character vector
names <- c("Alice", "Bob", "Charlie", "David")
print(names)
print(class(names))

# Create a logical vector
status <- c(TRUE, FALSE, TRUE, TRUE, FALSE)
print(status)
print(class(status))

# Create an integer vector (explicitly)
id_numbers <- c(101L, 102L, 103L)
print(id_numbers)
print(class(id_numbers))

# Creating a vector of mixed types - Coercion
# R will automatically coerce (convert) all elements to the most flexible data type
# The hierarchy of flexibility: logical -> integer -> numeric -> character
mixed_vector_1 <- c(1, "apple", TRUE) # Numeric and logical will become character
print(mixed_vector_1)
print(class(mixed_vector_1))

mixed_vector_2 <- c(10L, 20.5, FALSE) # Integer and logical will become numeric
print(mixed_vector_2)
print(class(mixed_vector_2))
```

**Output:**

```
[1] 25 30 22 35 28
[1] "numeric"
[1] "Alice"   "Bob"     "Charlie" "David"
[1] "character"
[1]  TRUE FALSE  TRUE  TRUE FALSE
[1] "logical"
[1] 101 102 103
[1] "integer"
[1] "1"     "apple" "TRUE"
[1] "character"
[1] 10.0  20.5   0.0
[1] "numeric"
```

**Key Point: Type Coercion:**
If you try to combine different atomic data types within a single vector using `c()`, R will automatically "coerce" (convert) all elements to the most general or flexible data type among them. The general hierarchy of flexibility is: `logical` < `integer` < `numeric` (double) < `character` < `complex` < `raw`. This means if you have a character and a number, everything becomes a character. If you have a numeric and an integer, everything becomes numeric. This is important to remember to avoid unexpected data type conversions.

---

#### **Vector Indexing and Slicing**

Accessing specific elements or subsets of elements within a vector is called indexing or slicing. R uses square brackets `[]` for this purpose.

**Methods of Indexing:**

1. **Positive Integers:** Select elements by their position (1-based indexing).
2. **Negative Integers:** Select all elements *except* those at the specified positions.
3. **Logical Vector:** Select elements where the corresponding logical value is `TRUE`.
4. **Character Vector:** Select elements by their names (if the vector has names).

**Code Snippets:**

```r
my_vector <- c("apple", "banana", "cherry", "date", "elderberry", "fig")
print(my_vector)

# 1. Indexing by Positive Integers
# Access the first element
print(my_vector[1])

# Access the third element
print(my_vector[3])

# Access multiple specific elements
print(my_vector[c(2, 5)])

# Access a range of elements
print(my_vector[1:3]) # Elements from 1 to 3

# Duplicated indices
print(my_vector[c(1, 1, 3)])

# 2. Indexing by Negative Integers
# Exclude the second element
print(my_vector[-2])

# Exclude the first and fourth elements
print(my_vector[c(-1, -4)])

# Note: Cannot mix positive and negative indexing in the same vector
# print(my_vector[c(1, -3)]) # This will give an error

# 3. Indexing by Logical Vector
# Create a logical vector with the same length as my_vector
# TRUE for elements to keep, FALSE for elements to drop
is_long_fruit <- c(FALSE, FALSE, TRUE, FALSE, TRUE, FALSE)
print(my_vector[is_long_fruit])

# More common: using a condition to create the logical vector
numbers <- c(10, 5, 20, 15, 30, 8)
print(numbers[numbers > 15]) # Select numbers greater than 15
print(numbers[numbers %% 2 == 0]) # Select even numbers

# 4. Indexing by Character Vector (Named Vectors)
# First, create a named vector
student_scores <- c(Alice = 95, Bob = 88, Charlie = 72, David = 91)
print(student_scores)

# Access score by name
print(student_scores["Alice"])

# Access multiple scores by name
print(student_scores[c("Bob", "David")])
```

**Output:**

```
[1] "apple"      "banana"     "cherry"     "date"       "elderberry" "fig"
[1] "apple"
[1] "cherry"
[1] "banana"     "elderberry"
[1] "apple"  "banana" "cherry"
[1] "apple"  "apple"  "cherry"
[1] "apple"      "cherry"     "date"       "elderberry" "fig"
[1] "banana"     "cherry"     "elderberry" "fig"
[1] "cherry"     "elderberry"
[1] 20 30
[1] 10 20 30  8
    Alice      Bob  Charlie    David
       95       88       72       91
    Alice
       95
  Bob David
   88    91
```

---

#### **Vectorized Operations Deep Dive**

We briefly introduced vectorized operations in Lesson 2. Now, let's look at how they apply to vectors more explicitly. R's vectorized nature means that many functions and operators automatically apply to each element of a vector without you needing to write a loop.

**Code Snippets:**

```r
# Element-wise addition
grades_midterm <- c(75, 82, 90, 68, 95)
grades_final <- c(80, 85, 92, 70, 98)
total_grades <- grades_midterm + grades_final
print(total_grades)

# Scalar multiplication on a vector
prices <- c(10.50, 25.00, 5.75)
discounted_prices <- prices * 0.90 # 10% discount
print(discounted_prices)

# Applying a function to each element
sqrt_values <- sqrt(c(4, 9, 16, 25))
print(sqrt_values)

# Logical comparison on a vector
temperatures <- c(20, 25, 18, 30, 22)
above_20 <- temperatures > 20
print(above_20)

# Recycling rule in action (watch the warning for non-multiples)
vector_long <- c(1, 2, 3, 4, 5, 6, 7)
vector_short <- c(10, 20)
sum_recycled <- vector_long + vector_short
print(sum_recycled) # R will warn if lengths are not multiples
```

**Output:**

```
[1] 155 167 182 138 193
[1]  9.45 22.50  5.175
[1] 2 3 4 5
[1] FALSE  TRUE FALSE  TRUE  TRUE
[1] 11 22 13 24 15 26 17
Warning message:
In vector_long + vector_short :
  longer object length is not a multiple of shorter object length
```

**Key Point:** Vectorized operations are fundamental to efficient R programming. They are generally much faster than explicit loops for element-wise operations. Understand the recycling rule, especially the potential for warnings when vector lengths are not direct multiples.

---

This lesson provided a deep dive into atomic vectors, their types, creation, and how to access their elements using various indexing methods. You also gained a better understanding of how vectorized operations work in R. These concepts are foundational for working with more complex data structures.

**Next, we will explore Lesson 2: Matrices and Arrays.**
