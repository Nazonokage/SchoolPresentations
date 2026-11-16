# Task API lab
Choose one server. Both expose GET/POST /tasks and PATCH/DELETE /tasks/{id}. Records have a string id, title and Boolean done. Use sample data on a private class network. These shared demo endpoints do not authenticate students.

**MongoDB** Start a local mongod service. From this folder run `npm install`, then `npm start`. Set MONGO_URI on the server to use another deployment. For a phone on your trusted LAN set `$env:LAB_HOST='0.0.0.0'` before starting.

**SQL** Start MySQL or MariaDB in XAMPP/WampServer. In its administration console create database adet_lab and a dedicated local account with table creation and CRUD privileges on that database. Apache is optional. FastAPI serves HTTP on port 8000. In a Python virtual environment run:

```powershell
python -m pip install fastapi uvicorn "sqlalchemy>=2,<3" pymysql cryptography
$env:DATABASE_URL='mysql+pymysql://LAB_USER:URL_ENCODED_PASSWORD@127.0.0.1:3306/adet_lab'
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Set EXPO_PUBLIC_API_URL on the Expo development computer to the API URL reachable from the phone. Never put DATABASE_URL or MONGO_URI into Expo variables. Verify GET /tasks in the phone browser before starting Expo. For a school LAN with device isolation or blocked cleartext HTTP, use an instructor-provisioned HTTPS API. Check POST with a blank title (422), create a valid task (201), mark it done, restart the client, delete it (204) and verify the list. Restart the **server** too to distinguish persistence from memory.
