-- uses hbtn_usa database and creates cities table
CREATE TABLE IF NOT EXISTS cities
(

	id INT AUTO_INCREMENT,
	FOREIGN KEY (state_id)
	REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
