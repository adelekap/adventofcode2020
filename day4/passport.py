from dataclasses import dataclass
from typing import List

REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
HAIRCOLOR_OPTIONS = {str(i) for i in range(10)}.union({'a', 'b', 'c', 'd', 'e', 'f'})
EYECOLOR_OPTIONS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


@dataclass
class Passport:
    passport_input: str

    @property
    def passport_details(self) -> dict:
        components = self.passport_input.split(' ')
        details = {}

        for component in components:
            key, value = component.split(':')
            details[key] = value

        return details

    @property
    def passport_fields(self) -> set:
        return set(self.passport_details.keys())

    @property
    def validations(self) -> List[bool]:
        return [self._birth_year_valid(),
                self._issue_year_valid(),
                self._expiration_year_valid(),
                self._height_valid(),
                self._haircolor_valid(),
                self._eyecolor_valid(),
                self._id_valid()]

    def _birth_year_valid(self) -> bool:
        byr = self.passport_details.get('byr', '0')
        return 1920 <= int(byr) <= 2002

    def _issue_year_valid(self) -> bool:
        iyr = self.passport_details.get('iyr', '0')
        return 2010 <= int(iyr) <= 2020

    def _expiration_year_valid(self) -> bool:
        eyr = self.passport_details.get('eyr', '0')
        return 2020 <= int(eyr) <= 2030

    def _height_valid(self) -> bool:
        hgt = self.passport_details.get('hgt', '')

        if 'cm' in hgt:
            return 150 <= int(hgt.split('cm')[0]) <= 193
        if 'in' in hgt:
            return 59 <= int(hgt.split('in')[0]) <= 76

        return False

    def _haircolor_valid(self) -> bool:
        hcl = self.passport_details.get('hcl', '')

        return hcl[0] == '#' and len(hcl) == 7 and len(set(hcl[1:]) - HAIRCOLOR_OPTIONS) == 0

    def _eyecolor_valid(self) -> bool:
        ecl = self.passport_details.get('ecl', '')
        return ecl in EYECOLOR_OPTIONS

    def _id_valid(self) -> bool:
        return len(self.passport_details.get('pid', '')) == 9

    def _all_fields_exist(self):
        return len(REQUIRED_FIELDS - self.passport_fields) == 0

    def valid(self) -> bool:
        return self._all_fields_exist() and all(self.validations)
