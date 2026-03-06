SELECT YEAR(sales_date) as YEAR,
    MONTH(sales_date) as MONTH,
    gender as GENDER,
    COUNT(DISTINCT o.USER_ID) as USERS
FROM USER_INFO as u
JOIN ONLINE_SALE as o
    ON u.USER_ID = o.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR(sales_date), MONTH(sales_date), gender
ORDER BY YEAR(sales_date), MONTH(sales_date), gender