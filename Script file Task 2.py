#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[184]:


df=pd.read_excel("DA -Task 2..xlsx")


# In[185]:


df.shape


# In[16]:


df.columns


# In[41]:


df.info()


# In[18]:


df.isnull().sum()


#   

#  # Column Wise Analysis

# In[29]:


df.columns


# In[22]:


df['VIN'].describe()


#  

# <b>Column: VIN</b>    
# Data Type: object (string)  
# Unique Values: 98 unique out of 100  
# Duplicated Values: 2 VINs are repeated  
# Distribution: Mostly unique per row, except 2 repeated cases
# 
# <b> Significance for Stakeholders:</b>  
# Acts as a vehicle identifier, helping trace history, repairs, and performance.
# Duplicate VINs could indicate repeated service or data entry issues – worth flagging.

# In[32]:


df['TRANSACTION_ID'].info()


# In[62]:


df['TRANSACTION_ID'].head()


# In[61]:


df['TRANSACTION_ID'].duplicated().value_counts()


#   

# <b>Column: TRANSACTION_ID</b>  
# Data Type: int64  
# Unique Values: 32 unique out of 100  
# Duplicated Values: 68 values are duplicates (with IDs repeating up to 10 times)  
# Distribution: Highly skewed — some IDs appear 10 times, others only once.
# 
# <b>Significance for Stakeholders:</b>  
# TRANSACTION_ID is expected to represent a unique service event. High duplication suggests that: The same service might have multiple repair records (sub-events under one transaction). Clarification is needed on whether this ID is supposed to be unique. Stakeholders should confirm the business logic to avoid inaccurate aggregation and analysis.

#   

# In[40]:


df['CORRECTION_VERBATIM'].value_counts()

#df['CORRECTION_VERBATIM'].describe()


#   

# <b>Column: CORRECTION_VERBATIM</b>  
# Data Type: object (string)  
# Unique Values: 93 unique out of 100  
# Duplicated Values: 7 entries are repeated  
# Distribution: Primarily unique descriptions of repairs, with a few recurring phrases like "REPLACED STEERING WHEEL"
# 
# <b>Significance for Stakeholders:</b>  
# Represents the technician’s input on the fix performed. It’s critical for:  
# Identifying common fixes and recurring issues  
# Enhancing maintenance documentation and standardization  
# Assisting warranty analysis and product improvement initiatives

# In[54]:


df['REPAIR_DATE'].duplicated().value_counts()

#df['REPAIR_DATE'].value_counts()


# <b>Column: REPAIR_DATE</b>  
# Data Type: datetime (or object, depending on parsing)  
# Unique Values: 29 unique out of 100  
# Duplicated Values: 71 repair dates are repeated  
# Distribution: High duplication indicates multiple repairs on the same day  
# 
# <b>Significance for Stakeholders:</b>
# Helps track repair frequency over time. Repeated dates may reveal peak service periods or batch servicing. Useful for planning resource allocation and identifying operational bottlenecks.

# In[58]:


#df['CUSTOMER_VERBATIM'].describe()
df['CUSTOMER_VERBATIM'].head()


# <b>Column: CUSTOMER_VERBATIM</b>  
# Data Type: object (string)  
# Unique Values: 100 unique out of 100  
# Duplicated Values: No duplicates – all values are unique  
# Distribution: Every record has a distinct customer statement
# 
# <b>Significance for Stakeholders:</b>  
# Captures the customer’s direct input or complaint in their own words. Useful for sentiment analysis, identifying recurring issues in natural language, and improving customer satisfaction through better service understanding.

# In[66]:


#df['CAUSAL_PART_NM'].head()
df['CAUSAL_PART_NM'].describe()
#df['CAUSAL_PART_NM'].duplicated().value_counts()


# <b>Column: CAUSAL_PART_NM</b>  
# Data Type: object (string)  
# Unique Values: 18 unique out of 95 non-null values  
# Duplicated Values: 77 values are repeated  
# Distribution: Highly skewed – one part name ("WHEEL ASM-STRG *JET BLACK") appears 45 times  
# 
# <b>Significance for Stakeholders:</b>  
# Indicates the part suspected to have caused the issue. The heavy skew toward one specific part suggests it may be a common failure point, which is critical for quality control, part redesign, or supplier evaluation.

# In[71]:


#df['GLOBAL_LABOR_CODE_DESCRIPTION'].tail()
df['GLOBAL_LABOR_CODE_DESCRIPTION'].describe()
#df['GLOBAL_LABOR_CODE_DESCRIPTION'].duplicated().value_counts()


# <b>Column: GLOBAL_LABOR_CODE_DESCRIPTION</b>  
# Data Type: object (string)  
# Unique Values: 4 unique out of 100  
# Duplicated Values: 96 values are repeated  
# Distribution: Highly concentrated – "Steering Wheel Replacement" appears 78 times
# 
# <b>Significance for Stakeholders:</b>  
# Captures the nature of labor performed. The dominance of one labor type signals recurring service needs, aiding in workforce training, labor time estimation, and identifying potential product or design flaws.

# In[76]:


#df['PLATFORM'].head()
df['PLATFORM'].describe()
#df['PLATFORM'].duplicated().value_counts()


