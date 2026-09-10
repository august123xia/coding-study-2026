DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS invoices;

CREATE TABLE customers (
    customer_id INTEGER,
    customer_name TEXT,
    country TEXT
);

CREATE TABLE invoices (
    invoice_id INTEGER,
    customer_id INTEGER,
    amount INTEGER,
    status TEXT
);

INSERT INTO customers VALUES
(1, 'Google', 'USA'),
(2, 'Amazon', 'USA'),
(3, 'Dnata', 'Australia'),
(4, 'Canva', 'Australia'),
(5, 'Apple', 'USA');

INSERT INTO invoices VALUES
(101, 1, 1200, 'paid'),
(102, 1, 1800, 'unpaid'),
(103, 2, 3500, 'unpaid'),
(104, 3, 5000, 'unpaid'),
(105, 5, 900, 'paid');

SELECT
    customers.customer_name,
    SUM(invoices.amount) AS total_amount
FROM customers
LEFT JOIN invoices
ON customers.customer_ID = invoices.customer_id
GROUP BY customers.customer_name
ORDER BY total_amount  DESC;

SELECT
    customers.customer_name,
    COALESCE(SUM(invoices.amount), 0) AS total_amount
FROM customers
LEFT JOIN invoices
ON customers.customer_id = invoices.customer_id
GROUP BY customers.customer_name
ORDER BY total_amount DESC;

SELECT
    customers.customer_name,
    COALESCE(SUM(invoices.amount), 0) AS total_amount,
    CASE
        WHEN COALESCE(SUM(invoices.amount), 0) >= 5000 THEN 'High'
        WHEN COALESCE(SUM(invoices.amount), 0) >= 1000 THEN 'Medium'
        ELSE 'Low'
    END AS customer_priority
FROM customers
LEFT JOIN invoices
ON customers.customer_id = invoices.customer_id
GROUP BY customers.customer_name
ORDER BY total_amount DESC;

-- Review:
-- COALESCE(value, 0) replaces NULL with 0.
-- LEFT JOIN may produce NULL when the right table has no matching row.
-- CASE WHEN creates a new calculated category based on conditions.
-- The first matching WHEN condition is used.
-- CASE WHEN is useful for customer priority, aging buckets, and risk levels.


SELECT
    customers.customer_name,
    COALESCE(SUM(invoices.amount), 0) AS total_amount,
    CASE
        WHEN COALESCE(SUM(invoices, amount), 0) >= 5000 THEN 'High'
        WHEN COALESCE(SUM(invoices, amount), 0) >= 1000 THEN 'Medium'
        ELSE 'Low'
    END AS customer_priority
FROM customers
LEFT JOIN invoices
ON customers.customer_ID = invoices.customer_ID
GROUP BY customers.customer_name
ORDER BY total_amount DESC;