-- 코드를 입력하세요

SELECT
    Z.FLAVOR
FROM
(
    SELECT 
        ROWNUM RNUM
        , FLAVOR
    FROM
    (

        SELECT
            A.FLAVOR
        FROM
            FIRST_HALF A
            , (
                SELECT
                    B.FLAVOR 
                    , SUM(TOTAL_ORDER) TOTAL_ORDER
                FROM
                    JULY B
                GROUP BY 
                    B.FLAVOR
            ) C
        WHERE
            A.FLAVOR = C.FLAVOR 
        ORDER BY 
            A.TOTAL_ORDER + C.TOTAL_ORDER DESC 
    )
) Z
WHERE
    Z.RNUM <= 3