# <b>Column: PLATFORM</b>  
# Data Type: object (string)  
# Unique Values: 11 unique out of 100  
# Duplicated Values: 89 values are repeated  
# Distribution: Skewed – "Full-Size Trucks" dominates with 52 occurrences
# 
# <b>Significance for Stakeholders:</b>  
# Identifies the vehicle platform, essential for segment-based analysis. Dominance of a specific platform can reveal focus areas for quality checks, platform-specific issues, or sales/service patterns. Helps target design improvements and resource planning.

# In[78]:


df['BODY_STYLE'].describe()
#df['BODY_STYLE'].duplicated().value_counts()


# <b>Column: BODY_STYLE</b>  
# Data Type: object (string)  
# Unique Values: 6 unique out of 100  
# Duplicated Values: 94 values are repeated  
# Distribution: Heavily skewed – "Crew Cab" appears 50% of the time
# 
# <b>Significance for Stakeholders:</b>  
# Defines vehicle body configuration, impacting design, manufacturing, and repair considerations. High concentration of "Crew Cab" suggests it’s a major variant and should be prioritized for quality reviews, inventory management, and targeted campaigns.

# In[79]:


df['VPPC'].describe()


# <b>Column: VPPC</b>  
# Data Type: object (string)  
# Unique Values: 26 unique out of 100  
# Duplicated Values: 74 values are repeated  
# Distribution: Moderate repetition, with “T1CCF” occurring most frequently (20 times)
# 
# <b>Significance for Stakeholders:</b>  
# VPPC (Vehicle Program Performance Code) helps categorize or track specific vehicle programs. Frequent occurrence of specific codes like “T1CCF” might indicate focus on certain vehicle lines, useful for warranty tracking, performance analytics, and quality management initiatives.

# In[80]:


df['PLANT'].describe()


# <b>Column: PLANT</b>  
# Data Type: object (string)  
# Unique Values: 11 unique out of 99 non-null entries  
# Missing Values: 1 missing entry  
# Duplicated Values: 88 values are repeated  
# Distribution: Fairly concentrated — “SIL” is the most common, appearing 19 times
# 
# <b>Significance for Stakeholders:</b>  
# Indicates the manufacturing plant where the vehicle was assembled. Frequent mentions of specific plants like “SIL” can help trace production issues, analyze quality trends, and optimize plant-level performance metrics. Missing plant info should be flagged for potential data quality improvement.

# In[81]:


df['BUILD_COUNTRY'].describe()


# <b>Column: BUILD_COUNTRY</b>
# Data Type: object (string)
# Unique Values: 3 unique out of 100
# Duplicated Values: 97 values are repeated
# Distribution: Heavily skewed toward "US" (73%)
# 
# <b>Significance for Stakeholders:</b>
# Identifies the country of manufacture, which can be essential for regulatory compliance, warranty tracking, and quality assurance. A dominant value like "US" indicates centralized production, while others could point to export or overseas assembly units. Useful for region-specific analysis.

# In[85]:


df['LAST_KNOWN_DLR_NAME'].describe()


# <b>Column: LAST_KNOWN_DLR_NAME</b>  
# Data Type: object (string)  
# Unique Values: 100 unique out of 100  
# Duplicated Values: None — all entries are unique  
# Distribution: Uniform, each dealer name appears once  
# 
# <b>Significance for Stakeholders:</b>  
# Captures the most recent dealership associated with the vehicle. Uniqueness suggests each record relates to a different dealership, enabling granular tracking of service networks. Valuable for analyzing dealer performance, geographic service coverage, and customer touchpoints.

# In[86]:


df['LAST_KNOWN_DLR_CITY'].describe()


# <b>Column: LAST_KNOWN_DLR_CITY</b>  
# Data Type: object (string)  
# Unique Values: 94 unique out of 100  
# Duplicated Values: 6 city names appear more than once (e.g., SMITHTOWN appears twice)  
# Distribution: Mostly unique cities with a few overlaps  
# 
# <b>Significance for Stakeholders:</b>  
# Indicates the city where the vehicle was last serviced. Useful for regional analysis of dealer locations, customer distribution, and identifying service clusters. Can help in optimizing service operations and planning regional dealership support.

# In[87]:


df['REPAIRING_DEALER_CODE'].describe()


# <b>Column: REPAIRING_DEALER_CODE</b>  
# Data Type: object (string)  
# Unique Values: 95 unique out of 100  
# Duplicated Values: 5 dealer codes are repeated, with the most frequent appearing 3 times  
# Distribution: Mostly unique with minor repetition in dealer codes  
# 
# <b>Significance for Stakeholders:</b>  
# Identifies the specific dealership responsible for performing repairs. Tracking this helps assess dealer performance, monitor frequent service centers, and flag patterns like recurring issues linked to specific dealers. Useful for warranty cost audits and service network optimization.

# In[88]:


df['DEALER_NAME'].describe()


# <b>Column: DEALER_NAME</b>  
# Data Type: object (string)  
# Unique Values: 100 unique out of 100  
# Duplicated Values: None  
# Distribution: All dealer names are unique in this dataset  
# 
# <b>Significance for Stakeholders:</b>  
# Represents the official name of the dealer handling the repair. Full uniqueness in this sample may imply a wide dealer network or isolated servicing instances. Enables identification of specific dealers in reporting, trend analysis, and accountability for service outcomes.

# In[89]:


df['REPAIR_DLR_CITY'].describe()


