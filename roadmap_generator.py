ROADMAP = {
    "python": ["Introduction to Python", "Data Types and Variables", "Control Structures", "Functions", "Classes and Objects"],
    "sqls": ["Introduction to SQL", "Basic Queries", "Joins and Subqueries", "Indexes and Optimization", "Stored Procedures"],
    "pandas": ["Introduction to Pandas", "DataFrames and Series", "Data Cleaning and Preparation", "Data Analysis and Visualization", "Advanced Pandas Techniques"],
    "numpy": ["Introduction to NumPy", "Arrays and Matrices", "Mathematical Operations", "Random Number Generation", "Advanced NumPy Techniques"],
    "sckit-learn": ["Introduction to Scikit-learn", "Supervised Learning", "Unsupervised Learning", "Model Evaluation and Selection", "Advanced Scikit-learn Techniques"],
    "matplotlib": ["Introduction to Matplotlib", "Basic Plotting", "Customizing Plots", "Subplots and Layouts", "Advanced Matplotlib Techniques"],
    "machine learning": ["Introduction to Machine Learning", "Regression Algorithms", "Classification Algorithms", "Clustering Algorithms", "Model Deployment and Monitoring"],
    "deep learning": ["Introduction to Deep Learning", "Neural Networks", "Convolutional Neural Networks", "Recurrent Neural Networks", "Advanced Deep Learning Techniques"],
    "nlp": ["Introduction to Natural Language Processing", "Text Preprocessing", "Sentiment Analysis", "Named Entity Recognition", "Advanced NLP Techniques"],
    "pytorch": ["Introduction to PyTorch", "Tensors and Operations", "Building Neural Networks", "Training and Evaluation", "Advanced PyTorch Techniques"],
    "tensorflow": ["Introduction to TensorFlow", "Tensors and Operations", "Building Neural Networks", "Training and Evaluation", "Advanced TensorFlow Techniques"],
    "transformers": ["Introduction to Transformers", "Attention Mechanism", "Transformer Architectures", "Fine-tuning Pre-trained Models", "Advanced Transformer Techniques"],  
    "hugging face": ["Introduction to Hugging Face", "Transformers Library", "Tokenization and Preprocessing", "Fine-tuning Models", "Advanced Hugging Face Techniques"],
    "llm": ["Introduction to Large Language Models", "Training LLMs", "Fine-tuning LLMs", "LLM Applications", "Advanced LLM Techniques"],
    "rag": ["Introduction to Retrieval-Augmented Generation", "RAG Architecture", "Implementing RAG Models", "Fine-tuning RAG Models", "Advanced RAG Techniques"],
    "opencv": ["Introduction to OpenCV", "Image Processing Basics", "Feature Detection and Matching", "Object Detection and Tracking", "Advanced OpenCV Techniques"],
    "cnn": ["Introduction to Convolutional Neural Networks", "Convolutional Layers", "Pooling Layers", "CNN Architectures", "Advanced CNN Techniques"],
    "yolo": ["Introduction to YOLO", "YOLO Architecture", "Object Detection with YOLO", "Fine-tuning YOLO Models", "Advanced YOLO Techniques"],
    "fastapi": ["Introduction to FastAPI", "Building APIs with FastAPI", "Request and Response Handling", "Authentication and Authorization", "Advanced FastAPI Techniques"],
    "flask": ["Introduction to Flask", "Routing and Views", "Templates and Forms", "Database Integration", "Advanced Flask Techniques"],
    "docker": ["Introduction to Docker", "Docker Images and Containers", "Docker Compose", "Docker Networking", "Advanced Docker Techniques"],
    "git": ["Introduction to Git", "Version Control Basics", "Branching and Merging", "Collaboration with Git", "Advanced Git Techniques"],
    "aws": ["Introduction to AWS", "EC2 and S3", "AWS Lambda", "AWS RDS", "Advanced AWS Techniques"],
    "mongodb": ["Introduction to MongoDB", "CRUD Operations", "Indexes and Aggregation", "Replication and Sharding", "Advanced MongoDB Techniques"],
    "postgresql": ["Introduction to PostgreSQL", "Basic Queries", "Joins and Subqueries", "Indexes and Optimization", "Stored Procedures", "Advanced PostgreSQL Techniques"],
}

def generate_roadmap(missing_skills):
    roadmap = {}

    for skill in missing_skills:
        skill = skill.lower()

        if skill in ROADMAP:
            roadmap[skill] = ROADMAP[skill]
        else:
            roadmap[skill] = [f"Learn the basics of {skill}, Practice {skill} with small exercises, Build a small project using {skill}, Explore advanced topics in {skill}, Contribute to open-source projects using {skill}"]

    return roadmap