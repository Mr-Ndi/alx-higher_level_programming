-- a script that converts hbtn_0c_0 database to UTF8 
use hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARSET SET utf8mb4 COLLATE utf8mb4_unicode_ci;