# <b>Column: REPAIR_DLR_CITY</b>  
# Data Type: object (string)  
# Unique Values: 93 unique out of 100  
# Duplicated Values: 7 city names are repeated  
# Distribution: Mostly unique cities with a few repeated entries like "GRAND RAPIDS" (appears 3 times)  
# 
# <b>Significance for Stakeholders:</b>  
# Identifies the city where each repair took place. Helps analyze geographic patterns in repair activity, detect city-level service volume trends, and optimize regional support. Repeated cities may indicate service hotspots or centralized operations.
# 

# In[90]:


df['STATE'].describe()


# <b>Column: STATE</b>  
# Data Type: object (string)  
# Unique Values: 39 unique out of 98 non-null entries  
# Duplicated Values: 59 states are repeated  
# Distribution: Moderate repetition, with "CA" being the most frequent (9 times)  
# 
# <b>Significance for Stakeholders:</b>  
# Represents the state where repairs occurred. Useful for analyzing regional service trends, allocating resources, and identifying high-demand states. Helps in geographic segmentation and identifying compliance or logistical challenges specific to states.

# In[98]:


df['DEALER_REGION'].tail()
#df['DEALER_REGION'].duplicated().value_counts()
#df['DEALER_REGION'].describe()


# <b>Column: DEALER_REGION</b>  
# Data Type: float64 (numeric)  
# Unique Values: Appears to be a small set (likely 1 to 4)  
# Distribution:  
# Mean: 1.09  
# Std Dev: 0.51  
# Min: 1, Max: 4  
# 75% of values are 1 → suggests heavy skew toward Region 1
# 
# <b>Significance for Stakeholders:</b>  
# Represents dealership region codes. The dominance of Region 1 may indicate a concentration of services in a specific area. Understanding regional distribution helps assess geographic coverage, service demand, and potential need for resource balancing.

# In[99]:


df['REPAIR_DLR_POSTAL_CD'].describe()


# <b>Column: REPAIR_DLR_POSTAL_CD</b>  
# Data Type: int64  
# Unique Values: 92 unique out of 98 non-null entries  
# Duplicated Values: 6 postal codes are repeated; one occurs 3 times  
# Distribution: Mostly unique, but some dealers share postal codes (e.g., 907551909)  
# 
# <b>Significance for Stakeholders:</b>  
# Postal code helps identify dealer locations at a granular level. Clustering of services in certain postal codes may highlight high-demand areas or dealer network overlap. Can support service coverage optimization and location-based performance analysis.

# In[105]:


#df['REPAIR_AGE'].describe()
df['REPAIR_AGE'].duplicated().value_counts()
#df['REPAIR_AGE'].isnull().sum()


# <b>Column: REPAIR_AGE</b>  
# Data Type: float64  
# Unique Values: 35 unique out of 100  
# Duplicated Values: 65 values are repeated  
# Missing Values: 2 missing (98 non-null)  
# Distribution:  
# Min: 0  
# Max: 50  
# Mean: 14.94  
# Median: 12  
# Std Dev: 12.37  
# Most values fall within 0–21 months range (IQR)  
# 
# <b>Significance for Stakeholders:</b>  
# Represents vehicle age (in months) at the time of repair. Useful to identify failure patterns over vehicle lifecycle. High duplication suggests common repair ages, which may point to predictable failure windows. Valuable for warranty planning, improving component lifespan, and proactive customer outreach.

# In[106]:


#df['KM'].describe()
#df['KM'].duplicated().value_counts()


# <b>Column: KM</b>  
# Data Type: float64  
# Unique Values: Assumed 100 (since count = 100, likely all unique)  
# Distribution:  
# Min: 3 km  
# Max: 107,905 km  
# Mean: 24,914 km  
# Median (50%): 21,962 km  
# Std Dev: 20,747  
# IQR: 26,610 (75% = 35,493.25, 25% = 8,883.25)  
# 
# <b>Significance for Stakeholders:</b>  
# Represents the vehicle mileage at the time of repair. High mileage may reflect wear-and-tear issues, while low mileage repairs could point to quality or early-life failures. Helps in correlating issues with usage intensity and planning for warranty, service intervals, and failure prediction models.

# In[112]:


df['COMPLAINT_CD_CSI'].describe()
#df['COMPLAINT_CD_CSI'].head()
#df['COMPLAINT_CD_CSI'].duplicated().value_counts()
#df['COMPLAINT_CD_CSI'].isnull().sum()


# <b>Column: COMPLAINT_CD_CSI</b>  
# Data Type: float64  
# Unique Values: 1 unique value (0.0) out of 100  
# Duplicated Values: 99 values are repeated (all are 0.0)  
# Distribution: Constant – all values are 0.0  
# 
# <b>Significance for Stakeholders:</b>  
# This column appears to be unused or deprecated, as all values are 0.0. It currently holds no variance or analytical value. Stakeholders can consider omitting it from reporting unless future data captures meaningful entries.

# In[113]:


df['COMPLAINT_CD'].describe()


# <b>Column: COMPLAINT_CD</b>  
# Data Type: object (string)  
# Unique Values: 7 unique values out of 100  
# Duplicated Values: 93 complaint codes are repeated  
# Distribution: Highly skewed — top value '0-0890' appears 40 times, indicating a dominant complaint category  
# 
# <b>Significance for Stakeholders:</b>  
# This field categorizes customer complaints, which is crucial for identifying recurring product issues. The dominance of certain codes like '0-0890' can signal systemic issues requiring prioritization. It’s valuable for quality assurance, product improvement, and customer service strategy.

