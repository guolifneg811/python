create_table_sql = """CREATE TABLE IF NOT EXISTS MOVIES(MOVIE_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,MOVIE_NAME VARCHAR(100),DIRECTOR VARCHAR(200),WRITER VARCHAR(200),ACTORS VARCHAR(200),MOVIE_TYPE VARCHAR(100),LOCATION VARCHAR(100),MOVIE_LANGUAGE VARCHAR(80),MOVIE_TIME VARCHAR(80),MOVE_TIME_LENGTH VARCHAR(80),IMDB_LINK CHAR(100),DESCRIPTION TEXT,RATING FLOAT NOT NULL )"""

insert_table_sql = """INSERT INTO MOVIES(MOVIE_NAME, DIRECTOR, WRITER, ACTORS, MOVIE_TYPE, LOCATION, MOVIE_LANGUAGE, MOVIE_TIME, MOVE_TIME_LENGTH, IMDB_LINK, DESCRIPTION, RATING) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s','%s', %f)"""

select_ip_proxies = """SELECT IP, PORT FROM IPPROXIES WHERE PROTOCOL='HTTP'"""

create_requested_urls_sql = """CREATE TABLE IF NOT EXISTS URLS(URL_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, URL CHAR(100) NOT NULL)"""
select_requested_urls_sql = """SELECT URL FROM URLS"""
insert_requested_urls_sql = """INSERT INTO URLS(URL) VALUES ('%s')"""

