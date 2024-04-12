import abc
from users.model.course_model import Course


class CourseRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, name: str, description: str) -> Course:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id: int) -> Course:
        raise NotImplementedError


class LocalCourseRepository(CourseRepository):

    def __init__(self):
        self.courses = []

    def add(self, name: str, description: str) -> Course:
        if any(course.name == name for course in self.courses): #verificamos que no duplique
            return None
        new_course = Course( #nuevo curso
            id=len(self.courses) + 1,
            name=name,
            description=description
        )
        self.courses.append(new_course)
        return new_course

    def get(self, id: int) -> Course:
        return next((course for course in self.courses if course.id == id), None)
