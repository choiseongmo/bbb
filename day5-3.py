class Student:
    def __init__(self, number):
        self.number = number
        self.korean_score = 0
        self.english_score = 0
        self.math_score = 0

    def input_scores(self):
        self.korean_score = int(input(f"{self.number}번째 학생의 국어 성적 입력: "))
        self.english_score = int(input(f"{self.number}번째 학생의 영어 성적 입력: "))
        self.math_score = int(input(f"{self.number}번째 학생의 수학 성적 입력: "))
        self.calculate_and_print_average()

    def calculate_and_print_average(self):
        average = (self.korean_score + self.english_score + self.math_score) / 3
        print(f"{self.number}번째 학생의 평균 점수: {average}")


def main():
    num_students = int(input("학생 수 입력(N): "))

    for i in range(1, num_students + 1):
        student = Student(i)
        student.input_scores()


if __name__ == "__main__":
    main()