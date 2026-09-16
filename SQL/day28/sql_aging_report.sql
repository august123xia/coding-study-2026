DROP TABLE IF EXISTS invoices;

CREATE TABLE invoices (
    invoice_id INTEGER,
    customer TEXT,
    amount INTEGER,
    status TEXT,
    invoice_date TEXT,
    due_date TEXT
);

INSERT INTO invoices VALUES
(1, 'Google', 1200, 'paid', '2026-07-01', '2026-07-31'),
(2, 'Amazon', 3500, 'unpaid', '2026-06-15', '2026-07-15'),
(3, 'Ali', 800, 'unpaid', '2026-08-01', '2026-08-31'),
(4, 'Canva', 2200, 'paid', '2026-07-10', '2026-08-09'),
(5, 'Dnata', 5000, 'unpaid', '2026-05-01', '2026-05-31'),
(6, 'Google', 1800, 'unpaid', '2026-07-20', '2026-08-19'),
(7, 'Amazon', 2700, 'paid', '2026-08-05', '2026-09-04');

SELECT
    invoice_id,
    customer,
    amount,
    status,
    due_date,
    CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) AS days_overdue,
    CASE
        WHEN CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) < 0 THEN 'Not due'
        WHEN CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) <= 30 THEN '0-30 days'
        WHEN CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) <= 60 THEN '31-60 days'
        WHEN CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) <= 90 THEN '61-90 days'
        ELSE '90+ days'
    END AS aging_bucket
FROM invoices
WHERE status = 'unpaid'
AND CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) > 0
ORDER BY days_overdue DESC;



SELECT
    CASE
        WHEN CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) < 0 THEN 'Not due'
        WHEN CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) <= 30 THEN '0-30 days'
        WHEN CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) <= 60 THEN '31-60 days'
        WHEN CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) <= 90 THEN '61-90 days'
        ELSE '90+ days'
    END AS aging_bucket,
    COUNT(*) AS invoice_count,
    SUM(amount) AS total_amount
FROM invoices
WHERE status = 'unpaid'
AND CAST(julianday('2026-08-27') - julianday(due_date) AS INTEGER) > 0
GROUP BY aging_bucket
ORDER BY total_amount DESC;




SELECT 
    customer,
    COUNT(*) AS overdue_count,
    SUM(amount) AS total_overdue,
    CASE 
        WHEN  SUM(amount) >= 5000 THEN 'high'
        WHEN  SUM(amount) > 3000 THEN 'medium'
        ELSE  'low'
    END AS priority

FROM invoices
WHERE status = 'unpaid'
AND CAST(julianday('2026-09-16') - julianday(due_date) AS INTEGER) > 0
GROUP BY customer
ORDER BY total_overdue DESC

-- Review:
-- WHERE filters original invoice rows before grouping.
-- status = 'unpaid' keeps unpaid invoices only.
-- days_overdue > 0 keeps overdue invoices only.
-- GROUP BY customer summarizes overdue invoices by customer.
-- COUNT(*) counts overdue invoices for each customer.
-- SUM(amount) calculates total overdue amount for each customer.
-- CASE WHEN creates a priority level based on total_overdue.
-- HAVING is used only when filtering grouped results such as SUM(amount).
