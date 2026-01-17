-- show list of tv genre name and count of the number of shows by inner join query 
SELECT Tv_genres.name AS genre, COUNT(Tv_show_genres.genre_id) AS number_of_shows 
FROM Tv_show_genres
JOIN Tv_genres ON Tv_genres.id = Tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
