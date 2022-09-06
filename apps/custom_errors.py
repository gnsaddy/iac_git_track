import sys
from django.http import JsonResponse
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CustomError(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    @classmethod
    def unauthorized(cls, err):
        """ 401 Unauthorized """
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "401"
        }), 401
        return response

    @classmethod
    def forbidden(cls, err):
        """ 403 Forbidden """
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "403"
        }), 403
        return response

    @classmethod
    def not_found(cls, err):
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "404"
        }), 404
        return response

    @classmethod
    def server_error(cls, err):
        """ 500 Internal Server Error """
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "500"
        }), 500
        return response

    @classmethod
    def not_implemented(cls, err):
        """ 501 Not Implemented """
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "501"
        }), 501
        return response

    @classmethod
    def service_unavailable(cls, err):
        """ 503 Service Unavailable """
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "503"
        }), 503
        return response

    @classmethod
    def bad_gateway(cls, err):
        """ 502 Bad Gateway """
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "502"
        }), 502
        return response

    @classmethod
    def gateway_timeout(cls, err):
        """ 504 Gateway Timeout """
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "504"
        }), 504
        return response

    @classmethod
    def bad_request(cls, err):
        """ 400 Bad Request """
        ex_type, ex_value, ex_traceback = sys.exc_info()
        logger.exception("Exception type : %s " % ex_type.__name__)
        logger.exception("Exception message : %s" % ex_value.__str__())
        logger.exception("Exception line number : %s" %
                         ex_traceback.tb_lineno.__str__())
        response = JsonResponse({
            "status": "fail",
            "message": "error",
            "data": "error fetching result",
            "error_type": ex_type.__name__,
            "error": str(err),
            "error_code": "400"
        }), 400
        return response
