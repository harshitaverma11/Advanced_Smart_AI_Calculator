import os
from flask import Flask, jsonify, render_template, request
from openai import OpenAI
from datetime import datetime

# Configure OpenAI client
client = OpenAI(
    #api_key=""
)

app = Flask(__name__)

# In-memory storage for calculation history (in production, use a database)
calculation_history = []


@app.route("/")
def index():
    return render_template("calculator_advanced.html")


@app.route("/api/calc", methods=["POST"])
def api_calc():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    mode = data.get("mode", "standard")  # standard, detailed, step-by-step

    if not question:
        return jsonify({"error": "Question is required."}), 400

    try:
        # Different system prompts based on mode
        system_prompts = {
            "standard": "You are a smart calculator. Solve the math problem correctly and give only the final answer.",
            "detailed": "You are an advanced calculator. Solve the math problem and provide: 1) The final answer, 2) A brief explanation of the method used.",
            "step-by-step": "You are a teaching calculator. Solve the math problem step-by-step, showing each calculation step clearly, then provide the final answer."
        }
        
        system_prompt = system_prompts.get(mode, system_prompts["standard"])
        
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )
        answer = response.choices[0].message.content
        
        # Store in history
        history_entry = {
            "id": len(calculation_history) + 1,
            "question": question,
            "answer": answer,
            "mode": mode,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        calculation_history.append(history_entry)
        
        return jsonify({
            "answer": answer,
            "history_id": history_entry["id"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/history", methods=["GET"])
def get_history():
    limit = request.args.get("limit", 10, type=int)
    return jsonify({
        "history": calculation_history[-limit:][::-1],  # Return most recent first
        "total": len(calculation_history)
    })


@app.route("/api/history/<int:history_id>", methods=["DELETE"])
def delete_history_item(history_id):
    global calculation_history
    calculation_history = [h for h in calculation_history if h["id"] != history_id]
    return jsonify({"success": True})


@app.route("/api/history", methods=["DELETE"])
def clear_history():
    global calculation_history
    calculation_history = []
    return jsonify({"success": True})


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 Advanced Smart AI Calculator Server Starting...")
    print("="*60)
    print(f"\n📍 Server running at: http://127.0.0.1:5000")
    print(f"🌐 Open in browser: http://127.0.0.1:5000")
    print("\n💡 Press CTRL+C to stop the server")
    print("="*60 + "\n")
    app.run(host="127.0.0.1", port=5000, debug=True)
