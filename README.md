# Customer Processor – Python Data Validation Pipeline

## Project Overview

<img width="1447" height="699" alt="image" src="https://github.com/user-attachments/assets/be5fcbd1-0978-4330-a6e7-7441c0842f56" />

Customer Processor is a Python-based batch data processing pipeline that ingests customer records from a CSV file provided by an external partner system, validates and enriches the data, separates valid and invalid records, logs detailed validation failures, and produces clean output for downstream systems.

The project is designed using **backend engineering best practices**:
- Clear separation of concerns
- Robust exception handling
- Strong observability via logging and metrics
- No external dependencies (Python standard library only)

---

##  Problem Statement

- Receive a CSV file containing customer records
- Data may be invalid, incomplete, or malformed
- Validate each record using configurable rules
- Separate valid and invalid records
- Persist clean data and log detailed errors
- Provide visibility into why data fails

---

##  Project Structure

```
Customer_processor/
├── config.py        # paths and validation rules (single source of truth)
├── logger.py        # sets up file logging once (errors.log)
├── reader.py        # safe CSV reading (returns list/dict rows)
├── validator.py     # pure validation logic for one record (returns error list)
├── writer.py        # writes valid records to clean_data.csv
├── processor.py     # orchestration: read → validate → enrich → collect → write
├── main.py          # user entry point + interactive menu & reporting
├── customers.csv    # input (test/sample)
├── clean_data.csv   # output (valid rows)
└── errors.log       # output (logged invalid rows + reasons)
```

---
## Sample Screenshots

<img width="1074" height="774" alt="image" src="https://github.com/user-attachments/assets/0671889b-9c9e-4830-802a-1c9992d1edf1" />
<img width="723" height="732" alt="image" src="https://github.com/user-attachments/assets/a5e5edb9-3be6-45a2-8b5b-f0dec37c613e" />
<img width="1035" height="768" alt="image" src="https://github.com/user-attachments/assets/36a424f4-fc76-4cf9-b83f-5e5ab9c9c28d" />
<img width="1039" height="365" alt="image" src="https://github.com/user-attachments/assets/244efb7f-b6e4-49e3-9b2a-fb7fafe907ac" />

