CREATE DATABASE Guessing_Game
GO
CREATE TABLE Game_Info(NAME VARCHAR(50), AGE TINYINT, RANDOM_NUMBER INT,RESULT VARCHAR(5))
GO
CREATE PROCEDURE sp_insert_data
	@name varchar(50),
	@age tinyint,
	@random_number int,
	@result varchar(5)
AS
BEGIN
	INSERT INTO Game_Info(NAME, AGE, RANDOM_NUMBER, RESULT)
	VALUES (@name, @age, @random_number, @result)
END
GO
CREATE PROCEDURE sp_history
AS
BEGIN
	SELECT * FROM Game_Info
END
GO
SELECT * FROM Game_Info
GO
