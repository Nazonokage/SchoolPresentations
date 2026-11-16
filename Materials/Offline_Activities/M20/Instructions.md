# Module 20: Transform and summarize data

## Transform and summarize data

1. Individual practical activity • 20 points • Suggested time: 60–90 minutes.
2. Use XAMPP, the local database server and phpMyAdmin. Keep this deck and the supplied files on your computer.
3. Submit your working database export, SQL statements, screenshots and activity log. Your instructor records the score.

## Start your offline workspace

1. Before class: the instructor installs and tests XAMPP and copies this activity folder to each computer. No downloads or online accounts are needed during the activity.
2. Open XAMPP Control Panel. Start Apache and MySQL. XAMPP commonly bundles MariaDB under the MySQL label; these tasks use compatible SQL.
3. Open http://localhost/phpmyadmin in your browser. If Apache uses another port, use the instructor-provided local address.

## Create your activity database

1. Choose New or Databases. Create im_m20_lastname, replacing lastname with your surname using letters, numbers and underscores. Choose utf8mb4_general_ci.
2. If that database already exists, use a fresh name ending in _v2; keep your previous work.
3. Select the new database in the left sidebar. Use its SQL tab to enter statements and Go to execute. Save each successful statement in a local queries.sql text file.

## Clean text and calculate dates

1. Import starter.sql. Browse customers and orders.
2. Use UPPER(TRIM(customer_name)) to display clean customer names. Keep the stored originals unchanged.
3. Use DATE_ADD(order_date, INTERVAL 5 DAY) to calculate a delivery date for each order. Include order_id in the output.

## Calculate sales summaries

1. Use ROUND(quantity * unit_price, 2) to display the total for each order.
2. Use a JOIN and GROUP BY customer_id, customer_name to calculate sales per customer. Expected: customer 1 = 150.00; customer 2 = 75.00.
3. Use COUNT(*) and SUM(quantity * unit_price) for a summary. Expected: three orders and 225.00 total. Capture results and save queries.

## Export and restore your work

1. Select your activity database. Choose Export > Quick > SQL > Go (or Export) and save database.sql.
2. Choose New and create a separate empty database with _restore added to your activity database name. Select it.
3. Choose Import > Choose file, select database.sql, then Go. Compare the restored table row counts with the original. Capture the restored database name and data.

## Evidence and submission

1. Create a folder named Lastname_Firstname_M20. Save database.sql and queries.sql inside it.
2. Save numbered screenshots: database structure, each requested task result or expected error, and the restored database. Include the SQL and result together where possible.
3. Add activity_log.txt: your name, section, date, database/server version shown by phpMyAdmin, actions completed, observations requested above, and one problem with its fix.
4. Copy the folder to the instructor’s USB drive or designated local submission folder. Show the working database when asked.

## Recorded activity criteria

1. Database structure and valid data: 6 points. Full credit when all specified columns, keys and records are correct.
2. Task execution and results: 8 points. Award proportionally for completed steps with correct results, including required constraint checks.
3. Evidence and activity log: 4 points. Screenshots show the requested work and the log explains observations.
4. Export and successful restore: 2 points. SQL backup imports into a separate database and row counts match.

## If something stops working

1. Apache or MySQL will not start: capture the Control Panel message and ask the instructor to check the port or service conflict.
2. Import says table already exists: select a new empty database and import there once.
3. Foreign-key error: create and populate parent tables first; child values must match existing parent IDs.
4. Before closing: confirm your submission files are saved outside the browser. Browser history alone is not your activity record.

## Ready-to-copy SQL

Open [Code.html](Code.html) for numbered SQL steps with offline Copy buttons, or open [apply.sql](apply.sql) in a text editor. Run one statement at a time and capture the requested outputs. Skip setup statements you already completed through the interface. Expected-error checks are separate in Code.html.
