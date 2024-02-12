from src.views.http_types.http_response import HttpResponse

from src.errors.error_types.http_unprocessable_entity_error import (
    HttpUnprocessableEntityError,
)


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        # enviar para um log
        # enviar um email de notificação
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Server error", "detail": str(error)}]},
    )