# In[114]:


df['VEH_TEST_GRP'].describe()


# <b>Column: VEH_TEST_GRP</b>  
# Data Type: object (string)  
# Unique Values: 23 unique values out of 98 non-null entries  
# Duplicated Values: 75 entries are repeated  
# Distribution: Certain test groups like 'T05.3386' are dominant (appearing 19 times), while many others are less frequent  
# 
# <b>Significance for Stakeholders:</b>  
# Indicates the vehicle test group classification, which helps in linking complaints or repairs to specific vehicle test batches or configurations. Repetition may reflect common issues in particular groups, aiding engineering and manufacturing teams in identifying patterns across production batches.

# In[115]:


df['COUNTRY_SALE_ISO'].describe()


# <b>Column: COUNTRY_SALE_ISO</b>  
# Data Type: object (string)  
# Unique Values: 6 unique out of 100  
# Duplicated Values: 94 entries are repeated  
# Distribution: Highly skewed — 'US' dominates with 84 occurrences  
# 
# <b>Significance for Stakeholders:</b>  
# Shows the country where the vehicle was sold. The dominance of 'US' may indicate the dataset’s regional focus. Understanding distribution by country helps stakeholders identify region-specific trends in vehicle issues or customer feedback, aiding in targeted service or recall strategies.

# In[119]:


#df['ORD_SELLING_SRC_CD'].describe()
df['ORD_SELLING_SRC_CD'].duplicated().value_counts()


# <b>Column: ORD_SELLING_SRC_CD</b>  
# Data Type: float64 (numerical)  
# Unique Values: 7 unique out of 100  
# Duplicated Values: 93 values are repeated  
# Distribution: Highly duplicated with a right-skewed distribution – most values are clustered at the lower end, with a few high outliers (mean = 24.59, max = 72)  
# 
# <b>Significance for Stakeholders:</b>  
# Represents the order selling source code, which may correlate with sales channels or distribution pathways. The repetition suggests concentration in a few channels. Analyzing these can help identify performance or issue patterns linked to specific sources, allowing for targeted improvements in sales strategy or service support.

# In[120]:


df['OPTN_FAMLY_CERTIFICATION'].describe()


# <b>Column: OPTN_FAMLY_CERTIFICATION</b>  
# Data Type: object (string)  
# Unique Values: 3 unique out of 90 non-null entries  
# Duplicated Values: 87 values are repeated  
# Distribution: Heavily skewed towards 'FE9' (62 occurrences), suggesting it's the most common certification option  
# 
# <b>Significance for Stakeholders:</b>  
# Indicates the vehicle's certification family, likely tied to emissions or compliance standards. The dominance of 'FE9' shows a standardized  certification type across vehicles. Useful for compliance tracking, market segmentation, or regional certification analysis. The missing values (10%) may need review for data completeness.

# In[121]:


df['OPTF_FAMLY_EMISSIOF_SYSTEM'].describe()


# <b>Column: OPTF_FAMLY_EMISSIOF_SYSTEM</b>  
# Data Type: object (string)  
# Unique Values: 8 unique out of 95 non-null entries  
# Duplicated Values: 87 values are repeated  
# Distribution: Strongly skewed toward 'FTB' (62 occurrences), showing a dominant emission system type  
# 
# <b>Significance for Stakeholders:</b>  
# Represents the emission system configuration associated with the vehicle. A high frequency of 'FTB' suggests standardization in emission systems, which can aid in regulatory reporting and performance tracking. The 5 missing values may indicate data entry issues or incomplete documentation.

# In[123]:


#df['GLOBAL_LABOR_CODE'].describe()
df['GLOBAL_LABOR_CODE'].duplicated().value_counts()


# <b>Column: GLOBAL_LABOR_CODE</b>  
# Data Type: float64 (numeric)  
# Unique Values: 4 unique out of 100  
# Duplicated Values: 96 values are repeated  
# Distribution: Highly repetitive — most values are clustered at specific labor codes (e.g., 130), with a few outliers like 2400 indicating intensive labor
# 
# <b>Significance for Stakeholders:</b>  
# Represents standard labor effort for specific repair types. High duplication implies consistent repair types, helping in labor cost estimation and process optimization. Outliers could signal special repairs or data entry inconsistencies worth further review.

# In[124]:


df['TRANSACTION_CATEGORY'].describe()


# <b>Column: TRANSACTION_CATEGORY</b>  
# Data Type: object (categorical)  
# Unique Values: 2 unique out of 100  
# Duplicated Values: 98 values are repeated (based on 2 categories)  
# Distribution: Highly skewed — 'FREG' appears 89 times, indicating it is the dominant transaction type  
# 
# <b>Significance for Stakeholders:</b>  
# This field categorizes the nature of repair transactions. The dominance of one category ('FREG') may reflect a standardized type of service or warranty-related repairs. Analyzing the minority category can reveal exceptional or special-case transactions.

# In[126]:


#df['CAMPAIGN_NBR'].describe()
df['CAMPAIGN_NBR'].duplicated().value_counts()


# <b>Column: CAMPAIGN_NBR</b>  
# Data Type: float64 (likely due to all nulls or a placeholder type)  
# Unique Values: 0 non-null values (entire column is empty)  
# Duplicated Values: 99 duplicated nulls, 1 first-occurrence null  
# Distribution: No valid data; all entries are missing (NaN)  
# 
# <b>Significance for Stakeholders:</b>  
# Currently, this field holds no actionable data. It might be a placeholder for future campaign tracking or represents missing data in the current extract. 

