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
(106, 1, 700, 'unpaid'),
(107, 1, 600, 'unpaid'),
(103, 2, 3500, 'unpaid'),
(104, 3, 5000, 'unpaid'),
(105, 5, 900, 'paid');



SELECT
    customer_id,
    customer_name,
    country
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM invoices
    WHERE status = 'unpaid'
);

SELECT '--- Customers without unpaid invoices ---';

SELECT
    customer_id,
    customer_name,
    country
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM invoices
    WHERE status = 'unpaid'
);

SELECT
    customers.customer_id,
    customers.customer_name,
    invoices.invoice_id,
    invoices.amount,
    invoices.status
FROM customers
JOIN invoices
ON customers.customer_id = invoices.customer_id
WHERE invoices.status = 'unpaid';


SELECT 
    customers.customer_name,
    COUNT(*) AS unpaid_count,
    SUM(invoices.amount) AS unpaid_total 
FROM customers
JOIN invoices
ON customers.customer_id = invoices.customer_id
WHERE invoices.status = 'unpaid'
GROUP BY customers.customer_name
ORDER BY unpaid_total DESC;

SELECT
    customers.customer_name,
    COUNT(invoices.invoice_id) AS unpaid_count,
    COALESCE(SUM(invoices.amount), 0) AS total_unpaid
FROM customers
LEFT JOIN invoices
ON customers.customer_id = invoices.customer_id
AND invoices.status = 'unpaid'
GROUP BY customers.customer_name
ORDER BY total_unpaid DESC;