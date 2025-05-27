
import os

# Define the base directory name for the course
base_course_dir = "Comprehensive_R_Programming_Course"

# Define the course structure with phases, modules (which are now folders),
# and their contained lesson files with placeholder content.

course_outline = {
    "Phase_1_Introduction_to_R_and_Fundamentals": {
        "Module_1.1_Getting_Started_with_R": { # This is now a folder
            "lesson_1_What_is_R_and_RStudio.md": """# Lesson 1: What is R and RStudio?

* Introduction to R: What it is and why it's used in data science.
* Brief overview of the R ecosystem.
* Installing R and RStudio on your system.
* Tour of the RStudio Interface: Console, Script Editor, Environment, Files/Plots/Packages/Help panes.
""",
            "lesson_2_Basic_Operations.md": """# Lesson 2: Basic Operations

* R as a calculator: Basic arithmetic operations (+, -, *, /, ^, %%, %/%).
* Understanding operator precedence.
* Introduction to comments (`#`).
* Creating and running your first R scripts.
""",
            "lesson_3_Variables_and_Assignment.md": """# Lesson 3: Variables and Assignment

* Understanding variables in R.
* Assignment operators (`<-`, `=`).
* Rules for naming variables.
* Checking variable types and values.
"""
        },
        "Module_1.2_Data_Types_and_Structures": { # This is now a folder
            "lesson_1_Atomic_Vectors.md": """# Lesson 1: Atomic Vectors

* Introduction to vectors: The fundamental data structure in R.
* Numeric, Integer, Character, Logical, Complex data types.
* Creating vectors using `c()`.
* Vector indexing and slicing.
* Vectorized operations.
""",
            "lesson_2_Matrices_and_Arrays.md": """# Lesson 2: Matrices and Arrays

* Creating matrices (`matrix()`) and understanding their dimensions.
* Matrix indexing by row and column.
* Basic matrix operations (addition, multiplication, transpose).
* Brief introduction to multi-dimensional arrays.
""",
            "lesson_3_Lists.md": """# Lesson 3: Lists

* Understanding lists as heterogeneous data structures.
* Creating lists (`list()`).
* Accessing list elements using `[]`, `[[]]`, and `$`.
* Nested lists.
""",
            "lesson_4_Data_Frames_and_Factors.md": """# Lesson 4: Data Frames and Factors

* Data Frames: The most common data structure for tabular data.
* Creating data frames (`data.frame()`).
* Accessing columns by name and position.
* Basic data frame operations (`str()`, `summary()`, `dim()`, `names()`).
* Introduction to Factors: Handling categorical data.
* Ordering and re-leveling factors.
"""
        },
        "Module_1.3_Basic_Operations_and_Control_Flow": { # This is now a folder
            "lesson_1_Operators.md": """# Lesson 1: Operators

* Arithmetic Operators.
* Relational Operators (==, !=, <, >, <=, >=).
* Logical Operators (`&`, `|`, `!`, `&&`, `||`).
* Miscellaneous Operators (`%in%`, `%*%`).
""",
            "lesson_2_Conditional_Statements.md": """# Lesson 2: Conditional Statements

* The `if` statement.
* `if-else` statements.
* `if-else if-else` ladders.
* Using `ifelse()` for vectorized conditional logic.
""",
            "lesson_3_Loops.md": """# Lesson 3: Loops

* The `for` loop: Iterating over sequences.
* The `while` loop: Repeating until a condition is met.
* The `repeat` loop: Infinite loops with `break`.
* Using `next` to skip iterations.
* Why vectorization is preferred over loops in R.
"""
        },
        "Module_1.4_Functions_and_Packages": { # This is now a folder
            "lesson_1_Built_in_Functions.md": """# Lesson 1: Built-in Functions

* Understanding the purpose and usage of common built-in R functions (e.g., `mean()`, `sum()`, `max()`, `min()`, `length()`).
* Function arguments and default values.
* Using R's help system (`?`, `help()`, `example()`).
""",
            "lesson_2_Creating_Custom_Functions.md": """# Lesson 2: Creating Custom Functions

* Defining your own functions using the `function()` keyword.
* Function arguments, return values.
* Understanding scope (global vs. local variables).
* Best practices for writing readable functions.
""",
            "lesson_3_Introduction_to_Packages.md": """# Lesson 3: Introduction to Packages

* What are R packages and why are they important?
* Installing packages from CRAN (`install.packages()`).
* Loading packages into your R session (`library()`, `require()`).
* Exploring package documentation.
"""
        }
    },
    "Phase_2_Data_Manipulation_and_Wrangling": {
        "Module_2.1_Data_Import_and_Export": {
            "lesson_1_Importing_CSV_and_Text_Files.md": """# Lesson 1: Importing CSV and Text Files

* Reading data from CSV files using `read.csv()` and `read_csv()` from `readr`.
* Importing plain text files (`read.table()`, `read_delim()`).
* Understanding common import parameters (header, separator, missing values).
""",
            "lesson_2_Importing_Excel_and_Other_Formats.md": """# Lesson 2: Importing Excel and Other Formats

* Importing data from Excel files using `read_excel()` from `readxl`.
* Brief overview of importing data from statistical software (SAS, SPSS, Stata) using `haven`.
* Introduction to importing data from databases (conceptual overview).
""",
            "lesson_3_Exporting_Data.md": """# Lesson 3: Exporting Data

* Saving data to CSV (`write.csv()`, `write_csv()`).
* Exporting to other text formats.
* Saving R objects (`save()`, `saveRDS()`).
"""
        },
        "Module_2.2_Introduction_to_dplyr_for_Data_Transformation": {
            "lesson_1_The_Pipe_Operator.md": """# Lesson 1: The Pipe Operator

* Understanding the pipe operator (`%>%` from `magrittr` or `|>` in R 4.1+).
* Writing readable and chained operations.
""",
            "lesson_2_Selecting_and_Filtering.md": """# Lesson 2: Selecting and Filtering

* `select()`: Choosing columns by name, range, and pattern.
* `filter()`: Subsetting rows based on logical conditions.
* Combining `select()` and `filter()`.
""",
            "lesson_3_Mutate_and_Arrange.md": """# Lesson 3: Mutate and Arrange

* `mutate()`: Creating new variables or modifying existing ones.
* `transmute()`: Creating new variables while dropping others.
* `arrange()`: Reordering rows based on column values.
""",
            "lesson_4_Summarise_and_Group_by.md": """# Lesson 4: Summarise and Group by

* `summarise()` (or `summarize()`): Calculating aggregated statistics.
* `group_by()`: Performing operations on subsets of data.
* Combining `group_by()` and `summarise()`.
"""
        },
        "Module_2.3_Reshaping_and_Joining_Data": {
            "lesson_1_Long_and_Wide_Data.md": """# Lesson 1: Long and Wide Data

* Understanding the concepts of wide vs. long data formats.
* Using `pivot_longer()` from `tidyr` to transform wide to long.
* Using `pivot_wider()` from `tidyr` to transform long to wide.
""",
            "lesson_2_Uniting_and_Separating_Columns.md": """# Lesson 2: Uniting and Separating Columns

* `unite()`: Combining multiple columns into one.
* `separate()`: Splitting a single column into multiple.
""",
            "lesson_3_Relational_Joins.md": """# Lesson 3: Relational Joins

* Understanding different types of joins: `left_join()`, `right_join()`, `inner_join()`, `full_join()`.
* Joining data frames based on common key columns.
* Handling multiple join keys.
""",
            "lesson_4_Set_Operations.md": """# Lesson 4: Set Operations

* `union()`: Combining rows from two data frames.
* `intersect()`: Finding common rows between two data frames.
* `setdiff()`: Finding rows present in one but not the other.
"""
        },
        "Module_2.4_String_Manipulation_and_Regular_Expressions": {
            "lesson_1_Basic_String_Functions.md": """# Lesson 1: Basic String Functions

* `nchar()`: Counting characters.
* `paste()`, `paste0()`: Concatenating strings.
* `substr()`, `substring()`: Extracting substrings.
* `toupper()`, `tolower()`: Changing case.
* `grepl()`, `grep()`: Searching for patterns.
* `gsub()`, `sub()`: Replacing patterns.
""",
            "lesson_2_Introduction_to_stringr.md": """# Lesson 2: Introduction to stringr

* Overview of the `stringr` package for consistent string manipulation.
* Common `stringr` functions (e.g., `str_detect()`, `str_replace()`, `str_subset()`, `str_extract()`).
""",
            "lesson_3_Regular_Expressions_Basics.md": """# Lesson 3: Regular Expressions Basics

* What are regular expressions (regex) and why are they useful?
* Basic regex patterns: anchors, quantifiers, character classes.
* Applying regex in `base R` and `stringr` functions.
"""
        }
    },
    "Phase_3_Data_Visualization_with_ggplot2": {
        "Module_3.1_Fundamentals_of_ggplot2": {
            "lesson_1_Grammar_of_Graphics.md": """# Lesson 1: Grammar of Graphics

* Understanding the philosophy behind `ggplot2`.
* Key components: data, aesthetics (`aes()`), geoms.
* Basic `ggplot()` structure.
""",
            "lesson_2_Common_Geoms.md": """# Lesson 2: Common Geoms

* `geom_point()`: Scatter plots.
* `geom_line()`: Line plots.
* `geom_bar()`: Bar charts.
* `geom_histogram()`: Histograms.
* `geom_boxplot()`: Box plots.
* `geom_density()`: Density plots.
""",
            "lesson_3_Labels_Titles_and_Annotations.md": """# Lesson 3: Labels, Titles, and Annotations

* Adding main titles, subtitles, and captions.
* Labeling axes (`labs()`, `xlab()`, `ylab()`).
* Adding text annotations to plots.
"""
        },
        "Module_3.2_Customizing_and_Enhancing_Plots": {
            "lesson_1_Scales_and_Coordinates.md": """# Lesson 1: Scales and Coordinates

* Customizing axes limits and breaks (`scale_x_continuous()`, `scale_y_discrete()`).
* Controlling color, fill, size, shape, and alpha aesthetics (`scale_color_manual()`, `scale_fill_brewer()`).
* Coordinate systems (`coord_flip()`, `coord_polar()`).
""",
            "lesson_2_Faceting.md": """# Lesson 2: Faceting

* `facet_wrap()`: Creating a grid of plots based on one or more variables.
* `facet_grid()`: Creating a grid based on two variables (rows and columns).
* Controlling facet labels and scales.
""",
            "lesson_3_Themes.md": """# Lesson 3: Themes

* Using built-in themes (`theme_minimal()`, `theme_bw()`, `theme_classic()`).
* Customizing theme elements (text size, font, background, grid lines) using `theme()`.
* Saving and reusing custom themes.
""",
            "lesson_4_Saving_Plots.md": """# Lesson 4: Saving Plots

* Saving plots to various formats (PNG, JPEG, PDF, SVG) using `ggsave()`.
* Controlling plot dimensions and resolution.
"""
        },
        "Module_3.3_Advanced_Visualizations": {
            "lesson_1_Specialized_Geoms_and_Plots.md": """# Lesson 1: Specialized Geoms and Plots

* Violin plots and Ridge plots for distribution comparisons.
* Heatmaps for showing relationships between three variables (`geom_tile()`).
* Correlograms for visualizing correlations.
""",
            "lesson_2_Interactive_Plots.md": """# Lesson 2: Interactive Plots

* Brief introduction to `plotly` for making `ggplot2` plots interactive.
* Basic interactivity: tooltips, zoom, pan.
* Conceptual overview of `shiny` for web-based interactive visualizations.
""",
            "lesson_3_Working_with_Dates_and_Times.md": """# Lesson 3: Working with Dates and Times

* Handling date and time data types in R (`Date`, `POSIXct`, `POSIXlt`).
* Plotting time series data with `ggplot2`.
* Using `lubridate` for easier date/time manipulation.
"""
        }
    },
    "Phase_4_Statistical_Analysis_and_Modeling": {
        "Module_4.1_Descriptive_Statistics_and_Probability": {
            "lesson_1_Measures_of_Central_Tendency.md": """# Lesson 1: Measures of Central Tendency

* Mean, Median, Mode: Calculation and interpretation.
* When to use each measure.
""",
            "lesson_2_Measures_of_Dispersion.md": """# Lesson 2: Measures of Dispersion

* Variance, Standard Deviation, Interquartile Range (IQR).
* Range and Quantiles.
* Understanding spread and variability.
""",
            "lesson_3_Understanding_Distributions.md": """# Lesson 3: Understanding Distributions

* Normal distribution: Properties and importance.
* Binomial and Poisson distributions (conceptual).
* Visualizing distributions (histograms, density plots).
""",
            "lesson_4_Basic_Probability.md": """# Lesson 4: Basic Probability

* Concepts of probability: events, outcomes, sample space.
* Conditional probability (brief introduction).
* Introduction to simulation.
"""
        },
        "Module_4.2_Inferential_Statistics_and_Hypothesis_Testing": {
            "lesson_1_Sampling_and_CLT.md": """# Lesson 1: Sampling and Central Limit Theorem

* Understanding samples vs. populations.
* Random sampling techniques.
* The Central Limit Theorem (CLT) and its implications.
""",
            "lesson_2_Confidence_Intervals.md": """# Lesson 2: Confidence Intervals

* Constructing and interpreting confidence intervals for means and proportions.
* Understanding margin of error.
""",
            "lesson_3_T_tests_and_ANOVA.md": """# Lesson 3: T-tests and ANOVA

* One-sample, two-sample, and paired T-tests for comparing means.
* Analysis of Variance (ANOVA): One-way and two-way ANOVA for comparing multiple means.
* Post-hoc tests.
""",
            "lesson_4_Chi_squared_Test.md": """# Lesson 4: Chi-squared Test

* Chi-squared test for independence: Testing relationships between categorical variables.
* Chi-squared goodness-of-fit test.
"""
        },
        "Module_4.3_Linear_Regression": {
            "lesson_1_Simple_Linear_Regression.md": """# Lesson 1: Simple Linear Regression

* Introduction to regression: Predicting a continuous outcome.
* Fitting a simple linear regression model using `lm()`.
* Interpreting coefficients (slope, intercept).
* R-squared and its meaning.
""",
            "lesson_2_Multiple_Linear_Regression.md": """# Lesson 2: Multiple Linear Regression

* Extending to multiple predictor variables.
* Interpreting coefficients in a multiple regression model.
* Dealing with multicollinearity (conceptual).
* Basic variable selection strategies.
""",
            "lesson_3_Assumptions_and_Diagnostics.md": """# Lesson 3: Assumptions and Diagnostics

* Key assumptions of linear regression (linearity, independence, homoscedasticity, normality of residuals).
* Visualizing residuals to check assumptions.
* Identifying influential points.
"""
        },
        "Module_4.4_Logistic_Regression": {
            "lesson_1_Introduction_to_GLMs.md": """# Lesson 1: Introduction to Generalized Linear Models (GLMs)

* When to use GLMs.
* Difference between linear and logistic regression.
* The concept of a link function.
""",
            "lesson_2_Binary_Logistic_Regression.md": """# Lesson 2: Binary Logistic Regression

* Fitting a logistic regression model using `glm()`.
* Interpreting coefficients as log-odds.
* Calculating and interpreting odds ratios.
* Predicting probabilities.
""",
            "lesson_3_Model_Evaluation.md": """# Lesson 3: Model Evaluation

* Confusion Matrix: Accuracy, precision, recall, F1-score.
* ROC Curve and AUC (Area Under the Curve).
* Choosing an appropriate threshold.
"""
        }
    },
    "Phase_5_Advanced_R_Programming_and_Best_Practices": {
        "Module_5.1_Functional_Programming_in_R": {
            "lesson_1_Apply_Family_Functions.md": """# Lesson 1: Apply Family Functions

* `lapply()`: Applying a function to list or vector elements.
* `sapply()`: Simplified version of `lapply()`.
* `mapply()`: Multi-argument version of `sapply()`.
* `tapply()`: Applying a function over ragged arrays (grouped data).
* `apply()`: Applying a function to margins of arrays/matrices.
""",
            "lesson_2_Introduction_to_purrr.md": """# Lesson 2: Introduction to purrr

* Overview of the `purrr` package for functional programming in the tidyverse.
* `map()` functions: `map()`, `map_dfr()`, `map_chr()`, `map_lgl()`, `map_dbl()`.
* `walk()`: For side effects.
* Using anonymous functions (`~`) with `purrr`.
""",
            "lesson_3_Anonymous_Functions.md": """# Lesson 3: Anonymous Functions

* Creating and using nameless functions on the fly.
* Benefits in functional programming contexts.
"""
        },
        "Module_5.2_Performance_and_Debugging": {
            "lesson_1_Profiling_R_Code.md": """# Lesson 1: Profiling R Code

* Measuring execution time with `system.time()`.
* Using `profvis` for detailed code profiling.
* Identifying bottlenecks in your R code.
""",
            "lesson_2_Vectorization_vs_Loops.md": """# Lesson 2: Vectorization vs. Loops

* Deep dive into why vectorized operations are generally faster in R.
* Examples comparing loop performance to vectorized alternatives.
* When loops might still be necessary.
""",
            "lesson_3_Debugging_Tools.md": """# Lesson 3: Debugging Tools

* Using `browser()` for interactive debugging.
* `debug()` and `undebug()` for function tracing.
* `traceback()`: Understanding error call stacks.
* Using RStudio's debugging features.
""",
            "lesson_4_Error_Handling.md": """# Lesson 4: Error Handling

* Using `try()` and `tryCatch()` for robust code.
* Defining custom error messages.
* Handling warnings.
"""
        },
        "Module_5.3_Data_Structures_and_Algorithms_in_R": {
            "lesson_1_Advanced_Data_Structures.md": """# Lesson 1: Advanced Data Structures

* Advanced use cases for lists and data frames.
* Introduction to S3 and S4 object systems (conceptual overview).
* Reference classes (brief mention).
""",
            "lesson_2_Basic_Algorithms_in_R.md": """# Lesson 2: Basic Algorithms in R

* Conceptual overview of sorting algorithms (e.g., bubble sort, quicksort, merge sort) and their implementation in R (e.g., `sort()`, `order()`).
* Conceptual overview of searching algorithms.
"""
        },
        "Module_5.4_Advanced_Data_Manipulation_and_Big_Data_Concepts": {
            "lesson_1_Data_table_Introduction.md": """# Lesson 1: data.table Introduction

* Brief introduction to the `data.table` package for high-performance data manipulation.
* Key syntax differences and performance benefits compared to base R and `dplyr`.
* Basic `data.table` operations (selection, filtering, aggregation).
""",
            "lesson_2_Memory_Management.md": """# Lesson 2: Memory Management

* Understanding R's memory usage.
* Strategies for efficient memory management in R.
* Garbage collection (`gc()`).
""",
            "lesson_3_Introduction_to_Big_Data_in_R.md": """# Lesson 3: Introduction to Big Data in R

* Challenges of handling large datasets in R.
* Overview of packages for out-of-memory computations (e.g., `ff`, `disk.frame`).
* Brief introduction to the `arrow` package for Apache Arrow integration.
"""
        }
    },
    "Phase_6_Specialized_Topics_and_Application": {
        "Module_6.1_Time_Series_Analysis": {
            "lesson_1_Time_Series_Objects.md": """# Lesson 1: Time Series Objects

* Creating and manipulating time series objects (`ts`, `xts`, `zoo`).
* Date and time handling for time series.
* Plotting time series data.
""",
            "lesson_2_Time_Series_Decomposition.md": """# Lesson 2: Time Series Decomposition

* Understanding trend, seasonality, and remainder components.
* Additive and multiplicative decomposition (`decompose()`, `stl()`).
* Visualizing decomposed components.
""",
            "lesson_3_Basic_Forecasting_Models.md": """# Lesson 3: Basic Forecasting Models

* Introduction to ARIMA models (conceptual).
* Exponential Smoothing (ETS).
* Using the `forecast` package for automated forecasting.
"""
        },
        "Module_6.2_Machine_Learning_in_R": {
            "lesson_1_Supervised_vs_Unsupervised_Learning.md": """# Lesson 1: Supervised vs. Unsupervised Learning

* Fundamental concepts and differences.
* Examples of common tasks for each type.
* Data splitting for training and testing.
""",
            "lesson_2_Decision_Trees_and_Random_Forests.md": """# Lesson 2: Decision Trees and Random Forests

* Building and visualizing decision trees (`rpart`).
* Understanding overfitting and pruning.
* Introduction to Random Forests (`randomForest`).
* Feature importance.
""",
            "lesson_3_Clustering.md": """# Lesson 3: Clustering

* Introduction to K-Means Clustering.
* Choosing the optimal number of clusters.
* Interpreting clustering results.
* Hierarchical clustering (brief mention).
""",
            "lesson_4_Model_Tuning_and_Evaluation.md": """# Lesson 4: Model Tuning and Evaluation

* Cross-validation techniques (k-fold, leave-one-out).
* Hyperparameter tuning.
* Introduction to the `caret` and `tidymodels` ecosystems for consistent ML workflows.
"""
        },
        "Module_6.3_Reporting_and_Reproducibility_with_RMarkdown": {
            "lesson_1_Introduction_to_RMarkdown.md": """# Lesson 1: Introduction to R Markdown

* What is R Markdown and its role in reproducible research?
* Basic R Markdown syntax: YAML header, code chunks, inline R code.
* Output formats: HTML, PDF, Word.
""",
            "lesson_2_Including_Code_Plots_and_Tables.md": """# Lesson 2: Including Code, Plots, and Tables

* Controlling code chunk options (`echo`, `eval`, `include`, `message`, `warning`).
* Embedding R plots directly.
* Creating formatted tables (e.g., using `knitr::kable`, `flextable`).
""",
            "lesson_3_Parameterizing_Reports.md": """# Lesson 3: Parameterizing Reports

* Making reports dynamic with parameters.
* Generating multiple reports from a single R Markdown file.
"""
        },
        "Module_6.4_Building_Interactive_Web_Applications_with_Shiny": {
            "lesson_1_Introduction_to_Shiny.md": """# Lesson 1: Introduction to Shiny

* What is Shiny and why use it for web applications?
* Basic Shiny app structure: `ui.R` (user interface) and `server.R` (server logic).
* Running your first Shiny app.
""",
            "lesson_2_Input_Widgets_and_Output_Elements.md": """# Lesson 2: Input Widgets and Output Elements

* Common input widgets (sliders, text inputs, action buttons, select inputs).
* Displaying outputs (plots, tables, text).
* Understanding reactivity in Shiny.
""",
            "lesson_3_Reactives_and_Observers.md": """# Lesson 3: Reactives and Observers

* `reactive()` expressions: Caching computations.
* `observeEvent()` and `eventReactive()` for controlling reactivity flow.
* Understanding the reactive graph.
""",
            "lesson_4_Deploying_Shiny_Apps.md": """# Lesson 4: Deploying Shiny Apps

* Brief overview of options for deploying Shiny apps (shinyapps.io, RStudio Connect, Docker).
* Best practices for Shiny app development.
"""
        }
    },
    "Phase_7_R_for_Advanced_Data_Science_and_Deployment": {
        "Module_7.1_Advanced_Machine_Learning_Topics": {
            "lesson_1_Gradient_Boosting_Machines.md": """# Lesson 1: Gradient Boosting Machines

* Introduction to boosting.
* Using XGBoost and LightGBM in R.
* Hyperparameter tuning for boosting models.
""",
            "lesson_2_Support_Vector_Machines.md": """# Lesson 2: Support Vector Machines (SVMs)

* Conceptual understanding of SVMs for classification and regression.
* Kernel functions.
* Implementing SVMs in R.
""",
            "lesson_3_Neural_Networks_Basics.md": """# Lesson 3: Neural Networks Basics

* Introduction to Artificial Neural Networks (ANNs).
* Perceptrons, layers, activation functions.
* Brief introduction to using `keras` and `tensorflow` in R for deep learning.
""",
            "lesson_4_Ensemble_Methods.md": """# Lesson 4: Ensemble Methods

* Bagging, boosting, and stacking (recap and deeper dive).
* Combining multiple models for improved performance.
"""
        },
        "Module_7.2_Big_Data_Integration_and_Scalability": {
            "lesson_1_Connecting_R_to_Spark.md": """# Lesson 1: Connecting R to Spark

* Introduction to Apache Spark.
* Using `sparklyr` to interact with Spark from R.
* Performing data manipulation and machine learning on Spark.
""",
            "lesson_2_Working_with_Distributed_File_Systems.md": """# Lesson 2: Working with Distributed File Systems

* Conceptual understanding of HDFS.
* Reading and writing data to HDFS from R.
""",
            "lesson_3_Parallel_Computing_in_R.md": """# Lesson 3: Parallel Computing in R

* Utilizing multiple cores for faster computations.
* Packages like `parallel` and `foreach`.
* Strategies for parallelizing loops and tasks.
"""
        },
        "Module_7.3_Version_Control_and_Package_Development": {
            "lesson_1_Git_and_GitHub_for_R_Projects.md": """# Lesson 1: Git and GitHub for R Projects

* Setting up Git with RStudio.
* Basic Git commands (`commit`, `push`, `pull`, `branch`).
* Collaborating on R projects using GitHub.
* Resolving merge conflicts.
""",
            "lesson_2_Best_Practices_for_R_Development.md": """# Lesson 2: Best Practices for R Development

* Coding style guides (e.g., Tidyverse style guide).
* Project organization using RStudio Projects.
* Writing clean, maintainable, and well-documented R code.
""",
            "lesson_3_Basic_R_Package_Development.md": """# Lesson 3: Basic R Package Development

* Why create R packages?
* Package structure (R/, man/, inst/, DESCRIPTION, NAMESPACE).
* Using `devtools` for package development.
* Documenting functions with `roxygen2`.
* Building and checking packages.
"""
        },
        "Module_7.4_Deployment_and_Production_Considerations": {
            "lesson_1_Containerization_with_Docker.md": """# Lesson 1: Containerization with Docker

* Introduction to Docker: What it is and why it's useful for R.
* Creating a Dockerfile for an R application.
* Building and running Docker containers with R.
* Docker Compose for multi-service applications.
""",
            "lesson_2_API_Development_with_R.md": """# Lesson 2: API Development with R

* Introduction to `plumber` for creating RESTful APIs from R code.
* Defining endpoints, inputs, and outputs.
* Deploying `plumber` APIs.
""",
            "lesson_3_Monitoring_and_Logging_R_Applications.md": """# Lesson 3: Monitoring and Logging R Applications

* Strategies for logging events and errors in R scripts and applications.
* Introduction to monitoring tools and dashboards (conceptual).
""",
            "lesson_4_Ethical_Considerations_in_Data_Science.md": """# Lesson 4: Ethical Considerations in Data Science

* Data privacy, bias in algorithms, and transparency.
* Responsible AI practices.
* Ethical guidelines for data scientists.
"""
        }
    }
}

