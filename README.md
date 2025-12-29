# Retail Sales Performance & Store Analytics (Power BI)


## Project Overview

This project demonstrates an end-to-end analytics workflow aligned with Junior Business Analyst responsibilities. The objective was to transform raw retail sales data into a structured reporting solution that helps stakeholders understand overall performance, evaluate the impact of promotions and holidays, and assess store-level efficiency.

The project reflects a typical business analytics process: data preparation in Python, structured validation and modelling using SQL, and KPI-driven reporting in Power BI. The focus was on answering business questions and supporting decision-making rather than producing isolated charts.


**Tools:** Python (VS Code), SQL (SQLite), Power BI, DAX  


--


## Data and Preparation

The dataset contains weekly sales data across multiple stores and departments over several years. In addition to sales values, it includes calendar attributes, holiday indicators, promotional flags, store characteristics such as store size and type, and selected external economic factors. This structure enables analysis across time, location, and trading conditions, supporting both performance monitoring and operational insight.

### Data Preparation in Python (VS Code)

Python was used to prepare and validate the raw datasets before analysis. Key preparation steps included:

- Loading and inspecting raw datasets to understand structure, volume, and data quality  
- Standardising column names and formats to ensure consistency across files  
- Validating key fields such as store IDs, department IDs, and dates to support reliable joins  
- Reviewing data coverage across time and stores to identify gaps or inconsistencies  
- Deriving business-relevant indicators, such as return or negative sales weeks, to support later risk analysis  

### Data Modelling and Validation Using SQL (SQLite)

Once cleaned, the data was stored in a SQLite database and organised into a simple star schema, with a central sales fact table linked to store and calendar dimension tables. SQL was used to:

- Validate joins between fact and dimension tables  
- Confirm data completeness across stores and time periods  
- Explicitly define data types to ensure accurate reporting in Power BI  

This structured approach ensured the data was reliable, well-organised, and suitable for KPI-driven analysis and dashboard development.


---


## Dashboard Pages and Business Purpose

### Page 1: Executive Sales Overview

<img width="2144" height="1198" alt="image" src="https://github.com/user-attachments/assets/b6c22340-c0fd-49e8-8c45-da6ff40a16cb" />


This page provides a high-level view of overall business performance and establishes a baseline for analysis.

It answers:
- How is the business performing overall?  
- Are sales trending up or down over time?  
- Which stores and departments contribute most to total sales?  

Key metrics include total sales, average weekly sales, time-based trends, and top-performing stores and departments. This page is designed for quick performance monitoring and to highlight areas that require further analysis.


---


### Page 2: Promotion and Holiday Impact



<img width="2144" height="1198" alt="image" src="https://github.com/user-attachments/assets/adb2813d-f3a4-453a-80b1-1c3ec6e388c2" />


This page evaluates whether promotions and holidays drive meaningful sales uplift.

It answers:
- Do promotional weeks perform better than non-promotional weeks?  
- How do holiday periods compare to normal trading periods?  
- Is the business overly dependent on seasonal demand?  

Average weekly sales are benchmarked across promotional and non-promotional periods, with uplift percentages used to support evidence-based assessment of campaign effectiveness. This page supports tactical planning and marketing-related decisions.


---


### Page 3: Store Performance and Efficiency


<img width="2144" height="1198" alt="image" src="https://github.com/user-attachments/assets/2d86f8e3-7d1e-45fa-a128-2374c503b5fb" />


This page focuses on operational performance by analysing store-level efficiency rather than raw sales volume.

It answers:
- Which stores perform best relative to their size?  
- Which stores underperform or show inconsistent trends?  
- Where should operational attention be prioritised?  

Store efficiency is calculated by normalising sales by store size, enabling fair comparison across locations. Trend analysis highlights performance consistency and potential operational risk.


---


## Conclusion and Key Learnings

Through this project, I developed a practical understanding of how end-to-end analytics workflows operate in real business environments. I learned the importance of data quality and validation before reporting, how SQL supports reliable data modelling and analysis, and how Power BI dashboards should be designed around business questions rather than raw metrics.

Most importantly, this project strengthened my ability to translate data into insights that support operational and tactical decision-making, which is a core skill for entry-level roles such as Junior Business Analyst, Data Analyst, and Operations Analyst.


