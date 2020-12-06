def load_questions_part_1(filename):
    with open(filename) as f:
        answers = set()
        sum_of_answered_questions = 0
        for line in f:
            if line == "\n":
                sum_of_answered_questions += len(answers)
                answers.clear()
                continue
            else:
                split_line = list(line.strip())
                for letter in split_line:
                    answers.add(letter)

        sum_of_answered_questions += len(answers)
        print(sum_of_answered_questions)


def load_questions_part_2(filename):
    from collections import Counter

    with open(filename) as f:
        answers = {}
        sum_of_answered_questions = 0
        num_of_people_in_group = 0
        for line in f:
            if line == "\n":
                c = Counter(answers)
                # num_of_answered_questions_by_group = 0
                for num in c.values():
                    if num == num_of_people_in_group:
                        sum_of_answered_questions += 1
                answers.clear()
                num_of_people_in_group = 0
                continue
            else:
                num_of_people_in_group += 1
                split_line = list(line.strip())
                for letter in split_line:
                    if letter in answers:
                        answers[letter] += 1
                    else:
                        answers[letter] = 1

        c = Counter(answers)
        for num in c.values():
            if num == num_of_people_in_group:
                sum_of_answered_questions += 1

        print(sum_of_answered_questions)


load_questions_part_2("input.txt")
