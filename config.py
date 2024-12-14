import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'tech0-gen-8-step3-rdb-14.mysql.database.azure.com'),
    'user': os.getenv('DB_USER', 'tech0gen8student'),
    'password': os.getenv('DB_PASSWORD', '5iTbVNuqQu8z14'),
    'database': os.getenv('DB_NAME', 'recipes_table'),
    'charset': 'utf8mb4'
}
