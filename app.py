import os
import json
import openai
from flask import Flask, jsonify, request

# Directly set your OpenAI API key (not recommended for production)
openai.api_key = "your-api-key-here"  # Replace with your actual API key

app = Flask(__name__)

@app.route('/generate-question', methods=['GET'])
def generate_question():
    # Get difficulty from query parameters (default: medium)
    difficulty = request.args.get('difficulty', 'medium')
    prompt = f"""
    Generate a challenging AP Biology or USABO-style multiple-choice question at {difficulty} difficulty.
    Include four answer options labeled A., B., C., and D., specify the correct answer in a field called "correct_answer"
    (just the letter, e.g., "C"), and provide an explanation for the correct answer.
    Format your answer as valid JSON with these fields: question, options (an array of strings), correct_answer, explanation.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" if preferred
            messages=[{"role": "system", "content": prompt}],
            temperature=0.7
        )
        content = response["choices"][0]["message"]["content"]
        # Parse the generated JSON
        question_data = json.loads(content)
        return jsonify(question_data)
    except Exception as e:
        # In case of errors, return the error and raw content for debugging
        return jsonify({"error": str(e), "raw": content if 'content' in locals() else ""})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
