# Lesson 4: Data Frames and Factors

* Data Frames: The most common data structure for tabular data.
* Creating data frames (`data.frame()`).
* Accessing columns by name and position.
* Basic data frame operations (`str()`, `summary()`, `dim()`, `names()`).
* Introduction to Factors: Handling categorical data.
* Ordering and re-leveling factors.

Data frames are arguably the most important and frequently used data structure in R for data analysis. They combine the best aspects of matrices and lists, allowing you to store tabular data where columns can have different data types.

---

## **Phase 1: Introduction to R and Fundamentals**

### **Module 1.2: Data Types and Structures**

---

### **Lesson 4: Data Frames**

This lesson focuses on **data frames**, the most widely used data structure for tabular data in R. Data frames are unique because they combine the column-based organization of matrices with the heterogeneity of lists, making them ideal for representing datasets where each column can store a different type of information.

---

#### **Understanding Data Frames: The Workhorse of R Data Analysis**

A **data frame** is a list of equal-length vectors. It is the R implementation of a table or spreadsheet, where:

* Each column is a **vector** (a variable) and can be of a different atomic data type (numeric, character, logical, etc.).
* Each row represents an **observation** or a record.
* All columns must have the **same number of rows** (length).

Think of a data frame as a collection of variables (columns) with each variable containing the same number of observations (rows). This structure is perfectly suited for most real-world datasets, where you typically have different types of measurements or attributes for each individual or entity.

**Key Characteristics of Data Frames:**

* **Two-Dimensional:** Organized into rows and columns, similar to a spreadsheet.
* **Heterogeneous Columns:** Each column can be of a different data type.
* **Homogeneous within Columns:** All elements within a single column must be of the same data type (as a vector).
* **Equal Length Columns:** All columns must have the same number of rows.
* **Named Columns and Rows:** Columns typically have names (variable names), and rows can optionally have names.

---

#### **Creating Data Frames**

The primary function to create a data frame in R is `data.frame()`. You typically pass vectors as arguments, where each vector becomes a column in the data frame.

**Syntax:**

```R
data.frame(col1_vector, col2_vector, ..., colN_vector, stringsAsFactors = TRUE/FALSE)
```

**Parameters:**

* `col1_vector, col2_vector, ...`: Vectors of equal length that will form the columns of the data frame. You can name these arguments to give names to your columns.
* `stringsAsFactors`: A logical value (default `TRUE` in older R versions, `FALSE` in newer versions like R 4.0+). If `TRUE`, character vectors are automatically converted into factors. If `FALSE`, they remain as character vectors. **It is generally recommended to set this to `FALSE`** to avoid unintended factor conversions, especially when loading data.

**Return Value:**

* A data frame object.

**Code Snippets:**

```r
# Create a simple data frame
# Each argument becomes a column
my_df <- data.frame(
    ID = c(1, 2, 3, 4),
    Name = c("Alice", "Bob", "Charlie", "David"),
    Age = c(24, 30, 22, 28),
    IsStudent = c(TRUE, FALSE, TRUE, FALSE)
)
print("My First Data Frame:")
print(my_df)
print(class(my_df))

# Create a data frame and specify stringsAsFactors = FALSE
# This ensures Name remains a character vector, not a factor
students_df <- data.frame(
    StudentID = c("S001", "S002", "S003", "S004", "S005"),
    FirstName = c("Emma", "Liam", "Olivia", "Noah", "Ava"),
    Major = c("Math", "Physics", "Chem", "Math", "Biology"),
    GPA = c(3.8, 3.5, 3.9, 3.2, 3.7),
    stringsAsFactors = FALSE # IMPORTANT: Keeps strings as characters
)
print("Students Data Frame:")
print(students_df)
print(class(students_df$FirstName)) # Check type of 'FirstName' column

# Attempt to create a data frame with unequal length vectors (will cause error)
# invalid_df <- data.frame(
#     A = c(1, 2, 3),
#     B = c("x", "y")
# )
# print(invalid_df) # Uncomment to see error
```

**Output:**

