# 🔧 Repair Complaint Analysis & Tagging – Task 2

This project focuses on analyzing customer repair data, extracting structured insights from unstructured complaint fields, and tagging each record based on components and failure conditions. The dataset was cleaned, visualized, and enriched with keyword-based tags to support future NLP or predictive modeling use cases.

---

## 📁 Project Summary

- **Records**: 100 (reduced to 69 after outlier removal)
- **Columns**: 52
- **Objective**: Clean and analyze the repair dataset, extract tags from verbatim fields, and summarize key failure patterns and cost insights.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Matplotlib & Seaborn
- Regular Expressions (re)
- CSV / Excel
- UTF-8 Encoding Handling

---

## 📌 Key Steps & Methodology

### 1️⃣ Column Analysis

| Type            | Example Columns                                      |
|------------------|-------------------------------------------------------|
| Text Fields      | `CUSTOMER_VERBATIM`, `CORRECTION_VERBATIM`           |
| Categorical      | `STATE`, `ENGINE`, `PLATFORM`, `TRANSMISSION`        |
| Date             | `REPAIR_DATE`                                        |
| Numerical        | `REPAIR_AGE`, `KM`, `TOTALCOST`, `LBRCOST`           |
| Identifiers      | `VIN`, `TRANSACTION_ID` (treated as primary keys)    |

---

### 2️⃣ Data Cleaning

- **Missing Values**:
  - Rows with missing critical fields were dropped
  - Simple imputation (e.g., `"Unknown"`) used for non-critical categorical columns
- **Categorical Normalization**:
  - Used `.str.lower().strip()` to standardize values
  - Fixed typos and inconsistent formats
- **Outlier Removal**:
  - Applied **IQR method** to numerical fields (`KM`, `REPAIR_AGE`, `TOTALCOST`, `LBRCOST`)
  - Final dataset: **69 records**

---

### 3️⃣ Visualizations

- 📊 **Top 10 Complaint Types**  
  Identified high-frequency issues – especially related to **QA** and **manufacturing defects**

- 🗺️ **Top 10 States by Repair Volume**  
  Bar chart showed states like **FL** and **OH** had the highest repair counts

- 💰 **Average Repair Cost by State**  
  Highlighted regional variations in total repair costs

---

### 4️⃣ Tagging Logic

Used basic keyword matching to extract tags from:
- `CUSTOMER_VERBATIM`
- `CORRECTION_VERBATIM`

**Tag Categories**:
- 🧩 **Component Tags**: e.g., `steering wheel`, `transmission`, `engine`
- ⚠️ **Condition Tags**: e.g., `not working`, `heating`, `peeling`, `loose`

**Sample Tags**:
`"steering wheel"`, `"heating"`, `"replaced"`, `"loose"`, `"cover"`

Generated a new `ALL_TAGS` column with comma-separated matched terms.

---

## 💡 Key Takeaways & Recommendations

### 🔍 Tag-Based Insights
- Steering-related issues were the most frequently mentioned
- Comfort and cosmetic problems (like **heating**, **peeling**) dominated
- Repairs without error codes indicate possible **quality assurance gaps**

### ✅ Recommendations
- Prioritize **root cause analysis** for high-frequency tags
- Improve **pre-delivery inspections** for comfort features
- Consider applying **sentiment analysis** to verbatim text

### ⚠️ Discrepancies Handled
- **Foreign language text**: Considered for translation in future versions
- **Encoding issues**: Handled using `utf-8` decoding
- **Inconsistent terminology**: Unified through normalization and tagging

---

## 🗂️ Deliverables

- ✅ Cleaned dataset with new `ALL_TAGS` column
- 🐍 Python script / notebook for preprocessing and analysis
- 📊 Visualizations for repair type, cost, and geography

---

## 🔮 Future Use Case

The `ALL_TAGS` column can be used to:
- Train NLP models for automated tagging
- Build predictive models to forecast failures based on symptoms
- Power dashboards for support teams or product QA

---

