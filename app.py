from flask import Flask, jsonify
import random

app = Flask(__name__)

questions = [
    {
        "question": "Which organelle is responsible for energy production in cells?",
        "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"],
        "explanation": "Mitochondria are known as the powerhouse of the cell because they generate ATP, the cell's energy currency."
    },
    {
        "question": "What is the primary function of ribosomes?",
        "options": ["DNA replication", "Protein synthesis", "Energy production", "Lipid metabolism"],
        "explanation": "Ribosomes are responsible for synthesizing proteins by translating mRNA sequences into amino acid chains."
    },
    {
        "question": "Which biomolecule serves as the primary energy source for cells?",
        "options": ["Lipids", "Proteins", "Carbohydrates", "Nucleic acids"],
        "explanation": "Carbohydrates, specifically glucose, serve as the main source of energy for cells through cellular respiration."
    }
]

@app.route('/generate-question', methods=['GET'])
def generate_question():
    question_data = random.choice(questions)
    return jsonify(question_data)

if __name__ == '__main__':
    app.run(debug=True)
