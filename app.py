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

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # CORS設定を更新

# 1. レシピデータを取得するエンドポイント
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = fetch_all_recipes()
    return jsonify(recipes)

# 2. カレンダーにレシピを追加するエンドポイント
@app.route('/api/calendar/add', methods=['POST'])
def add_to_calendar():
    data = request.json
    recipe_id = data['recipeId']
    calendar_date = data['calendarDate']
    update_calendar(recipe_id, calendar_date)
    return jsonify({"message": "Recipe added to calendar successfully", "success": True})

# 3. カレンダーからレシピを削除するエンドポイント
@app.route('/api/calendar/remove', methods=['DELETE'])
def remove_from_calendar_route():
    data = request.json
    recipe_id = data['recipeId']
    remove_from_calendar(recipe_id)
    return jsonify({"message": "Recipe removed from calendar successfully", "success": True})

# 4. 候補リストからレシピを削除するエンドポイント
@app.route('/api/candidates/remove', methods=['DELETE'])
def remove_from_candidates_route():
    data = request.json
    recipe_id = data['recipeId']
    remove_from_candidates(recipe_id)
    return jsonify({"message": "Recipe removed from candidates successfully", "success": True})

# 5. お気に入りリストにレシピを追加/削除するエンドポイント
@app.route('/api/favorites/toggle', methods=['POST'])
def toggle_favorite_route():
    data = request.json
    recipe_id = data['recipeId']
    on_favorite = data['onFavorite']
    toggle_favorite(recipe_id, on_favorite)
    return jsonify({"message": "Favorite status updated", "success": True})

# 6. レシピ詳細情報を取得するエンドポイント
@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe_by_id(recipe_id):
    recipe = fetch_recipe_by_id(recipe_id)
    if recipe:
        return jsonify(recipe)
    return jsonify({"message": "Recipe not found", "success": False}), 404

if __name__ == '__main__':
    app.run(debug=True)
    