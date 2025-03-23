from django import forms

class QuizForm(forms.Form):
    # Define questions for each course
    QUESTIONS = {
        "python": [
            ("q1", "What is the output of print(2**3)?", [("a", "6"), ("b", "8"), ("c", "9"), ("d", "12")], "b"),
            ("q2", "Which keyword is used for function definition in Python?", [("a", "define"), ("b", "func"), ("c", "def"), ("d", "lambda")], "c"),
            ("q3", "What data type is the result of 3 / 2 in Python 3?", [("a", "int"), ("b", "float"), ("c", "double"), ("d", "long")], "b"),
            ("q4", "Which collection is ordered and mutable?", [("a", "Tuple"), ("b", "List"), ("c", "Set"), ("d", "Dictionary")], "b"),
            ("q5", "What is the output of bool([])?", [("a", "True"), ("b", "False")], "b"),
            ("q6", "Which operator is used for exponentiation?", [("a", "^"), ("b", "**"), ("c", "pow()"), ("d", "//")], "b"),
            ("q7", "Which module is used for handling JSON data?", [("a", "json"), ("b", "pickle"), ("c", "csv"), ("d", "os")], "a"),
            ("q8", "Which statement is used to end a loop early?", [("a", "exit"), ("b", "break"), ("c", "stop"), ("d", "return")], "b"),
            ("q9", "How do you open a file in read mode?", [("a", "open('file.txt')"), ("b", "open('file.txt', 'r')"), ("c", "open('file.txt', 'w')"), ("d", "open('file.txt', 'a')")], "b"),
            ("q10", "Which of these is an immutable data type?", [("a", "List"), ("b", "Dictionary"), ("c", "Tuple"), ("d", "Set")], "c"),
        ],
        "java": [
            ("q1", "Which keyword is used to define a class in Java?", [("a", "class"), ("b", "define"), ("c", "struct"), ("d", "object")], "a"),
            ("q2", "What is the size of an int in Java?", [("a", "2 bytes"), ("b", "4 bytes"), ("c", "8 bytes"), ("d", "16 bytes")], "b"),
            ("q3", "Which method is used to start a thread in Java?", [("a", "run()"), ("b", "start()"), ("c", "execute()"), ("d", "begin()")], "b"),
            ("q4", "Which of these is not a Java keyword?", [("a", "static"), ("b", "try"), ("c", "goto"), ("d", "include")], "d"),
            ("q5", "What is the default value of a boolean in Java?", [("a", "true"), ("b", "false"), ("c", "null"), ("d", "0")], "b"),
            ("q6", "Which of these is a valid Java identifier?", [("a", "1variable"), ("b", "_variable"), ("c", "variable!"), ("d", "var-iable")], "b"),
            ("q7", "Which package is imported by default in Java?", [("a", "java.util"), ("b", "java.lang"), ("c", "java.io"), ("d", "java.net")], "b"),
            ("q8", "What is the parent class of all classes in Java?", [("a", "Object"), ("b", "Class"), ("c", "Base"), ("d", "Root")], "a"),
            ("q9", "Which exception is thrown when dividing by zero in Java?", [("a", "ArithmeticException"), ("b", "NullPointerException"), ("c", "IOException"), ("d", "ClassNotFoundException")], "a"),
            ("q10", "Which of these is not a primitive data type in Java?", [("a", "int"), ("b", "float"), ("c", "String"), ("d", "char")], "c"),
        ],
        "ai": [
            ("q1", "What does AI stand for?", [("a", "Artificial Intelligence"), ("b", "Automated Interface"), ("c", "Advanced Integration"), ("d", "Algorithmic Input")], "a"),
            ("q2", "Which algorithm is used for supervised learning?", [("a", "K-Means"), ("b", "Linear Regression"), ("c", "Apriori"), ("d", "DBSCAN")], "b"),
            ("q3", "Which of these is a type of neural network?", [("a", "Convolutional Neural Network"), ("b", "Decision Tree"), ("c", "Random Forest"), ("d", "Support Vector Machine")], "a"),
            ("q4", "What is the purpose of backpropagation in neural networks?", [("a", "Data preprocessing"), ("b", "Weight adjustment"), ("c", "Feature extraction"), ("d", "Model evaluation")], "b"),
            ("q5", "Which of these is an AI programming language?", [("a", "Python"), ("b", "HTML"), ("c", "CSS"), ("d", "SQL")], "a"),
            ("q6", "What is the full form of NLP in AI?", [("a", "Natural Language Processing"), ("b", "Neural Learning Protocol"), ("c", "Network Layer Processing"), ("d", "Node Link Prediction")], "a"),
            ("q7", "Which of these is a reinforcement learning algorithm?", [("a", "Q-Learning"), ("b", "Linear Regression"), ("c", "K-Means"), ("d", "Apriori")], "a"),
            ("q8", "What is the purpose of a confusion matrix?", [("a", "Evaluate model performance"), ("b", "Data normalization"), ("c", "Feature selection"), ("d", "Data augmentation")], "a"),
            ("q9", "Which of these is a popular AI framework?", [("a", "TensorFlow"), ("b", "Bootstrap"), ("c", "React"), ("d", "Django")], "a"),
            ("q10", "Which AI concept involves machines learning from data?", [("a", "Machine Learning"), ("b", "Cloud Computing"), ("c", "Blockchain"), ("d", "Internet of Things")], "a"),
        ],
    }

    def __init__(self, course, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = self.QUESTIONS.get(course.lower(), [])
        for q_id, question, choices, correct in questions:
            self.fields[q_id] = forms.ChoiceField(
                label=question,
                choices=choices,
                widget=forms.RadioSelect,
                required=True
            )

    def check_answers(self):
        """Check the user's answers and calculate the score."""
        score = 0
        for q_id, _, _, correct in self.QUESTIONS.get(self.course.lower(), []):
            if self.cleaned_data.get(q_id) == correct:
                score += 1
        return score
