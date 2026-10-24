#!/usr/bin/env python3
import pytest
from flask import Flask
from models import db

@pytest.fixture(scope="function")
def test_client():
    test_app = Flask(__name__)
    test_app.config["TESTING"] = True
    test_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    test_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(test_app)

    with test_app.app_context():
        db.create_all()

        yield test_app.test_client()

        db.session.remove()
        db.drop_all()
