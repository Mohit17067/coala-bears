import os
from queue import Queue

from bears.general.CopyrightCheckBear import CopyrightCheckBear
from coalib.testing.LocalBearTestHelper import LocalBearTestHelper
from coalib.testing.BearTestHelper import generate_skip_decorator
from coalib.results.Result import Result
from coalib.settings.Section import Section


def get_testfile_path(name):
    return os.path.join(os.path.dirname(__file__),
                        'copyrightcheck_test_files',
                        name)


def load_testfile(name):
    with open(get_testfile_path(name)) as f:
        output = f.readlines()
    return output


@generate_skip_decorator(CopyrightCheckBear)
class CopyrightCheckBearTest(LocalBearTestHelper):

    def setUp(self):
        self.uut = CopyrightCheckBear(Section('name'), Queue())

    def copyright_without_author(self):
        file_contents = load_testfile('copyright_without_author.java')
        self.check_results(
            self.uut,
            file_contents,
            [],
            filename=get_testfile_path('copyright_without_author.java'))

    def copyright_with_author(self):
        file_contents = load_testfile('copyright_with_author.txt')
        self.check_results(
            self.uut,
            file_contents,
            [],
            filename=get_testfile_path('copyright_with_author.txt'),
            settings={'author': 'The coala developers'})

    def no_copyright(self):
        file_contents = load_testfile('no_copyright.py')
        self.check_results(
            self.uut,
            file_contents,
            [Result.from_values('CopyrightCheckBear',
                                'Copyright notice not present.',
                                file=get_testfile_path('no_copyright.py'))],
            filename=get_testfile_path('no_copyright.py'))
