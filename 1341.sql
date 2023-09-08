SELECT name as results
FROM
( 
  SELECT u.name, COUNT(mr.user_id) as count
  FROM Users u
  JOIN MovieRating mr ON u.user_id = mr.user_id
  GROUP BY u.name
  ORDER BY count DESC, u.name
  LIMIT 1
 ) sub

UNION ALL

SELECT title as results
FROM
(
  SELECT m.title, AVG(mr.rating) as max_rating
  FROM Movies M
  JOIN MovieRating mr ON m.movie_id = mr.movie_id
  WHERE mr.created_at >= '2020-02-01' AND mr.created_at <= '2020-02-28'
  GROUP BY m.title
  ORDER BY max_rating DESC, title
  LIMIT 1
) sub2