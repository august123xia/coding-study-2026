-- Day 13 SQL Validation
-- Validate Pandas-generated overdue customer summary

DROP TABLE IF EXISTS overdue_report;

CREATE TABLE overdue_report (
    invoice_id INTEGER,
    customer TEXT,
    amount INTEGER,
    status TEXT,
    invoice_date TEXT,
    due_date TEXT,
    days_overdue INTEGER,
    aging_bucket TEXT
);

.mode csv
.import --skip 1 ../../projects/ar_invoice_cleaner/data/overdue_report.csv overdue_report

.headers on
.mode column

SELECT
    customer,
    SUM(amount) AS overdue_total
FROM overdue_report
GROUP BY customer
ORDER BY overdue_total DESC;