from flask import Flask, jsonify, request
from flask_cors import CORS
from models import (
    fetch_all_recipes,
    fetch_recipe_by_id,
    update_calendar,
    remove_from_calendar,
    toggle_favorite,
    remove_from_candidates
)

import json  # 追加

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # CORS設定を更新

# 0. ルートのエンドポイント指定
@app.route("/", methods=["GET"])
def home():
    return json.dumps({"message": "これはわるねっとのWEBアプリAPIページです！"}, ensure_ascii=False)

# 1. レシピデータを取得するエンドポイント
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = fetch_all_recipes()
    return json.dumps(recipes, ensure_ascii=False)

# 2. カレンダーにレシピを追加するエンドポイント
@app.route('/api/calendar/add', methods=['POST'])
def add_to_calendar():
    data = request.json
    print(data)  # 受け取ったJSONデータを出力
    try:
        recipe_id = data['recipeId']
        calendar_date = data['calendarDate']
        update_calendar(recipe_id, calendar_date)
        return json.dumps({"message": "カレンダーにレシピが追加されました", "success": True}, ensure_ascii=False)
    except KeyError as e:
        return json.dumps({"error": f"Missing key: {e}"}), 400


# 3. カレンダーからレシピを削除するエンドポイント
@app.route('/api/calendar/remove', methods=['DELETE'])
def remove_from_calendar_route():
    data = request.json
    recipe_id = data['recipeId']
    remove_from_calendar(recipe_id)
    return json.dumps({"message": "カレンダーからレシピが削除されました", "success": True}, ensure_ascii=False)

# 4. 候補リストからレシピを削除するエンドポイント
@app.route('/api/candidates/remove', methods=['DELETE'])
def remove_from_candidates_route():
    data = request.json
    recipe_id = data['recipeId']
    remove_from_candidates(recipe_id)
    return json.dumps({"message": "候補リストからレシピが削除されました", "success": True}, ensure_ascii=False)

# 5. お気に入りリストにレシピを追加/削除するエンドポイント
@app.route('/api/favorites/toggle', methods=['POST'])
def toggle_favorite_route():
    data = request.json
    recipe_id = data['recipeId']
    on_favorite = data['onFavorite']
    toggle_favorite(recipe_id, on_favorite)
    return json.dumps({"message": "お気に入りのステータスが変更（追加or削除）されました", "success": True}, ensure_ascii=False)

# 6. レシピ詳細情報を取得するエンドポイント
@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe_by_id(recipe_id):
    recipe = fetch_recipe_by_id(recipe_id)
    if recipe:
        return jsonify(recipe)
    return json.dumps({"message": "レシピ詳細情報が見つかりません", "success": False}, ensure_ascii=False), 404

if __name__ == '__main__':
    app.run(debug=True)
    