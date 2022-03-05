CREATE TABLE `remindDB`.`users`(
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `firstName` VARCHAR(25) NOT NULL,
    `lastName` VARCHAR(25) NOT NULL,
    `userName` VARCHAR(30) UNIQUE,
    `passWord` VARCHAR(30),
    `email` VARCHAR(50) NOT NULL,
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `remindDB`.`contacts`(
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `userID` INT,
    `firstName` VARCHAR(25) NOT NULL,
    `lastName` VARCHAR(25) NOT NULL,
    `email_0` VARCHAR(50),
    `email_1` VARCHAR(50),
    `phonenumber_0` INT NOT NULL,
    `phonenumber_1` INT NOT NULL,
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP
);