# In[130]:


#df['REPORTING_COST'].describe()
df['REPORTING_COST'].duplicated().value_counts()


# <b>Column: REPORTING_COST</b>  
# Data Type: float64  
# Unique Values: 100 unique values out of 100 entries  
# Distribution:  
# Mean: 531.19  
# Median (50%): 433.97  
# Min: 27.69  
# Max: 2457.45  
# Standard Deviation: 411.16  
# 
# <b>Significance for Stakeholders:</b>  
# Represents the cost associated with each repair record. Uniqueness of values suggests highly specific cost data, likely influenced by labor, parts, or location. Useful for financial forecasting, identifying high-cost repairs, and flagging anomalies. Patterns in cost can help optimize service strategies and reduce unnecessary expenses.

# In[131]:


df['TOTALCOST'].describe()


# <b>Column: TOTALCOST</b>  
# Data Type: float64  
# Non-Null Entries: 94 out of 100  
# Unique Values: Not explicitly stated, but likely high due to continuous nature  
# Distribution:  
# Mean: 561.16
# Median (50%): 457.23
# Min: 27.69
# Max: 3205.45
# Standard Deviation: 452.80
# 
# <b>Significance for Stakeholders:</b>  
# Indicates the overall cost incurred per repair, including labor, parts, and any additional service charges. Useful for cost benchmarking, budgeting, and ROI analysis. High-cost repairs might require investigation or process optimization. Missing values (6 entries) may suggest incomplete billing or reporting.

# In[132]:


df['LBRCOST'].describe()


# <b>Column: LBRCOST</b>  
# Data Type: float64  
# Non-Null Entries: 100 out of 100  
# Distribution:  
# Mean: 106.34  
# Median (50%): 78.56  
# Min: 20.00  
# Max: 1012.67  
# Standard Deviation: 113.22  
# 
# <b>Significance for Stakeholders:</b>  
# Represents the labor cost component of the total repair expense. Critical for evaluating technician efficiency, service pricing strategy, and cost optimization. High variance may indicate inconsistency in service hours or labor rates across dealers and locations.

# In[133]:


df['ENGINE'].describe()


# <b>Column: ENGINE</b>  
# Data Type: object (categorical)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 12  
# Most Frequent Value: L84 (appears 24 times)  
# Distribution: Some engines are far more common than others (e.g., L84)  
# 
# <b>Significance for Stakeholders:</b>  
# Engine type can influence the nature of repairs and associated costs. Certain engines might be more prone to specific issues, making this data valuable for predictive maintenance, root cause analysis, and targeting technical service bulletins (TSBs). Helps engineering and product quality teams monitor engine-specific patterns.

# In[134]:


df['ENGINE_DESC'].describe()


# <b>Column: ENGINE_DESC</b>  
# Data Type: object (categorical)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 12  
# Most Frequent Value: GAS, 8 CYL, 5.3L, V8, DI, DFM, ALUM, GEN 5 (appears 24 times)  
# Distribution: Skewed — one engine description appears nearly a quarter of the time  
# 
# <b>Significance for Stakeholders:</b>  
# Detailed engine descriptions help pinpoint technical configurations linked with recurring issues. Useful for engineering teams to trace issues to specific builds or generations. Aids service and parts teams in identifying compatibility and stocking the right components.
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[135]:


df['TRANSMISSION'].describe()


# <b>Column: TRANSMISSION</b>  
# Data Type: object (categorical)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 19  
# Most Frequent Value: MHS (appears 28 times)  
# Distribution: Skewed — top value accounts for 28% of the entries  
# 
# <b>Significance for Stakeholders:</b>  
# Identifying the most common transmission types helps link specific transmission models with recurring repair trends. Useful for diagnosing model-specific issues and informing warranty strategies, supplier performance reviews, and inventory planning.

# In[136]:


df['TRANSMISSION_DESC'].describe()


# <b>Column: TRANSMISSION_DESC</b>  
# Data Type: object (categorical)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 20  
# Most Frequent Value: BYT 10 SPD, 10L80, GRX, GEN 1, ATSS, ETRS, VAR 1 (28 occurrences)  
# Distribution: Moderately skewed — one description dominates over a quarter of entries  
# <b>Significance for Stakeholders:</b>  
# Detailed transmission descriptions allow for granular diagnostics and trend analysis. High frequency of a specific configuration may correlate with recurring issues or repair types, aiding in root cause analysis, parts stocking strategies, and supplier quality assessments.

# In[137]:


df['ENGINE_SOURCE_PLANT'].describe()


# <b>Column: ENGINE_SOURCE_PLANT</b>  
# Data Type: object (categorical)  
# Non-Null Entries: 88 out of 100  
# Unique Values: 9  
# Most Frequent Value: 830107152 (15 occurrences)  
# Missing Values: 12  
# 
# <b>Significance for Stakeholders:</b>  
# This column identifies where the engine was manufactured. Frequent repairs associated with a particular source plant could highlight quality control or manufacturing issues. Understanding plant-level performance enables targeted interventions, enhances supplier accountability, and improves overall vehicle reliability.

# In[138]:


df['ENGINE_TRACE_NBR'].describe()


