print("===== RULE BASED CHATBOT =====")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    
    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    
    elif "name" in user:
        print("Bot: My name is AI Chatbot.")

    elif "who are you" in user:
        print("Bot: I am a simple Rule-Based AI Chatbot.")

    
    elif "how are you" in user:
        print("Bot: I am fine. Thanks for asking!")

    elif "your age" in user:
        print("Bot: I don't have an age because I am a computer program.")

    
    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.")

    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI that learns from data.")

    elif "deep learning" in user:
        print("Bot: Deep Learning is an advanced form of Machine Learning.")

    
    elif "python creator" in user or "creator of python" in user or "father of python" in user:
        print("Bot: Guido van Rossum is the creator of Python.")

    elif "python" in user:
        print("Bot: Python is a popular and easy-to-learn programming language.")

    elif "c++" in user:
        print("Bot: C++ is an object-oriented programming language.")

    elif "java" in user:
        print("Bot: Java is a platform-independent programming language.")

    elif "programming" in user:
        print("Bot: Programming is the process of writing instructions for computers.")

   
    elif "study" in user:
        print("Bot: Regular study and practice help improve your skills.")

    elif "university" in user:
        print("Bot: A university is an institution for higher education.")

    
    elif "pakistan" in user:
        print("Bot: Pakistan became independent on 14 August 1947.")

    elif "capital of pakistan" in user:
        print("Bot: Islamabad is the capital of Pakistan.")

    elif "computer" in user:
        print("Bot: A computer is an electronic device that processes data.")

    #
    elif "joke" in user:
        print("Bot: Why do programmers prefer Python? Because it's easy to understand!")

    elif "favorite language" in user:
        print("Bot: I like all programming languages equally.")

    elif "thanks" in user or "thank you" in user:
        print("Bot: You're welcome!")

    
    elif "help" in user:
        print("Bot: You can ask me about AI, Python, Programming, Pakistan, or Computers.")

    
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")