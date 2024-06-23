import logging
from time import perf_counter

logger = logging.getLogger(__name__)


class RequestTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request, *args: logging.Any, **kwds: logging.Any) -> logging.Any:
        start_time = perf_counter()
        response = self.get_response(request)
        elapsed_time = perf_counter() - start_time
        logger.info(
            f"Endpoint: {request.path}, Request processed in {elapsed_time} seconds"
        )
        # дописываем в http-ответ заголовок со временем выполнения запроса
        response["X-Elapsed-Time"] = str(elapsed_time)

        return response
