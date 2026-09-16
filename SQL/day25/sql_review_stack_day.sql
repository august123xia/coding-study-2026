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
    COALESCE(SUM(invoices.amount), 0)  AS total_unpaid,
CASE 
    WHEN COALESCE(SUM(invoices.amount), 0) >= 5000 THEN 'High'
    WHEN COALESCE(SUM(invoices.amount), 0) >= 3000 THEN 'Medium'
    WHEN COALESCE(SUM(invoices.amount), 0) > 0 THEN 'Low'
    ELSE 'No unpaid'
END AS risk_level
FROM 
    customers
LEFT JOIN invoices
ON customers.customer_id = invoices.customer_id
AND invoices.status = 'unpaid'
GROUP BY customers.customer_name
ORDER BY total_unpaid DESC    

-- Review:
-- LEFT JOIN keeps all customers from the left table.
-- ON defines how the two tables are matched.
-- AND invoices.status = 'unpaid' in ON means only unpaid invoices can be joined.
-- COUNT(invoices.invoice_id) counts matched unpaid invoices.
-- COALESCE(SUM(invoices.amount), 0) changes NULL into 0.
-- GROUP BY customers.customer_name summarizes invoices by customer.
-- CASE WHEN creates a risk level based on total_unpaid.
-- ORDER BY total_unpaid DESC sorts customers by unpaid amount.