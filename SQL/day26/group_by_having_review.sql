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
(105, 5, 900, 'paid'),
(106, 1, 700, 'unpaid'),
(107, 1, 600, 'unpaid');

SELECT
    customers.customer_name,
    COUNT(invoices.invoice_id) AS unpaid_count,
    SUM(invoices.amount) AS total_unpaid
FROM customers
LEFT JOIN invoices
ON customers.customer_id = invoices.customer_id
WHERE status = 'unpaid'
GROUP BY customers.customer_id
HAVING SUM(invoices.amount) > 3000
ORDER BY total_unpaid DESC