# <b>Column: ENGINE_TRACE_NBR</b>  
# Data Type: object  
# Non-Null Entries: 88 out of 100  
# Unique Values: 88  
# Most Frequent Value: V2210281MFTX0488 (only appears once)  
# Missing Values: 12  
# 
# <b>Significance for Stakeholders:</b>  
# This is a unique engine identifier, likely used for tracking and traceability during manufacturing, warranty, or service processes. Although it's not useful for aggregation or statistical analysis, it is crucial for:  
# Root cause analysis in recalls or failures.
# Traceability in quality audits and supplier accountability.
# Linking repair records to specific engines across datasets.
# For analysis, you’d typically not use this in modeling but keep it for reference or merging with other technical records.

# In[141]:


#df['TRANSMISSION_SOURCE_PLANT'].describe()
df['TRANSMISSION_SOURCE_PLANT'].duplicated().value_counts()


# <b>Column: TRANSMISSION_SOURCE_PLANT</b>  
# Data Type: float64 (numeric identifier)  
# Non-Null Entries: 88 out of 100  
# Unique Values: 7  
# Most Frequent Value: 287827.0 (appears frequently in lower quartiles)  
# Missing Values: 12  
# 
# <b>Significance for Stakeholders:</b>  
# This likely represents a coded identifier for the plant where the transmission was manufactured. While not directly meaningful for statistical trends, it's important for:  
# Supply chain traceability and manufacturing lineage
# Identifying defect patterns linked to specific plants
# Auditing and compliance tracking in case of regional or plant-based performance issues
# Enhancing root cause investigations across plant-level operations

# In[142]:


df['TRANSMISSION_TRACE_NBR'].describe()


# <b>Column: TRANSMISSION_TRACE_NBR</b>  
# Data Type: object (identifier)  
# Non-Null Entries: 88 out of 100  
# Unique Values: 88  
# Most Frequent Value: S2210121CNJX0941 (only appears once)  
# Missing Values: 12  
#  
# <b>Significance for Stakeholders:</b>  
# This is a unique identifier for each transmission unit, likely used for traceability in manufacturing and post-sales processes. Though not useful for numerical analysis or aggregation, it serves critical roles in:
# Tracing individual transmission units for quality control or failure analysis
# Supporting warranty validation and historical tracking of parts
# Linking service records back to specific units for better lifecycle insights
# Root cause investigations during defect clustering or plant performance reviews

# In[146]:


#df['SRC_TXN_ID'].describe()
df['SRC_TXN_ID'].duplicated().value_counts()


# <b>Column: SRC_TXN_ID</b>  
# Data Type: float64 (numeric identifier)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 100  
# Most Frequent Value: All values are unique  
# Missing Values: 0  
# 
# <b>Significance for Stakeholders:</b>  
# This appears to be a transaction-level unique identifier, likely assigned to each service or repair transaction. While not used for statistical summarization, it plays a crucial role in:  
# Maintaining data integrity when merging or joining multiple datasets  
# Audit trails and traceability for service or repair events  
# Enabling drill-downs in dashboards or transaction-level inspection in reports  
# Ensuring referential integrity in relational database designs

# In[149]:


#df['SRC_VER_NBR'].describe()
df['SRC_VER_NBR'].duplicated().value_counts()


# <b>Column: SRC_VER_NBR</b>  
# Data Type: float64 (version number)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 10  
# Most Frequent Value: Multiple values with varying frequencies  
# Missing Values: 0  
# Duplicate Entries: 90  
# 
# <b>Significance for Stakeholders:</b>  
# This field likely represents a source system version number, useful for identifying which version of a system or data model the transaction originated from. It can support:  
# Troubleshooting discrepancies across system versions  
# Ensuring backward compatibility in analytics and reporting pipelines

# In[150]:


#df['TRANSACTION_CNTR'].describe()
df['TRANSACTION_CNTR'].describe()


# <b>Column: TRANSACTION_CNTR</b>  
# Data Type: float64 (constant numeric value)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 1  
# Most Frequent Value: 1.0 (appears 100 times)  
# Missing Values: 0  
# Duplicate Entries: 99  
# 
# <b>Significance for Stakeholders:</b>  
# This column contains a constant value (1.0) for every row, suggesting it might be a placeholder or default counter.  
# Low analytical value in its current state due to lack of variability  
# Should be validated—if it's redundant, it can be excluded from analytical models to reduce noise  

# In[151]:


df['MEDIA_FLAG'].describe()


# <b>Column: MEDIA_FLAG</b>  
# Data Type: object (categorical)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 2  
# Most Frequent Value: 'N' (appears 62 times)  
# Missing Values: 0  
# 
# <b>Significance for Stakeholders:</b>  
# MEDIA_FLAG likely indicates whether a particular record or transaction involves media (e.g., video evidence, documentation, or marketing materials).
# Helps segment records based on media involvement, which may affect processing times, costs, or quality review.
# Useful for filtering records for compliance, legal review, or customer support cases.
# If tied to repair or service events, can help analyze the impact of documentation/media availability on resolution effectiveness.

# In[152]:


df['VIN_MODL_DESGTR'].describe()


# <b>Column: VIN_MODL_DESGTR</b>  
# Data Type: object (categorical/model identifier)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 41  
# Most Frequent Value: 'CF10543' (appears 15 times)  
# Missing Values: 0  
# 
# <b>Significance for Stakeholders:</b>  
# This column likely represents a Vehicle Identification Number (VIN) model designator, which encodes specific information about the model configuration.
# Essential for product performance analysis, recalls, and warranty tracking based on specific vehicle builds.

