"""Custom exceptions"""

import werkzeug.exceptions as wexc


class FlaskSmorestError(Exception):
    """Generic flask-smorest exception"""


class OpenAPIVersionNotSpecified(FlaskSmorestError):
    """OpenAPI version was not specified"""


class CheckEtagNotCalledError(FlaskSmorestError):
    """ETag enabled on resource but check_etag not called"""


class NotModified(wexc.HTTPException, FlaskSmorestError):
    """Resource was not modified (Etag is unchanged)

    Exception created to compensate for a lack in Werkzeug (and Flask)
    """
    code = 304
    description = 'Resource not modified since last request.'


class PreconditionRequired(wexc.PreconditionRequired, FlaskSmorestError):
    """Etag required but missing"""
    # Overriding description as we don't provide If-Unmodified-Since
    description = (
        'This request is required to be conditional; try using "If-Match".')


class PreconditionFailed(wexc.PreconditionFailed, FlaskSmorestError):
    """Etag required and wrong ETag provided"""