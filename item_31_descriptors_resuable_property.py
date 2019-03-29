from weakref import WeakKeyDictionary


class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value

class OldExam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self.math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self.math_grade = value


class OldGrade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value


    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value


class LeakyExam(object):
    # class attributes. NOT instance attributes
    # The problem is that a single Grade instance is shared across all Exam 
    # instances for the class attribute writing_grade
    math_grade = OldGrade()
    writing_grade = OldGrade()
    science_grade = OldGrade()


class LeakyGrade(object):
    """will leak memory. The _values dict will hold a reference to every 
    instance of Exam ever passed to __set__ over the lifetime of the
    program. This causes instances to never have their reference count 
    go to zero preventing cleanup by the garbage collector
    """
    def __init__(self):
        self._values = {}

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

class Grade(object):
    """ use weakref that provides WeakKeyDictionary

    https://docs.python.org/3/library/weakref.html#weakref.WeakKeyDictionary

    python will do the bookkeeping for you and ensures that the _values
    dictionary will be empty whell Exam instances are no longer in use
    """
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


def main():
    # nick = Homework()
    # nick.grade = 95
    first_exam = Exam()
    first_exam.writing_grade = 82
    second_exam = Exam()
    second_exam.writing_grade = 75
    print('First', first_exam.writing_grade, 'is right')
    print('Second', second_exam.writing_grade, 'is right')


if __name__ == '__main__':
    main()
