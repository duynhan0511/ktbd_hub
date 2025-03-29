# configs/settings.py
import pymysql.cursors

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "root",       # hoặc 'root' nếu đang dùng XAMPP
    "password": "",    # để trống nếu là root không password
    "database": "efootball_ktbd",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}

# Cấu hình API nếu cần dùng chung
BASE_API_URL = "https://api.efootballdb.com/api/2022"
