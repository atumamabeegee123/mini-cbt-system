class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer.strip().lower() == (user_answer or "").strip().lower()

questions_list = [
    Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    Question("What is the capital of Nigeria?", ["Lagos", "Abuja", "Kano", "Port Harcourt"], "Abuja"),
    Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
    Question("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Pacific", "Arctic"], "Pacific"),
    Question("Who wrote 'Things Fall Apart'?", ["Wole Soyinka", "Chinua Achebe", "Ngugi wa Thiong'o", "Ben Okri"], "Chinua Achebe"),
]
{
    "question": "What is 2 + 2?",
    "options": ["3", "4", "5"],
    "answer": "4"
}
{
    "question": "Who developed the theory of relativity?",
    "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei"],
    "answer": "Albert Einstein"
}
{
    "question": "What is the largest planet in our solar system?",
    "options": ["Earth", "Jupiter", "Saturn"],
    "answer": "Jupiter"
}
{
    "question": "Which language is primarily spoken in Brazil?",
    "options": ["Spanish", "Portuguese", "French"],
    "answer": "Portuguese"
}