```
[1] "My First Data Frame:"
  ID    Name Age IsStudent
1  1   Alice  24      TRUE
2  2     Bob  30     FALSE
3  3 Charlie  22      TRUE
4  4   David  28     FALSE
[1] "data.frame"
[1] "Students Data Frame:"
  StudentID FirstName   Major GPA
1      S001     Emma    Math 3.8
2      S002     Liam Physics 3.5
3      S003   Olivia    Chem 3.9
4      S004     Noah    Math 3.2
5      S005      Ava Biology 3.7
[1] "character"
```

**Key Points:**

* Always ensure vectors passed to `data.frame()` have the same length.
* For new projects, explicitly use `stringsAsFactors = FALSE` to prevent R from converting character vectors to factors by default. Factors are a special type that we'll discuss later.

---

#### **Data Frame Indexing and Slicing**

Accessing data in a data frame is very flexible, combining matrix-like indexing with list-like access for columns.

**Methods of Indexing:**

1. **`[row_index, column_index]`:** Standard matrix-like indexing.
2. **`[[column_index]]` or `[[column_name]]`:** To extract a single column as a vector (list-like).
3. **`$column_name`:** To extract a single named column as a vector (list-like, most common for named columns).
4. **Logical Indexing:** Using conditions to select rows or columns.

**Code Snippets:**

```r
employees_df <- data.frame(
    EmpID = c("E001", "E002", "E003", "E004", "E005"),
    Name = c("John Doe", "Jane Smith", "Peter Jones", "Mary Brown", "Chris Green"),
    Department = c("HR", "IT", "Sales", "HR", "IT"),
    Salary = c(60000, 85000, 70000, 62000, 90000),
    YearsExp = c(5, 10, 7, 6, 12),
    IsActive = c(TRUE, TRUE, FALSE, TRUE, TRUE),
    stringsAsFactors = FALSE
)
print("Original Employees Data Frame:")
print(employees_df)

# 1. Accessing a single element (matrix-like)
print("Name of employee in row 2, column 2:")
print(employees_df[2, 2])
print("Salary of employee E003:")
print(employees_df[3, "Salary"])

# 2. Accessing a specific row (matrix-like)
print("Data for the 3rd employee (row 3):")
print(employees_df[3, ]) # Returns a data frame (unless drop=TRUE for single row/col)

# 3. Accessing a specific column as a vector (list-like using [[ ]])
print("All Names (as a vector):")
print(employees_df[["Name"]])
print(class(employees_df[["Name"]]))

# 4. Accessing a specific column as a vector (list-like using $) - MOST COMMON
print("All Salaries (as a vector):")
print(employees_df$Salary)
print(class(employees_df$Salary))

# 5. Accessing multiple rows and columns (sub-dataframe)
print("Names and Departments for employees 1, 3, 5:")
print(employees_df[c(1, 3, 5), c("Name", "Department")])

# 6. Logical Indexing (selecting rows based on a condition)
print("Employees with Salary > 70000:")
print(employees_df[employees_df$Salary > 70000, ])

print("Employees in 'IT' department who are active:")
print(employees_df[employees_df$Department == "IT" & employees_df$IsActive == TRUE, ])

# Select only specific columns for the filtered rows
print("Names and Salary of employees with > 8 years experience:")
print(employees_df[employees_df$YearsExp > 8, c("Name", "Salary")])

# 7. Modifying elements
employees_df[1, "Salary"] <- 62000 # Update John Doe's salary
employees_df$Department[2] <- "Marketing" # Update Jane Smith's department
print("Data frame after modifications:")
print(employees_df)

# Adding a new column
employees_df$Bonus <- employees_df$Salary * 0.10 # 10% bonus
print("Data frame after adding 'Bonus' column:")
print(employees_df)

# Removing a column (set to NULL)
employees_df$IsActive <- NULL
print("Data frame after removing 'IsActive' column:")
print(employees_df)
```

**Output:**

