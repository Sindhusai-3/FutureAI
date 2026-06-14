question_bank = {
    "python": ["What is a decorator?", "Explain list comprehension.", "What is a generator?",
                "What is exception handling?", "What is OOP?"],
    "sql": ["What is normalization?", "Explain JOIN operations.", "What is a primary key?",
            "What is a foreign key?"],
    "react": ["What are React hooks?", "What is Virtual DOM?", "What is useState?", "What is useEffect?"],
    "javascript": ["What is hoisting?", "What is a closure?", "What is event bubbling?"],
    "java": ["What is JVM?", "What is encapsulation?", "What is inheritance in Java?"],
    "machine learning": ["What is supervised learning?", "What is overfitting?", "What is underfitting?"],
    "nodejs": ["What is Node.js?", "What is middleware?", "What is Express.js?"],
    "mongodb": ["What is MongoDB?", "What is aggregation?", "What is a collection?"],
    "html": ["What is HTML?", "What are semantic tags?", "What is a form?"],
    "css": ["What is Flexbox?", "What is CSS Grid?", "What is CSS?"],
}

def generate_questions(skills):
    questions = []
    for skill in skills:
        if skill.lower() in question_bank:
            questions.extend(question_bank[skill.lower()])
    return questions[:10]
