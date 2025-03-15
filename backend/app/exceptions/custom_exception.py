from fastapi import HTTPException, status


class BaseAPIException(HTTPException):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail_message: str = "Internal server error"

    def __init__(self, detail: str = None):
        super().__init__(
            status_code=self.status_code,
            detail=detail or self.detail_message
        )


class ResourceNotFoundException(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    detail_message = "Resource not found"


class BadRequestException(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail_message = "Bad request"


class UnauthorizedException(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail_message = "Unauthorized access"


class ForbiddenException(BaseAPIException):
    status_code = status.HTTP_403_FORBIDDEN
    detail_message = "Access forbidden"


class DatabaseException(BaseAPIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail_message = "Database error occurred"