--IBM Questions
SELECT EXTRACT('MONTH' FROM sale_date), product_id as product, AVG(quantity) FROM sales 