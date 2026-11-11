-- Example SQL analysis for customer_transactions_simulated.csv.
-- Load the CSV into a table named transactions before running.

-- 1. Monthly revenue and order metrics
SELECT
    DATE_TRUNC('month', transaction_date) AS month,
    COUNT(DISTINCT transaction_id) AS orders,
    COUNT(DISTINCT customer_id) AS customers,
    SUM(revenue) AS revenue,
    SUM(revenue) / NULLIF(COUNT(DISTINCT transaction_id), 0) AS average_order_value
FROM transactions
GROUP BY 1
ORDER BY 1;

-- 2. Category performance
SELECT
    category,
    COUNT(DISTINCT transaction_id) AS orders,
    SUM(quantity) AS units,
    SUM(revenue) AS revenue
FROM transactions
GROUP BY category
ORDER BY revenue DESC;

-- 3. Highest-value customers
SELECT
    customer_id,
    COUNT(DISTINCT transaction_id) AS orders,
    SUM(revenue) AS lifetime_revenue
FROM transactions
GROUP BY customer_id
ORDER BY lifetime_revenue DESC
LIMIT 20;