```
[1] "Original Employees Data Frame:"
  EmpID        Name Department Salary YearsExp IsActive
1  E001    John Doe         HR  60000        5     TRUE
2  E002  Jane Smith         IT  85000       10     TRUE
3  E003 Peter Jones      Sales  70000        7    FALSE
4  E004  Mary Brown         HR  62000        6     TRUE
5  E005 Chris Green         IT  90000       12     TRUE
[1] "Name of employee in row 2, column 2:"
[1] "Jane Smith"
[1] "Salary of employee E003:"
[1] 70000
[1] "Data for the 3rd employee (row 3):"
  EmpID        Name Department Salary YearsExp IsActive
3  E003 Peter Jones      Sales  70000        7    FALSE
[1] "All Names (as a vector):"
[1] "John Doe"    "Jane Smith"  "Peter Jones" "Mary Brown"  "Chris Green"
[1] "character"
[1] "All Salaries (as a vector):"
[1] 60000 85000 70000 62000 90000
[1] "numeric"
[1] "Names and Departments for employees 1, 3, 5:"
        Name Department
1    John Doe         HR
3 Peter Jones      Sales
5 Chris Green         IT
[1] "Employees with Salary > 70000:"
  EmpID        Name Department Salary YearsExp IsActive
2  E002  Jane Smith         IT  85000       10     TRUE
5  E005 Chris Green         IT  90000       12     TRUE
[1] "Employees in 'IT' department who are active:"
  EmpID        Name Department Salary YearsExp IsActive
2  E002  Jane Smith         IT  85000       10     TRUE
5  E005 Chris Green         IT  90000       12     TRUE
[1] "Names and Salary of employees with > 8 years experience:"
        Name Salary
2 Jane Smith  85000
5 Chris Green 90000
[1] "Data frame after modifications:"
  EmpID        Name Department Salary YearsExp IsActive
1  E001    John Doe         HR  62000        5     TRUE
2  E002  Jane Smith  Marketing  85000       10     TRUE
3  E003 Peter Jones      Sales  70000        7    FALSE
4  E004  Mary Brown         HR  62000        6     TRUE
5  E005 Chris Green         IT  90000       12     TRUE
[1] "Data frame after adding 'Bonus' column:"
  EmpID        Name Department Salary YearsExp IsActive Bonus
1  E001    John Doe         HR  62000        5     TRUE  6200
2  E002  Jane Smith  Marketing  85000       10     TRUE  8500
3  E003 Peter Jones      Sales  70000        7    FALSE  7000
4  E004  Mary Brown         HR  62000        6     TRUE  6200
5  E005 Chris Green         IT  90000       12     TRUE  9000
[1] "Data frame after removing 'IsActive' column:"
  EmpID        Name Department Salary YearsExp Bonus
1  E001    John Doe         HR  62000        5  6200
2  E002  Jane Smith  Marketing  85000       10  8500
3  E003 Peter Jones      Sales  70000        7  7000
4  E004  Mary Brown         HR  62000        6  6200
5  E005 Chris Green         IT  90000       12  9000
```

---

#### **Useful Data Frame Functions**

Several functions are commonly used to inspect and manipulate data frames:

* `str()`: Displays the internal structure of the data frame, including column names and types. Highly recommended for initial data inspection.
* `summary()`: Provides a statistical summary of each column.
* `head()`: Shows the first few rows (default 6).
* `tail()`: Shows the last few rows (default 6).
* `colnames()` / `names()`: Get or set column names.
* `rownames()`: Get or set row names.
* `dim()`: Returns the number of rows and columns.
* `nrow()` / `ncol()`: Returns the number of rows/columns.
* `rbind()` / `cbind()`: Used to combine data frames by rows or columns.

**Code Snippets:**

