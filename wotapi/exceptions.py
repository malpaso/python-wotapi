class WotApiException(Exception): pass


class SystemException(WotApiException): pass


class HTTPRequestException(SystemException): pass

_ERROR_MAP = {
    0: SystemException,
}


def exception_for_code(code):
    return _ERROR_MAP[code]
