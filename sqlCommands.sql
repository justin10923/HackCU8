CREATE TABLE remindDB.users(
	id INT AUTO_INCREMENT NOT NULL,
    firstName VARCHAR(25) NOT NULL,
    lastName VARCHAR(25) NOT NULL,
    userName VARCHAR(30) UNIQUE,
    password VARCHAR(30),
    email VARCHAR(50) NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);

CREATE TABLE remindDB.contacts(
	id INT AUTO_INCREMENT NOT NULL,
    userId INT NOT NULL,
    firstName VARCHAR(25) NOT NULL,
    lastName VARCHAR(25) NOT NULL,
    email_0 VARCHAR(50),
    email_1 VARCHAR(50),
    phonenumber_0 VARCHAR NOT NULL,
    phonenumber_1 VARCHAR NOT NULL,
    next_contact_date DATETIME,
    interval_days INT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY(userID)  REFERENCES users(id)
);