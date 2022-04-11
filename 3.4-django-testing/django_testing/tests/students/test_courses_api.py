import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_exact_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/courses/2/')

    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_courses_list(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/courses/')

    # Assert
    data = response.json()
    assert len(data) == len(courses)


# @pytest.mark.django_db
# def test_id_filter(client, course_factory):
#     # Arrange
#     courses = course_factory(_quantity=10)
#     course = Course.objects.first()
#
#     # Act
#     response = client.get(f'/courses/?id={course.id}/')
#
#     # Assert
#     assert response.status_code == 200
#     assert response.data[0].get('id') == course.id
#
#     # возникает ошибка "bad request"


# @pytest.mark.django_db
# def test_name_filter(client, course_factory):
#     # Arrange
#     courses = course_factory(_quantity=10)
#     course = Course.objects.first()
#
#     # Act
#     response = client.get(f'/courses/?name={course.name}/')
#
#     # Assert
#     assert response.status_code == 200
#     assert response.data[0].get('name') == course.name


@pytest.mark.django_db
def test_success_create(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.post('/courses/', {
        'name': 'HTML',
        'students': [],
    })

    # Assert
    assert response.status_code == 201


@pytest.mark.django_db
def test_success_update(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    course = Course.objects.first()

    # Act
    response = client.patch(f'/courses/{course.id}/', name='css')

    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_success_delete(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    course = Course.objects.first()

    # Act
    response = client.delete(f'/courses/{course.id}/', {
        'name': 'css',
    })

    # Assert
    assert response.status_code == 204

