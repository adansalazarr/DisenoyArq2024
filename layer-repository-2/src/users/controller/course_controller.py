from flask import Blueprint, jsonify, request
from users.model.course_model import Course
from users.repository.course_repository import CourseRepository, LocalCourseRepository


blueprint = Blueprint('course_controller', __name__)
repository = LocalCourseRepository()

#Insert Course
@blueprint.route("/courses", methods=["POST"])
def insert_course():
    course_data = request.get_json()
    course = repository.add(course_data["name"], course_data["description"])
    if course is None:
        return jsonify({"Courso ya existe"})
    return jsonify(course)

#Cursos basados en id
@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    id = int(course_id)
    course = repository.get(course_id)
    if course is None:
        return jsonify({"Curso no encontrado"}), 404
    return jsonify(course)