# In[153]:


df['LINE_SERIES'].describe()


# <b>Column: LINE_SERIES</b>  
# Data Type: object (categorical)  
# Non-Null Entries: 99 out of 100  
# Unique Values: 22  
# Most Frequent Value: '1500' (appears 52 times)  
# Missing Values: 1  
# 
# <b>Significance for Stakeholders:</b>  
# The LINE_SERIES column likely represents the product line or series of the vehicle.
# Important for segmenting data based on vehicle classification or market segment.
# Valuable for forecasting demand, managing inventory of parts, or planning production schedules based on series popularity.

# In[155]:


#df['LAST_KNOWN_DELVRY_TYPE_CD'].describe()
df['LAST_KNOWN_DELVRY_TYPE_CD'].duplicated().value_counts()


# <b>Column: LAST_KNOWN_DELVRY_TYPE_CD</b>  
# Data Type: float64 (categorical code, likely numeric representation)  
# Non-Null Entries: 98 out of 100  
# Unique Values: 12  
# Most Frequent Value: 10.0 (appears most frequently – inferred from median and mode alignment)  
# Missing Values: 2  
# Duplicate Values: 88 out of 98 (frequent repetition)  
# 
# <b>Significance for Stakeholders:</b>  
# This column likely represents the delivery type classification (e.g., type of customer delivery or logistics method), encoded as numbers.  
# Useful for logistics and operations teams to analyze delivery patterns and performance.  
# Helps identify the most common delivery types and their relationship to service issues or complaints.  
# Can be used for optimization of delivery strategies or further mapping to descriptive labels for business insights.  

# In[156]:


df['NON_CAUSAL_PART_QTY'].describe()


# <b>Column: NON_CAUSAL_PART_QTY</b>  
# Data Type: float64 (quantitative, binary-like values)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 2 (0.0 and 1.0)  
# Most Frequent Value: 0.0  
# Missing Values: 0  
# Duplicate Values: Highly duplicated (most values are 0.0)  
# 
# <b>Significance for Stakeholders:</b>  
# This column likely indicates whether non-causal parts were involved in a service or warranty repair (e.g., parts not directly responsible for the failure but replaced anyway).
# Useful for warranty analysis teams to measure the frequency of non-causal part replacements.
# Can help in cost analysis to identify unnecessary or preventive part replacements.
# Supports root cause investigations and optimization of repair guidelines or technician behavior.

# In[157]:


df['SALES_REGION_CODE'].describe()


# <b>Column: SALES_REGION_CODE</b>  
# Data Type: float64 (categorical as number codes)  
# Non-Null Entries: 100 out of 100  
# Unique Values: 4  
# Most Frequent Value: 1.0  
# Missing Values: 0  
# Duplicate Values: Yes (most values are 1.0; duplicates are present)  
# 
# <b>Significance for Stakeholders:</b>  
# This field likely represents the sales region classification code, grouping records based on geographic or organizational sales territories.
# Important for regional performance tracking and sales analysis.  

# ***

# # Data Cleaning

# In[186]:


df.isnull().sum()


# In[187]:


#Completely null. Hence, dropped.
df.drop(columns=['CAMPAIGN_NBR'], inplace=True)


# In[188]:


cat_cols_to_fill = ['CAUSAL_PART_NM', 'PLANT', 'STATE', 'REPAIR_DLR_POSTAL_CD','VEH_TEST_GRP', 'OPTN_FAMLY_CERTIFICATION', 'OPTF_FAMLY_EMISSIOF_SYSTEM',
    'ENGINE_SOURCE_PLANT', 'ENGINE_TRACE_NBR','TRANSMISSION_SOURCE_PLANT', 'TRANSMISSION_TRACE_NBR']
for col in cat_cols_to_fill:
    df[col] = df[col].fillna('UNKNOWN')


# In[189]:


# Fill numeric columns
df['TOTALCOST'] = df['TOTALCOST'].fillna(0)
df['LINE_SERIES'] = df['LINE_SERIES'].fillna(df['LINE_SERIES'].mode()[0])
df['LAST_KNOWN_DELVRY_TYPE_CD'] = df['LAST_KNOWN_DELVRY_TYPE_CD'].fillna(df['LAST_KNOWN_DELVRY_TYPE_CD'].mode()[0])


# In[190]:


df.isnull().sum()


# In[191]:


categorical_cols = ['STATE', 'PLANT', 'BUILD_COUNTRY', 'LAST_KNOWN_DLR_NAME', 'DEALER_NAME', 'REPAIR_DLR_CITY', 'VEH_TEST_GRP', 'PLATFORM', 'BODY_STYLE',
    'LINE_SERIES', 'VIN_MODL_DESGTR', 'MEDIA_FLAG', 'DEALER_REGION']

for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip().str.upper()


# In[192]:


for col in categorical_cols:
    print(f"\nColumn: {col}")
    print(df[col].value_counts(dropna=False))


# In[193]:


df['PLATFORM'] = df['PLATFORM'].replace({'GLOBAL GAMMA VEHICLES': 'GLOBAL GAMMA', 'GLOBAL CROSSOVER VEHICLES': 'CROSSOVER SUV', 'LUXURY CAR-2': 'LUXURY CAR',
    'LUXURY CAR-3': 'LUXURY CAR'})


# In[194]:


