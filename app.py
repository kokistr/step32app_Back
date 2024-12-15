from flask import Flask, Response, request
from flask_cors import CORS
from models import (
    fetch_all_recipes,
    fetch_recipe_by_id,
    update_calendar,
    remove_from_calendar,
    toggle_favorite,
    remove_from_candidates
)
from datetime import date
import json

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://tech0-gen-8-step3-app-node-14.azurewebsites.net",
            "https://tech0-gen-8-step3-rdb-14.mysql.database.azure.com/",
            "https://localhost:3000",
            "http://localhost:3000" # ローカル開発用
        ]
    }
})

# dateオブジェクトをISO形式の文字列に変換する関数
def convert_dates(data):
    if isinstance(data, list):
        for item in data:
            convert_dates(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, date):
                data[key] = value.isoformat()
            elif isinstance(value, (dict, list)):
                convert_dates(value)


def create_response(data):
    """UTF-8エンコーディングでJSONレスポンスを作成するヘルパー関数"""
    response_data = json.dumps(data, ensure_ascii=False, indent=2)
    return Response(response_data, content_type='application/json; charset=utf8mb4')


# 0. ルートのエンドポイント指定
@app.route("/", methods=["GET"])
def home():
    return create_response({"message": "これはわるねっとのWEBアプリAPIページです！"})


# 1. レシピデータを取得するエンドポイント
# 1. 文字化け修正
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = fetch_all_recipes()
    convert_dates(recipes)
    # UTF-8エンコーディングでレスポンスを返す
    response = create_response(recipes)
    #response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


# 2. カレンダーにレシピを追加するエンドポイント
@app.route('/api/calendar/add', methods=['POST'])
def add_to_calendar():
    data = request.json
    try:
        recipe_id = data['recipeId']
        calendar_date = data['calendarDate']
        update_calendar(recipe_id, calendar_date)
        return create_response({"message": "カレンダーにレシピが追加されました", "success": True})
    except KeyError as e:
        return create_response({"error": f"Missing key: {e}"}), 400


# 3. カレンダーからレシピを削除するエンドポイント
@app.route('/api/calendar/remove', methods=['DELETE'])
def remove_from_calendar_route():
    data = request.json
    recipe_id = data['recipeId']
    remove_from_calendar(recipe_id)
    return create_response({"message": "カレンダーからレシピが削除されました", "success": True})


# 4. 候補リストからレシピを削除するエンドポイント
@app.route('/api/candidates/remove', methods=['DELETE'])
def remove_from_candidates_route():
    data = request.json
    recipe_id = data['recipeId']
    remove_from_candidates(recipe_id)
    return create_response({"message": "候補リストからレシピが削除されました", "success": True})


# 5. お気に入りリストにレシピを追加/削除するエンドポイント
@app.route('/api/favorites/toggle', methods=['POST'])
def toggle_favorite_route():
    data = request.json
    recipe_id = data['recipeId']
    on_favorite = data['onFavorite']
    toggle_favorite(recipe_id, on_favorite)
    return create_response({"message": "お気に入りのステータスが変更（追加or削除）されました", "success": True})


# 6. レシピ詳細情報を取得するエンドポイント
@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe_by_id(recipe_id):
    recipe = fetch_recipe_by_id(recipe_id)
    if recipe:
        convert_dates(recipe)
        return create_response(recipe)
    return create_response({"message": "レシピ詳細情報が見つかりません", "success": False}), 404


if __name__ == '__main__':
    app.run(debug=True)