def create_course_materials(base_dir, outline):
    """
    Creates directories (phases, then modules) and Markdown lesson files
    based on the provided course outline.
    """
    os.makedirs(base_dir, exist_ok=True)
    print(f"Created base directory: {base_dir}")

    # Create the top-level README.md (introduction)
    readme_content = """# Welcome to the Comprehensive R Programming Course!

## Unlocking the Power of Data with R

Hello and welcome! I'm thrilled to present this comprehensive course designed to take you on an exciting journey from the very basics of R programming to advanced data science techniques. Whether you're a complete beginner with no prior coding experience or a seasoned professional looking to deepen your R skills, this course is meticulously structured to provide you with a robust foundation and the expertise to tackle real-world data challenges.

In today's data-driven world, R stands out as an incredibly powerful, versatile, and open-source language, favored by statisticians, data analysts, researchers, and data scientists worldwide. Its rich ecosystem of packages makes it an unparalleled tool for data manipulation, statistical analysis, stunning data visualization, and cutting-edge machine learning.

Just like my other course structures, we've organized this learning path into distinct **Phases**, each building upon the last. Within each phase, you'll find focused **Modules** (which are folders) that break down complex topics into digestible, hands-on lessons (which are Markdown files within those folders). My aim is to make your learning experience as clear, practical, and engaging as possible.

**What You'll Learn:**

* **Phase 1: Introduction to R and Fundamentals** - Get comfortable with the R environment, its core syntax, and fundamental data types.
* **Phase 2: Data Manipulation and Wrangling** - Master the art of preparing and transforming messy data into clean, analysis-ready formats using the powerful `tidyverse`.
* **Phase 3: Data Visualization with ggplot2** - Create compelling and insightful data visualizations that tell powerful stories.
* **Phase 4: Statistical Analysis and Modeling** - Dive into descriptive and inferential statistics, hypothesis testing, and foundational regression models.
* **Phase 5: Advanced R Programming and Best Practices** - Elevate your coding skills with functional programming, performance optimization, and debugging techniques.
* **Phase 6: Specialized Topics and Application** - Explore practical applications in time series analysis, machine learning, and reproducible reporting with R Markdown.
* **Phase 7: R for Advanced Data Science and Deployment** - Venture into advanced machine learning, big data integration, R package development, and deploying R applications.

Each module is crafted with practical examples, clear explanations, and hands-on exercises to solidify your understanding. My goal is not just to teach you R, but to empower you to think computationally and approach data problems with confidence.

I'm incredibly excited for you to embark on this learning adventure. Let's unlock the immense potential of R together!

Happy coding!

**[Your GitHub Username/Name]**
[Link to your GitHub Profile - Optional, but good for branding]
"""
    with open(os.path.join(base_dir, "README.md"), "w") as f:
        f.write(readme_content)
    print("Created info.md in the base directory.")

    for phase_name, modules_dict in outline.items():
        phase_path = os.path.join(base_dir, phase_name)
        os.makedirs(phase_path, exist_ok=True)
        print(f"  Created phase directory: {phase_path}")

        for module_name, lessons_dict in modules_dict.items():
            module_path = os.path.join(phase_path, module_name)
            os.makedirs(module_path, exist_ok=True) # Create module folder
            print(f"    Created module directory: {module_path}")

            for lesson_filename, content in lessons_dict.items():
                lesson_path = os.path.join(module_path, lesson_filename)
                with open(lesson_path, "w") as f:
                    f.write(content)
                print(f"      Created lesson file: {lesson_path}")

    print("\nCourse materials generation complete!")
    print(f"You can find your course structure in the '{base_course_dir}' folder.")

if __name__ == "__main__":
    create_course_materials(base_course_dir, course_outline)