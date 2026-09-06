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
    customers.customer_id,
    customers.customer_name,
    invoices.invoice_id,
    invoices.amount,
    invoices.status
FROM customers
LEFT JOIN invoices
ON customers.customer_id = invoices.customer_id;

SELECT
    customers.customer_id,
    customers.customer_name
FROM customers
LEFT JOIN invoices
ON customers.customer_id = invoices.customer_id
WHERE invoices.invoice_id IS NULL;


SELECT
    customers.customer_id,
    customers.customer_name,
    invoices.invoice_id,
    invoices.status
FROM customers
LEFT JOIN invoices
ON customers.customer_id = invoices.customer_id
AND invoices.status = 'unpaid'
WHERE invoices.invoice_id IS NULL;