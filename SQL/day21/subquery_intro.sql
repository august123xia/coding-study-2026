DROP TABLE IF EXISTS invoices;

CREATE TABLE invoices (
    invoice_id INTEGER,
    customer TEXT,
    amount INTEGER,
    status TEXT
);

INSERT INTO invoices VALUES
(101, 'Google', 1200, 'paid'),
(102, 'Google', 1800, 'unpaid'),
(103, 'Amazon', 3500, 'unpaid'),
(104, 'Dnata', 5000, 'unpaid'),
(105, 'Apple', 900, 'paid');

SELECT
    AVG(amount) AS average_amount
FROM invoices;

SELECT
    invoice_id,
    customer,
    amount
FROM invoices
WHERE amount > (
    SELECT AVG(amount)
    FROM invoices
);

SELECT
    invoice_id,
    customer,
    amount,
    status
FROM invoices
WHERE status = 'unpaid'
AND amount > (
    SELECT AVG(amount)
    FROM invoices
    WHERE status = 'unpaid'
);

SELECT
    invoice_id,
    customer,
    amount,
    status
FROM invoices
WHERE status = 'paid'
AND amount > (
    SELECT AVG(amount)
    FROM invoices
    WHERE status = 'paid'
);


-- Review:
-- A subquery is a SELECT statement inside another SELECT statement.
-- The inner SELECT runs first and returns a value.
-- The outer SELECT uses that value in the WHERE condition.
-- We can use subqueries to compare invoice amounts with average amounts.
-- Example: find invoices greater than the average unpaid invoice amount.