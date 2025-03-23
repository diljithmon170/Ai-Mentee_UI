from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def level(request):
    return render(request, 'level.html', {'user': request.user})

def quiz(request):
    course = request.GET.get('course', 'Unknown')

def quiz_page(request):
    """ Render the Quiz HTML Page """
    return render(request, "quiz.html")  # No need to pass questions here
    return HttpResponse(f"Quiz page for {course}")  # Just returning a basic response for now

def quiz_api(request):
    """ API to fetch questions based on the selected course """
    
    if request.method != "GET":
        return JsonResponse({"error": "Invalid request method"}, status=400)
    
    course = request.GET.get('course', 'Unknown')
    
    # Define categorized questions
    
    quizzes = {
        "Python": [
            # Beginner Level
            {"question": "What is the correct file extension for Python files?", 
             "options": [".py", ".pyt", ".pt", ".p"], "answer": ".py"},
            {"question": "Which function is used to print output in Python?", 
             "options": ["echo()", "console.log()", "print()", "write()"], "answer": "print()"},
            {"question": "Which data type is **immutable** in Python?", 
             "options": ["List", "Tuple", "Dictionary", "Set"], "answer": "Tuple"},
            {"question": "Which operator is used for exponentiation in Python?", 
             "options": ["^", "**", "//", "%%"], "answer": "**"},
            {"question": "Which built-in function is used to get user input in Python?", 
             "options": ["input()", "get_input()", "scan()", "read()"], "answer": "input()"},

            # Intermediate Level
            {"question": "What will `print(type([]))` return?", 
             "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>"], "answer": "<class 'list'>"},
            {"question": "Which method is used to remove a key from a dictionary?", 
             "options": ["del", "remove()", "pop()", "discard()"], "answer": "pop()"},
            {"question": "Which function is used to sort a list in **ascending order**?", 
             "options": ["sort()", "sorted()", "arrange()", "order()"], "answer": "sorted()"},
            {"question": "What is the output of `bool([])`?", 
             "options": ["True", "False", "None", "Error"], "answer": "False"},
            {"question": "Which of the following is **not** a Python framework?", 
             "options": ["Django", "Flask", "React", "FastAPI"], "answer": "React"},

            # Advanced Level
            {"question": "What is the time complexity of searching an element in a **balanced binary search tree (BST)?**", 
             "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "answer": "O(log n)"},
            {"question": "Which Python module is used for **multithreading**?", 
             "options": ["asyncio", "multiprocessing", "threading", "concurrent"], "answer": "threading"},
            {"question": "Which function in NumPy creates an array of **random numbers**?", 
             "options": ["np.random()", "np.random.rand()", "np.array()", "np.randomize()"], "answer": "np.random.rand()"},
            {"question": "Which library is used for **deep learning** in Python?", 
             "options": ["Pandas", "NumPy", "Matplotlib", "TensorFlow"], "answer": "TensorFlow"},
            {"question": "Which algorithm is used in **Garbage Collection** in Python?", 
             "options": ["Mark and Sweep", "LRU Caching", "Merge Sort", "Dijkstra"], "answer": "Mark and Sweep"}
        ],
        
        
    "AI": [
        # Beginner Level
        {"question": "What does AI stand for?", "options": ["Automated Intelligence", "Artificial Intelligence", "Advanced Internet", "Automated Information"], "answer": "Artificial Intelligence"},
        {"question": "Who is considered the father of AI?", "options": ["Alan Turing", "John McCarthy", "Geoffrey Hinton", "Andrew Ng"], "answer": "John McCarthy"},
        {"question": "Which of the following is an AI technique?", "options": ["Neural Networks", "Quantum Computing", "Compiler Design", "Cryptography"], "answer": "Neural Networks"},
        {"question": "Which is NOT a category of AI?", "options": ["Weak AI", "Strong AI", "Super AI", "Micro AI"], "answer": "Micro AI"},
        {"question": "Which algorithm is used in AI for decision-making?", "options": ["Dijkstra's Algorithm", "Minimax", "MD5 Hashing", "A* Search"], "answer": "Minimax"},
        
        # Intermediate Level
        {"question": "Which programming language is NOT commonly used in AI?", "options": ["Python", "R", "Java", "COBOL"], "answer": "COBOL"},
        {"question": "Which AI model generates human-like text?", "options": ["CNN", "RNN", "LLaMA", "SVM"], "answer": "LLaMA"},
        {"question": "What is a chatbot?", "options": ["A human assistant", "AI that talks like a human", "A type of virus", "None of the above"], "answer": "AI that talks like a human"},
        {"question": "What is reinforcement learning?", "options": ["AI learning through rewards", "AI learning from a teacher", "AI memorization", "A new type of ML"], "answer": "AI learning through rewards"},
        {"question": "Which company developed ChatGPT?", "options": ["Google", "Meta", "OpenAI", "Microsoft"], "answer": "OpenAI"},
        
        # Advanced Level
        {"question": "Which deep learning framework is NOT developed by Google?", "options": ["TensorFlow", "Keras", "PyTorch", "JAX"], "answer": "PyTorch"},
        {"question": "What does GAN stand for?", "options": ["General AI Network", "Generative Adversarial Network", "General Automated Neural Net", "None"], "answer": "Generative Adversarial Network"},
        {"question": "What is the role of a discriminator in a GAN?", "options": ["Generate data", "Classify images", "Distinguish real and fake data", "Optimize AI"], "answer": "Distinguish real and fake data"},
        {"question": "What does NLP stand for in AI?", "options": ["Natural Language Processing", "Neural Logic Programming", "Network Layer Protocol", "None"], "answer": "Natural Language Processing"},
        {"question": "Which AI technique is used in self-driving cars?", "options": ["SVM", "Decision Trees", "Deep Learning", "Blockchain"], "answer": "Deep Learning"}
    ],
        "ML": [
    # Beginner Level
    {"question": "What does ML stand for?", "options": ["Machine Learning", "Mega Learning", "Micro Learning", "Mixed Logic"], "answer": "Machine Learning"},
    {"question": "Which algorithm is used in supervised learning?", "options": ["K-Means", "Naive Bayes", "DBSCAN", "Apriori"], "answer": "Naive Bayes"},
    {"question": "Which ML technique is used in recommendation systems?", "options": ["Supervised Learning", "Clustering", "Reinforcement Learning", "Unsupervised Learning"], "answer": "Clustering"},
    {"question": "What is overfitting in ML?", "options": ["Too much bias", "High variance", "Low accuracy", "None"], "answer": "High variance"},
    {"question": "Which framework is best for ML?", "options": ["TensorFlow", "Bootstrap", "HTML", "CSS"], "answer": "TensorFlow"},
    
    # Intermediate Level
    {"question": "What is Gradient Descent used for in ML?", "options": ["Optimization", "Data Cleaning", "Feature Engineering", "Testing"], "answer": "Optimization"},
    {"question": "Which ML model is commonly used for classification?", "options": ["Linear Regression", "Decision Tree", "K-Means", "PCA"], "answer": "Decision Tree"},
    {"question": "Which method is used for dimensionality reduction?", "options": ["SVM", "PCA", "Naive Bayes", "Random Forest"], "answer": "PCA"},
    {"question": "What does a confusion matrix measure?", "options": ["Loss Function", "Model Accuracy", "Classification Performance", "Regression Output"], "answer": "Classification Performance"},
    {"question": "Which of these is NOT a machine learning model?", "options": ["Random Forest", "Logistic Regression", "CNN", "HTML"], "answer": "HTML"},
    
    # Advanced Level
    {"question": "Which optimization technique is used in Deep Learning?", "options": ["Adam", "Apriori", "DBSCAN", "TF-IDF"], "answer": "Adam"},
    {"question": "Which ML algorithm is best for anomaly detection?", "options": ["SVM", "Isolation Forest", "CNN", "LDA"], "answer": "Isolation Forest"},
    {"question": "Which neural network is best for sequential data?", "options": ["CNN", "RNN", "GAN", "KNN"], "answer": "RNN"},
    {"question": "Which activation function is commonly used in deep networks?", "options": ["ReLU", "Sigmoid", "Tanh", "Softmax"], "answer": "ReLU"},
    {"question": "What is Transfer Learning in ML?", "options": ["Training from scratch", "Using pre-trained models", "Hyperparameter tuning", "Data Augmentation"], "answer": "Using pre-trained models"}
],
        "Java": [
    # Beginner Level
    {"question": "What is the default value of a boolean variable in Java?", 
     "options": ["true", "false", "0", "null"], "answer": "false"},
    {"question": "Which keyword is used to define a class in Java?", 
     "options": ["class", "Class", "define", "new"], "answer": "class"},
    {"question": "Which method is the entry point for a Java program?", 
     "options": ["start()", "main()", "run()", "execute()"], "answer": "main()"},
    {"question": "Which of these is NOT a Java primitive data type?", 
     "options": ["int", "float", "char", "string"], "answer": "string"},
    {"question": "What is the correct way to declare an array in Java?", 
     "options": ["int[] arr;", "arr[] int;", "array int[];", "int arr[];"], "answer": "int[] arr;"},

    # Intermediate Level
    {"question": "Which access modifier makes a variable/method accessible only within the same class?", 
     "options": ["public", "private", "protected", "default"], "answer": "private"},
    {"question": "Which collection type maintains elements in sorted order?", 
     "options": ["ArrayList", "HashSet", "TreeSet", "LinkedList"], "answer": "TreeSet"},
    {"question": "Which keyword is used to create an instance of a class?", 
     "options": ["create", "new", "instance", "construct"], "answer": "new"},
    {"question": "What will `System.out.println(10 / 0);` throw?", 
     "options": ["ArithmeticException", "NullPointerException", "IndexOutOfBoundsException", "No error"], "answer": "ArithmeticException"},
    {"question": "Which Java feature ensures memory management for unused objects?", 
     "options": ["Destructor", "Garbage Collection", "Finalizer", "Pointer"], "answer": "Garbage Collection"},

    # Advanced Level
    {"question": "Which design pattern is used in the `java.lang.String` class to ensure immutability?", 
     "options": ["Singleton", "Factory", "Prototype", "Immutable"], "answer": "Immutable"},
    {"question": "What is the purpose of the `volatile` keyword in Java?", 
     "options": ["To make a variable thread-safe", "To prevent method overriding", "To define constants", "To improve performance"], "answer": "To make a variable thread-safe"},
    {"question": "Which Java feature allows executing code before garbage collection?", 
     "options": ["final", "finally", "finalize", "static"], "answer": "finalize"},
    {"question": "Which of these Java frameworks is used for web applications?", 
     "options": ["Spring", "TensorFlow", "Pandas", "PyTorch"], "answer": "Spring"},
    {"question": "Which interface is used for functional programming in Java 8?", 
     "options": ["Runnable", "Callable", "FunctionalInterface", "Comparator"], "answer": "FunctionalInterface"}
],
        "DBMS": [
    # Beginner Level
    {"question": "What does DBMS stand for?", 
     "options": ["Database Management System", "Data Backup Management System", "Database Manipulation Software", "Data Business Management System"], "answer": "Database Management System"},
    {"question": "Which of the following is NOT a type of database?", 
     "options": ["Hierarchical", "Relational", "Flat-file", "Compiler"], "answer": "Compiler"},
    {"question": "Which language is used to query a database?", 
     "options": ["HTML", "SQL", "Java", "Python"], "answer": "SQL"},
    {"question": "Which of these is an example of a relational database?", 
     "options": ["MongoDB", "Redis", "MySQL", "Neo4j"], "answer": "MySQL"},
    {"question": "Which SQL command is used to retrieve data from a database?", 
     "options": ["FETCH", "GET", "SELECT", "EXTRACT"], "answer": "SELECT"},

    # Intermediate Level
    {"question": "Which key uniquely identifies a row in a relational database?", 
     "options": ["Foreign Key", "Candidate Key", "Primary Key", "Unique Key"], "answer": "Primary Key"},
    {"question": "Which normalization form eliminates **partial dependencies**?", 
     "options": ["1NF", "2NF", "3NF", "BCNF"], "answer": "2NF"},
    {"question": "Which SQL clause is used to filter records?", 
     "options": ["WHERE", "ORDER BY", "HAVING", "GROUP BY"], "answer": "WHERE"},
    {"question": "What is the purpose of an index in a database?", 
     "options": ["To speed up queries", "To ensure data integrity", "To prevent data loss", "To establish relationships"], "answer": "To speed up queries"},
    {"question": "Which command is used to delete a database permanently?", 
     "options": ["DROP DATABASE", "DELETE DATABASE", "REMOVE DATABASE", "ERASE DATABASE"], "answer": "DROP DATABASE"},

    # Advanced Level
    {"question": "Which SQL statement is used for **transactions**?", 
     "options": ["BEGIN, COMMIT, ROLLBACK", "START, STOP, PAUSE", "INSERT, UPDATE, DELETE", "LOCK, UNLOCK"], "answer": "BEGIN, COMMIT, ROLLBACK"},
    {"question": "Which isolation level **prevents dirty reads**?", 
     "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"], "answer": "Read Committed"},
    {"question": "Which type of join returns only matching rows from both tables?", 
     "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"], "answer": "INNER JOIN"},
    {"question": "What is **sharding** in databases?", 
     "options": ["Splitting data across multiple servers", "Compressing large databases", "Encrypting data", "Creating indexes"], "answer": "Splitting data across multiple servers"},
    {"question": "Which NoSQL database is based on key-value pairs?", 
     "options": ["MongoDB", "Redis", "Neo4j", "Cassandra"], "answer": "Redis"}
]

    
    
    }
    questions = quizzes.get(course, [])

    return JsonResponse({"questions": questions})

    