class Quiz:
    def __init__(self, score_per_question=5):
        # Student info
        self.full_name = None
        self.student_id = None

        # Quiz data
        self.questions = []  # each question is a dict: {"question", "options", "answer"}

        # Scoring
        self.score_per_question = score_per_question
        self.right = 0
        self.wrong = 0
        self.total_score = 0

    def personal_info(self):
        # Collect student info with basic validation
        self.full_name = input("Enter your full name: ").strip()
        while True:
            sid = input("Enter your student ID (numbers only): ").strip()
            if sid.isdigit():
                self.student_id = int(sid)
                break
            print("Invalid ID. Please enter digits only.")

    def add_questions(self):
        # Ask how many questions to add
        while True:
            n = input("Enter number of questions you want to add: ").strip()
            if n.isdigit() and int(n) > 0:
                total = int(n)
                break
            print("Please enter a positive integer.")

        # Collect each question
        for i in range(1, total + 1):
            print(f"\n--- Adding question {i} ---")
            q_text = input("Enter question: ").strip()

            # Collect 4 options
            options = []
            for j in range(1, 5):
                opt = input(f"Enter option-{j}: ").strip()
                options.append(opt)

            # Choose correct option by number (1–4)
            while True:
                correct_idx = input("Enter the correct option number (1-4): ").strip()
                if correct_idx in {"1", "2", "3", "4"}:
                    correct_idx = int(correct_idx) - 1
                    break
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

            self.questions.append({
                "question": q_text,
                "options": options,
                "answer_index": correct_idx  # store index of correct option
            })

        print(f"\nAdded {len(self.questions)} question(s).")

    def start_quiz(self):
        if not self.questions:
            print("No questions found. Please add questions first.")
            return

        print("\n=== Quiz Started ===")
        for idx, q in enumerate(self.questions, start=1):
            print(f"\nQ{idx}. {q['question']}")
            for i, opt in enumerate(q["options"], start=1):
                print(f"  {i}. {opt}")

            # Get user answer by number (1–4)
            while True:
                ans = input("Your answer (1-4): ").strip()
                if ans in {"1", "2", "3", "4"}:
                    ans_idx = int(ans) - 1
                    break
                print("Please enter 1, 2, 3, or 4.")

            # Check correctness
            if ans_idx == q["answer_index"]:
                self.right += 1
                self.total_score += self.score_per_question
                print("✅ Correct!")
            else:
                self.wrong += 1
                correct_num = q["answer_index"] + 1
                print(f"❌ Wrong. Correct answer: {correct_num}. {q['options'][q['answer_index']]}")

        # Summary
        print("\n=== Quiz Finished ===")
        print(f"Student: {self.full_name} (ID: {self.student_id})")
        print(f"Correct: {self.right}")
        print(f"Wrong:   {self.wrong}")
        print(f"Score per question: {self.score_per_question}")
        print(f"Total score: {self.total_score}")

    def reset_results(self):
        # Reset only attempt-related data
        self.right = 0
        self.wrong = 0
        self.total_score = 0


if __name__ == "__main__":
    quiz = Quiz(score_per_question=5)   # create quiz object
    quiz.personal_info()                # step 1: collect student info
    quiz.add_questions()                # step 2: add questions
    quiz.start_quiz()                   # step 3: run the quiz