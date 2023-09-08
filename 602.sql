SELECT id, num
FROM (
    SELECT requester_id AS id, COUNT(*) AS num
    FROM (
        SELECT requester_id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id FROM RequestAccepted
    ) AS all_users
    GROUP BY requester_id
) AS friend_counts
ORDER BY num DESC
LIMIT 1;
