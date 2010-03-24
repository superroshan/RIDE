#  Copyright 2008 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
import unittest

from robot.utils.asserts import assert_equals

from resources import PYAPP_REFERENCE as _ #Needed to be able to create wx components
from robotide.editor.clipboard import _GridClipboard


class TestGridClipBoard(unittest.TestCase):

    def test_with_string_content(self):
        self._test_clipboard('Hello, world!', 'Hello, world!')

    def test_with_list_content(self):
        self._test_clipboard([['Hello', 'world!']], 'Hello\tworld!')

    def test_with_multiple_rows(self):
        self._test_clipboard([['Hello', 'world!'], ['Another', 'row']],
                             'Hello\tworld!\nAnother\trow')

    def test_with_invalid_data(self):
        self._test_clipboard(_GridClipboard())

    def _test_clipboard(self, content, expected=''):
        clipb = _GridClipboard()
        clipb.set_contents(content)
        assert_equals(clipb._get_value_from_clipboard(),
                      expected.replace('\n', os.linesep))


if __name__ == '__main__':
    unittest.main()
