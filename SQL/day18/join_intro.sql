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
(3, 'Dnata', 'Australia');

INSERT INTO invoices VALUES
(101, 1, 1200, 'paid'),
(102, 1, 1800, 'unpaid'),
(103, 2, 3500, 'unpaid'),
(104, 3, 5000, 'unpaid');

SELECT
    invoices.invoice_id,
    customers.customer_name,
    invoices.amount,
    invoices.status
FROM invoices
JOIN customers
ON invoices.customer_id = customers.customer_id;

SELECT
    invoices.invoice_id,
    customers.customer_name,
    invoices.amount,
    invoices.status
FROM invoices
JOIN customers
ON invoices.customer_id = customers.customer_id
WHERE invoices.status = 'unpaid';

SELECT
    customers.customer_name,
    SUM(invoices.amount) AS unpaid_total
FROM invoices
JOIN customers
ON invoices.customer_id = customers.customer_id
WHERE invoices.status = 'unpaid'
GROUP BY customers.customer_name
ORDER BY unpaid_total DESC;

SELECT
    customers.customer_name,
    customers.country,
    SUM(invoices.amount) AS unpaid_total
FROM invoices
JOIN customers
ON invoices.customer_id = customers.customer_id
WHERE 
    invoices.status = 'unpaid' AND customers.country = 'USA'
GROUP BY customers.customer_name, customers.country
ORDER BY unpaid_total DESC;


SELECT
    customers.customer_name,
    customers.country,
    SUM(invoices.amount) AS unpaid_total
FROM invoices
JOIN customers
ON invoices.customer_id = customers.customer_id
WHERE  invoices.status = 'unpaid' 
GROUP BY 
    customers.customer_name,
    customers.country
HAVING SUM(invoices.amount) > 3000
ORDER BY unpaid_total DESC;
 

SELECT
    customers.country,
    SUM(invoices.amount) AS unpaid_total,
    COUNT(*)
FROM invoices
JOIN customers
ON invoices.customer_id = customers.customer_id
WHERE invoices.status = 'unpaid'
GROUP BY customers.country
ORDER BY unpaid_total DESC;

