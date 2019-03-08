import collections


Grade = collections.namedtuple('Grade', ('score', 'weight'))


class SimpleWeightedGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        # setdefault(subject, [])
        # get the key 'subject', if key not available,
        # add key subject and set its value to []
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, weights_scores in by_subject.items():
            sum_weight_dot_score = sum(
                score * weight for score, weight in weights_scores
            )
            total_weight = sum(weight for _, weight in weights_scores)

            subject_avg = sum_weight_dot_score / total_weight
            score_sum += subject_avg
            score_count += 1
        return score_sum / score_count


# Better approach

class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class GradeBook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


if __name__ == '__main__':
    old_book = SimpleWeightedGradebook()
    old_book.add_student('Nick')
    old_book.report_grade('Nick', 'Math', 90, 1)
    old_book.report_grade('Nick', 'Math', 80, 3)
    old_book.report_grade('Nick', 'Math', 70, 2)

    print(old_book.average_grade('Nick'))

    good_book = GradeBook()
    nick = good_book.student('Nick')
    math = nick.subject('Math')
    math.report_grade(90, 1)
    math.report_grade(80, 3)
    math.report_grade(70, 2)

    print(nick.average_grade())
