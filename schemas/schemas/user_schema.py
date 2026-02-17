def validate_user_structure(user):
    assert "id" in user
    assert "name" in user
    assert "username" in user
    assert "email" in user
