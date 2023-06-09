import unittest

from mail import EmailExtractor

class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["janina.nowak@student.wat.edu.pl", True, False, "Janina", "Nowak"],
            ["adam.kowalski@wat.edu.pl", False, True, "Adam", "Kowalski"],
            ["katarzyna.szymanska@student.wat.edu.pl", True, False, "Katarzyna", "Szymanska"],
            ["michal.pawlowski@wat.edu.pl", False, True, "Michal", "Pawlowski"],
            ["agnieszka.wisniewska@student.wat.edu.pl", True, False, "Agnieszka", "Wisniewska"],
            ["pawel.adamczyk@wat.edu.pl", False, True, "Pawel", "Adamczyk"],
            ["monika.jakubowska@student.wat.edu.pl", True, False, "Monika", "Jakubowska"],
            ["bartosz.nowicki@wat.edu.pl", False, True, "Bartosz", "Nowicki"],
            ["anna.kowalczyk@student.wat.edu.pl", True, False, "Anna", "Kowalczyk"],
            ["marcin.wojcik@wat.edu.pl", False, True, "Marcin", "Wojcik"], ]


    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_male = x[2]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_male, extractor.is_male())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())