```r
# Re-create a clean data frame for demonstration
demo_df <- data.frame(
    Student = c("A", "B", "C", "D", "E", "F", "G", "H"),
    Gender = c("M", "F", "F", "M", "F", "M", "M", "F"),
    Score = c(85, 92, 78, 65, 95, 88, 70, 80),
    Grade = c("B", "A", "C", "D", "A", "B", "C", "B"),
    stringsAsFactors = FALSE
)
print("Demo Data Frame:")
print(demo_df)

# Inspect structure
print("Structure of demo_df (str()):")
str(demo_df)

# Get a summary of the data
print("Summary of demo_df:")
summary(demo_df)

# View the first few rows
print("First 3 rows:")
print(head(demo_df, n = 3))

# View the last few rows
print("Last 2 rows:")
print(tail(demo_df, n = 2))

# Get/Set column names
print("Column names:")
print(colnames(demo_df))
# colnames(demo_df)[3] <- "ExamScore" # To rename a column
# print(colnames(demo_df))

# Get/Set row names (default is numbers)
print("Row names:")
print(rownames(demo_df))
# rownames(demo_df) <- paste0("Obs_", 1:nrow(demo_df)) # To set custom row names
# print(rownames(demo_df))

# Get dimensions
print("Dimensions (rows, columns):")
print(dim(demo_df))
print("Number of rows:")
print(nrow(demo_df))
print("Number of columns:")
print(ncol(demo_df))

# Combining data frames
new_students_df <- data.frame(
    Student = c("I", "J"),
    Gender = c("F", "M"),
    Score = c(90, 75),
    Grade = c("A", "C"),
    stringsAsFactors = FALSE
)

# Row bind (add rows)
combined_df_rows <- rbind(demo_df, new_students_df)
print("Combined Data Frame (rows):")
print(combined_df_rows)

# Create another column as a data frame
new_column_df <- data.frame(
    Attendance = c("High", "Medium", "High", "Low", "High", "Medium", "Low", "High", "High", "Medium"),
    stringsAsFactors = FALSE
)

# Column bind (add columns - requires same number of rows)
# Note: new_column_df has 10 rows, combined_df_rows has 10 rows
combined_df_cols <- cbind(combined_df_rows, new_column_df)
print("Combined Data Frame (columns):")
print(combined_df_cols)
```

**Output:**

```
[1] "Demo Data Frame:"
  Student Gender Score Grade
1       A      M    85     B
2       B      F    92     A
3       C      F    78     C
4       D      M    65     D
5       E      F    95     A
6       F      M    88     B
7       G      M    70     C
8       H      F    80     B
[1] "Structure of demo_df (str()):"
'data.frame': 8 obs. of  4 variables:
 $ Student: chr  "A" "B" "C" "D" ...
 $ Gender : chr  "M" "F" "F" "M" ...
 $ Score  : num  85 92 78 65 95 88 70 80
 $ Grade  : chr  "B" "A" "C" "D" ...
[1] "Summary of demo_df:"
   Student             Gender              Score          Grade
 Length:8           Length:8           Min.   :65.0   Length:8
 Class :character   Class :character   1st Qu.:76.0   Class :character
 Mode  :character   Mode  :character   Median :82.5   Mode  :character
                                       Mean   :81.6
                                       3rd Qu.:86.8
                                       Max.   :95.0
[1] "First 3 rows:"
  Student Gender Score Grade
1       A      M    85     B
2       B      F    92     A
3       C      F    78     C
[1] "Last 2 rows:"
  Student Gender Score Grade
7       G      M    70     C
8       H      F    80     B
[1] "Column names:"
[1] "Student"  "Gender"   "Score"    "Grade"
[1] "Row names:"
[1] "1" "2" "3" "4" "5" "6" "7" "8"
[1] "Dimensions (rows, columns):"
[1] 8 4
[1] "Number of rows:"
[1] 8
[1] "Number of columns:"
[1] 4
[1] "Combined Data Frame (rows):"
   Student Gender Score Grade
1        A      M    85     B
2        B      F    92     A
3        C      F    78     C
4        D      M    65     D
5        E      F    95     A
6        F      M    88     B
7        G      M    70     C
8        H      F    80     B
9        I      F    90     A
10       J      M    75     C
[1] "Combined Data Frame (columns):"
   Student Gender Score Grade Attendance
1        A      M    85     B       High
2        B      F    92     A     Medium
3        C      F    78     C       High
4        D      M    65     D        Low
5        E      F    95     A       High
6        F      M    88     B     Medium
7        G      M    70     C        Low
8        H      F    80     B       High
9        I      F    90     A       High
10       J      M    75     C     Medium
```

---

This lesson provided a comprehensive overview of data frames, their creation, various methods for indexing and manipulation, and useful associated functions. Data frames are central to almost all data analysis workflows in R, and mastering them is a crucial step.

**Next, we will proceed to Lesson 5: Factors.**
