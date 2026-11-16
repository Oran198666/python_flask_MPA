from http import HTTPStatus
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from services.product_service import NotFoundError
from models.errors import NotFoundError


def register_exception_handler(server: Flask) -> None:

    @server.errorhandler(NotFoundError)
    def not_found_handler(err: NotFoundError):
        print("Error: " + str(err))
        return jsonify({"message": str(err)}), HTTPStatus.NOT_FOUND

    @server.errorhandler(HTTPException)
    def http_exception_handler(err: HTTPException):
        print("Error: " + str(err))
        return jsonify({"message": err.description}), err.code

    @server.errorhandler(Exception)
    def catch_all_handler(err: Exception):
        print("Error: " + str(err))
        return jsonify({"message": str(err)}), HTTPStatus.INTERNAL_SERVER_ERROR