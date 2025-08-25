from flask import Flask, request, jsonify
app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"ok": True})

@app.post("/zip-guard")
def zip_guard():
    data = request.json or {}
    if not data.get("city_or_zip"):
        return jsonify({"error": "city_or_zip required"}), 400
    return jsonify({"ok": True, "city_or_zip": data["city_or_zip"], "radius_miles": data.get("radius_miles")})
