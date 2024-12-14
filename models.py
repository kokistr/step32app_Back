# MySQLデータベースの操作を管理するためのモデルを作成
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

# データベース接続を取得する関数
def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# 1. すべてのレシピデータを取得する関数
def fetch_all_recipes():
    conn = get_db_connection()
    if conn is None:
        return []

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM recipes")
        recipes = cursor.fetchall()
        return recipes
    finally:
        cursor.close()
        conn.close()

# 2. レシピIDで特定のレシピを取得する関数
def fetch_recipe_by_id(recipe_id):
    conn = get_db_connection()
    if conn is None:
        return None

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM recipes WHERE recipeid = %s", (recipe_id,))
        recipe = cursor.fetchone()
        return recipe
    finally:
        cursor.close()
        conn.close()

# 3. カレンダーにレシピを追加する関数
def update_calendar(recipe_id, calendar_date):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE recipes SET onCalendar = TRUE, calendarDate = %s WHERE recipeid = %s",
            (calendar_date, recipe_id)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# 4. カレンダーからレシピを削除する関数
def remove_from_calendar(recipe_id):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE recipes SET onCalendar = FALSE, calendarDate = NULL WHERE recipeid = %s",
            (recipe_id,)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# 5. お気に入りリストにレシピを追加/削除する関数
def toggle_favorite(recipe_id, on_favorite):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE recipes SET onFavorite = %s WHERE recipeid = %s",
            (on_favorite, recipe_id)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# 6. 候補リストからレシピを削除する関数
def remove_from_candidates(recipe_id):
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE recipes SET onCandidate = FALSE WHERE recipeid = %s",
            (recipe_id,)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()
