
SELECT
  c.Year,
  ROUND(SUM(f.Weekly_Sales), 2) AS Total_Sales
FROM sales_fact f
JOIN calendar c ON f.Date = c.Date
GROUP BY c.Year
ORDER BY c.Year;


SELECT
  s.Store_Type,
  ROUND(SUM(f.Weekly_Sales), 2) AS Total_Sales
FROM sales_fact f
JOIN stores_info s ON f.Store_ID = s.Store_ID
GROUP BY s.Store_Type
ORDER BY Total_Sales DESC;


SELECT
  f.IsHoliday,
  ROUND(SUM(f.Weekly_Sales), 2) AS Total_Sales
FROM sales_fact f
GROUP BY f.IsHoliday;


SELECT
  f.Store_ID,
  ROUND(SUM(f.Weekly_Sales), 2) AS Total_Sales
FROM sales_fact f
GROUP BY f.Store_ID
ORDER BY Total_Sales DESC
LIMIT 10;


SELECT
  CASE
    WHEN Promo_Discount_1 > 0 THEN 'Promo Active'
    ELSE 'No Promo'
  END AS Promo_Status,
  ROUND(AVG(Weekly_Sales), 2) AS Avg_Weekly_Sales
FROM sales_fact
GROUP BY Promo_Status;


SELECT
  COUNT(*) AS Return_Weeks
FROM sales_fact
WHERE Is_Return_Week = 1;
