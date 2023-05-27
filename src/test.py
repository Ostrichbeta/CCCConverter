import unittest
from ccccoverter.convert import *


class TestConvert(unittest.TestCase):
    def test_convert_single_syllable(self):
        self.assertEqual(convert_single_syllable('jung'), ['yung', 'yong'])

    def test_convert_single_character(self):
        self.assertEqual(convert_single_character('慈'), 'tsz/tszi/tszu/tsi/tsee/chz/chzi/chzu/chi/chee')

    def test_convert_sentence(self):
        self.assertEqual(convert_sentence('慈雲山子', only_keep_first_spell=False, only_keep_first_pronunciation=False),
                         'tsz/tszi/tszu/tsi/tsee/chz/chzi/chzu/chi/chee wan/wun/wen'
                         ' shaan/shan/saan/san tsz/tszi/tszu/tsi/tsee/chz/chzi/chzu'
                         '/chi/chee||chz/chzi/chzu/chi/chee/tsz/tszi/tszu/tsi/tsee')
        self.assertEqual(convert_sentence('慈雲山子', only_keep_first_spell=True, only_keep_first_pronunciation=False),
                         'tsz wan shaan tsz||chz')
        self.assertEqual(convert_sentence('慈雲山子', only_keep_first_spell=True, only_keep_first_pronunciation=True),
                         'tsz wan shaan tsz')

    def test_convert_sentence_map(self):
        self.assertEqual(convert_sentence_map('慈雲山子'),
                         [('慈', 'tsz/tszi/tszu/tsi/tsee/chz/chzi/chzu/chi/chee'),
                          ('雲', 'wan/wun/wen'),
                          ('山', 'shaan/shan/saan/san'),
                          ('子',
                           'tsz/tszi/tszu/tsi/tsee/chz/chzi/chzu/chi/chee||'
                           'chz/chzi/chzu/chi/chee/tsz/tszi/tszu/tsi/tsee')])


if __name__ == '__main__':
    unittest.main()
