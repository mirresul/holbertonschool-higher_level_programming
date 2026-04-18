from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}

@app.route("/")
def home():
    """Əsas səhifə üçün endpoint."""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """Bütün istifadəçi adlarının siyahısını qaytarır."""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """API-nin vəziyyətini yoxlamaq üçün endpoint."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Dinamik route: İstifadəçi adına görə məlumat qaytarır."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Yeni istifadəçi əlavə edir."""
    # JSON formatının düzgünlüyünü yoxla
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    username = data.get("username")

    # Username yoxdursa
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # İstifadəçi artıq mövcuddursa
    if username in users:
        return jsonify({"error": "User already exists"}), 409

    # İstifadəçini lüğətə əlavə et
    users[username] = data
    
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()
