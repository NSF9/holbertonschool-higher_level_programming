-- uses hbtn_usa database and creates cities table
CREATE TABLE IF NOT EXISTS cities
(

	id INT AUTO_INCREMENT,
	state_id int NOT NULL,
	FOREIGN KEY (state_id) REFERENCES state(state_id),
	name VARCHAR(256) NOT NULL
);
