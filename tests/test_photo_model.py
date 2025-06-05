import pytest

from .factories import PhotoFactory, PhotoFileFactory

@pytest.mark.django_db
def test_has_photo_files_property():
    photo = PhotoFactory()
    assert photo.has_photo_files is False

    PhotoFileFactory(photo=photo)
    photo.refresh_from_db()
    assert photo.has_photo_files is True
