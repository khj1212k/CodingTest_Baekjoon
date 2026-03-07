# 부모 아이템의 등급 확인
# 등급 = RARE
# 그 부모를 재료로 하는 아이템 출력

SELECT t.ITEM_ID,	ITEM_NAME,	RARITY
FROM ITEM_TREE as t
JOIN ITEM_INFO as i
    ON t.ITEM_ID = i.ITEM_ID
WHERE PARENT_ITEM_ID IN (
    SELECT PARENT_ITEM_ID
    FROM ITEM_TREE as t
    JOIN ITEM_INFO as i
    ON t.PARENT_ITEM_ID = i.ITEM_ID # 부모 아이템의 희귀도를 봐야함.
    WHERE RARITY = 'RARE' # 부모 아이템의 희귀도
)
ORDER BY t.ITEM_ID DESC