df['LINE_SERIES'] = df['LINE_SERIES'].replace({
    '1LT': 'LT',
    '2LT': 'LT',
    'LT(AUTOMATIC)': 'LT',
    '1SS(AUTOMATIC)': 'SS',
    'PREMIUM LUXURY': 'LUXURY SERIES',
    'PREMIER': 'LUXURY SERIES',
    'LUX-1': 'LUXURY SERIES',
    'LUXURY': 'LUXURY SERIES'})


# In[195]:


import numpy as np

df['STATE'] = df['STATE'].replace('UNKNOWN', np.nan)
df['PLANT'] = df['PLANT'].replace('UNKNOWN', np.nan)
df['VEH_TEST_GRP'] = df['VEH_TEST_GRP'].replace('UNKNOWN', np.nan)


# In[196]:


df.dtypes


# Numerical Columns are either int64 or float64

# In[197]:


df.shape


# In[198]:


numerical_cols = ['KM', 'REPAIR_AGE', 'REPORTING_COST', 'TOTALCOST', 'LBRCOST']
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"{col}: {len(outliers)} to be removed")

    # Free from the outliers
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]


# In[199]:


df.shape


# # Identifying Critical Columns:

# <b>IMPORTANT FEATURES FOR STAKEHOLDERS</b> 
# 
# 
# * <b> REPAIR_AGE</b>	Indicates vehicle age at time of repair – useful for trend analysis over vehicle lifecycle.  
# * <b>TOTALCOST</b>	Shows the overall cost – essential for cost analysis and budgeting.  
# * <b>STATE</b>	Helps in identifying region-wise issues or hotspots.  
# * <b>VEH_TEST_GRP</b>	Relates to the test group or variant of vehicle – good for product-level insights.  
# * <b>COMPLAINT_CD</b>	Tells the nature/type of complaint – helps in identifying common failure areas.

# In[201]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[207]:


top_complaints = df['COMPLAINT_CD'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_complaints.values, y=top_complaints.index, palette='Set2', hue=top_complaints.index, legend=False)
plt.title('Top 10 Complaint Types')
plt.xlabel('Number of Complaints')
plt.ylabel('Complaint Code')
plt.tight_layout()
plt.show()


# As Described earlier as well in column wise analysis:
# Distribution: Highly skewed — top value '0-0890' appears 40 times, indicating a dominant complaint category
# This field categorizes customer complaints, which is crucial for identifying recurring product issues. The dominance of certain codes like '0-0890' can signal systemic issues requiring prioritization. It’s valuable for quality assurance, product improvement, and customer service strategy.

# In[209]:


top_states = df['STATE'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='colorblind', hue=top_states.index, legend=False)
plt.title('Top 10 States by Repair Volume')
plt.xlabel('Number of Repairs')
plt.ylabel('State')
plt.show()


# <b>Before removing outliers:</b>  
# California (CA) might have had many extremely high-cost repairs, which inflated its average or overall impact in cost-related charts.  
# <b>After removing outliers:</b>  
# Those very high repair costs from CA were likely removed as outliers  
# <b> Meanwhile, states like FL and OH, which might have had more consistent but high mid-range costs, now appear more prominent.</b>

# In[212]:


avg_cost_by_state = df.groupby('STATE')['TOTALCOST'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=avg_cost_by_state.index, y=avg_cost_by_state.values, palette='coolwarm', hue=avg_cost_by_state.values, legend=False)
plt.title('Average Total Cost by State')
plt.xlabel('State')
plt.ylabel('Average Total Cost')
plt.xticks(rotation=45)
plt.show()


# NY has been top state with highest- average Total cost repairs after removal of outliers.  
# Useful for cost benchmarking, budgeting, and ROI analysis. High-cost repairs might require investigation or process optimization  

# # Generating tags from free text available

# In[213]:


df['CUSTOMER_VERBATIM'].dropna().sample(10, random_state=1)


# In[214]:


df['CORRECTION_VERBATIM'].dropna().sample(10, random_state=1)


# In[215]:


import re


# In[216]:


def extract_tags(text, keywords):
    if pd.isna(text):
        return []
    return [kw for kw in keywords if re.search(rf'\b{re.escape(kw)}\b', text.lower())]


# In[217]:


component_keywords = ['steering wheel', 'switch', 'horn', 'wire harness', 'cover', 'leather', 'applique']
condition_keywords = ['not heating', 'loose', 'peeling', 'open circuit', 'inoperable', 'replace', 'replacement', 'diagnosis', 'bulletin']


# In[218]:


df['COMPONENT_TAGS'] = df['CUSTOMER_VERBATIM'].apply(lambda x: extract_tags(x, component_keywords))
df['CONDITION_TAGS'] = df['CUSTOMER_VERBATIM'].apply(lambda x: extract_tags(x, condition_keywords))


# In[219]:


df['ALL_TAGS'] = df.apply(lambda row: list(set(
    extract_tags(str(row['CUSTOMER_VERBATIM']), component_keywords + condition_keywords) +
    extract_tags(str(row['CORRECTION_VERBATIM']), component_keywords + condition_keywords)
)), axis=1)


# In[222]:


print(df['ALL_TAGS'])


# In[224]:


df['ALL_TAGS'] = df['ALL_TAGS'].apply(lambda x: ', '.join(x))


# In[225]:


df.to_excel('cleaned_tagged_data.xlsx', index=False)


# In[ ]:




