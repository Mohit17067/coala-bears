import re

from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result


class CopyrightCheckBear(LocalBear):
    """
    Checks for copyright notice in a file.
    """
    LANGUAGES = {'All'}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'License'}

    def run(self, filename, file,
            author: str=''):
        """
        :param author: pass the name of the author
        """
        copyright_regexp = \
            r'Copyright\s+(\(C\)\s+)?\d{4}([-,]\d{4})*\s+%(author)s'
        re_copyright = re.compile(copyright_regexp %
                                  {'author': author}, re.IGNORECASE)
        message = ''
        if not(re_copyright.search(''.join(file))):
            message = 'Copyright notice not present.'

        yield Result(self, message)
