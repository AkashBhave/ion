import logging
import re

logger = logging.getLogger(__name__)


class StripNewlinesMiddleware(object):
    """Strip extra newlines from rendered templates to
    enhance readability.
    """
    def process_response(self, request, response):
        if response["Content-Type"] == "text/html":
            response.content = re.sub(r'\n(\s*)\n', '\n', response.content)
            response.content = re.sub(r'^(\s*)\n', '', response.content)
        return response
