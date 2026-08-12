MySQL Terminal Commands
If you need to access your MySQL database manually via terminal:

1. Start the Server (Window 1)

Open a terminal in the folder where `mysqld.exe` lives: `D:\mga_data\WamppDB\bin\mysql\mysql8.4.7\bin\`

Run: `.\mysqld.exe --console` (Keep this window open while you work)

2. Connect to Database (Window 2)

Open a second terminal window in the same folder and run: `.\mysql.exe -u root -p`

3. Common SQL Commands

• Show all databases: `SHOW DATABASES;`

• Use a database: `USE your_database_name;`

• Show tables: `SHOW TABLES;`

• Exit MySQL: `EXIT;`



//// prompt from ausojsarrop email in claude