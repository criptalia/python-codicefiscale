# -*- coding: utf-8 -*-

from datetime import datetime

from codicefiscale import codicefiscale

import unittest


class CodiceFiscaleTestCase(unittest.TestCase):

    def test_encode_surname(self):

        data = [
            {
                'input':'',
                'result':'XXX',
            },
            {
                'input':'Caccamo',
                'result':'CCC',
            },
            {
                'input':'Fò',
                'result':'FOX',
            }
        ]

        for obj in data:
            # with self.subTest(obj=obj):
            self.assertEqual(
                codicefiscale.encode_surname(obj['input']),
                obj['result'])

    def test_encode_name(self):

        data = [
            {
                'input':'',
                'result':'XXX',
            },
            {
                'input':'Alessandro',
                'result':'LSN',
            },
            {
                'input':'Dario',
                'result':'DRA',
            },
            {
                'input':'Fabio',
                'result':'FBA',
            },
            {
                'input':'Giovanni',
                'result':'GNN',
            },
            {
                'input':'Hu',
                'result':'HUX',
            },
            {
                'input':'Maria',
                'result':'MRA',
            },
            {
                'input':'Michele',
                'result':'MHL',
            }
        ]

        for obj in data:
            # with self.subTest(obj=obj):
            self.assertEqual(
                codicefiscale.encode_name(obj['input']),
                obj['result'])

    def test_encode_birthdate_formats(self):

        data = [
            {
                'input':datetime(1985, 4, 3),
                'result':'85D03',
            },
            {
                'input':'03 04 1985',
                'result':'85D03',
            },
            {
                'input':'03/04/1985',
                'result':'85D03',
            },
            {
                'input':'03-04-1985',
                'result':'85D03',
            },
            {
                'input':'03.04.1985',
                'result':'85D03',
            },
            {
                'input':'3/4/1985',
                'result':'85D03',
            },
            {
                'input':'3-4-1985',
                'result':'85D03',
            },
            {
                'input':'3.4.1985',
                'result':'85D03',
            },
            {
                'input':'1985 04 03',
                'result':'85D03',
            },
            {
                'input':'1985/04/03',
                'result':'85D03',
            },
            {
                'input':'1985-04-03',
                'result':'85D03',
            },
            {
                'input':'1985.04.03',
                'result':'85D03',
            },
            {
                'input':'1985/4/3',
                'result':'85D03',
            },
            {
                'input':'1985-4-3',
                'result':'85D03',
            },
            {
                'input':'1985.4.3',
                'result':'85D03',
            },
        ]

        for obj in data:
            # with self.subTest(obj=obj):
            self.assertEqual(
                codicefiscale.encode_birthdate(obj['input'], 'M'),
                obj['result'])

    def test_encode_birthdate_sex(self):

        data = [
            {
                'input':['03/04/1985', 'M'],
                'result':'85D03',
            },
            {
                'input':['03/04/1985', 'F'],
                'result':'85D43',
            },
        ]

        for obj in data:
            # with self.subTest(obj=obj):
            self.assertEqual(
                codicefiscale.encode_birthdate(*obj['input']),
                obj['result'])

    def test_encode_birthplace_italy(self):

        data = [
            {
                'input':'Torino, Italy',
                'result':'L219',
            },
            {
                'input':'Torino (TO), Italy',
                'result':'L219',
            },
            {
                'input':'Torino (TO)',
                'result':'L219',
            },
            {
                'input':'Torino',
                'result':'L219',
            },
            {
                'input':'L219',
                'result':'L219',
            },
        ]

        for obj in data:
            # with self.subTest(obj=obj):
            self.assertEqual(
                codicefiscale.encode_birthplace(obj['input']),
                obj['result'])

    def test_encode_birthplace_foreign_country(self):

        data = [
            {
                'input':'Lettonia',
                'result':'Z145',
            },
            {
                'input':'Giappone',
                'result':'Z219',
            },
            {
                'input':'Marocco',
                'result':'Z330',
            },
        ]

        for obj in data:
            # with self.subTest(obj=obj):
            self.assertEqual(
                codicefiscale.encode_birthplace(obj['input']),
                obj['result'])

    def test_encode_cin(self):

        data = [
            {
                'input':'CCCFBA85D03L219',
                'result':'P',
            },
        ]

        for obj in data:
            # with self.subTest(obj=obj):
            self.assertEqual(
                codicefiscale.encode_cin(obj['input']),
                obj['result'])

    def test_encode(self):

        data = [
            {
                'input': { 'surname':'Ait Hadda', 'name':'Saad', 'sex':'M', 'birthdate':'08/09/1995', 'birthplace':'Marocco' },
                'result':'THDSDA95P08Z330H',
            },
            {
                'input': { 'surname':'Belousovs', 'name':'Olegs', 'sex':'M', 'birthdate':'22/03/1984', 'birthplace':'Lettonia' },
                'result':'BLSLGS84C22Z145O',
            },
            {
                'input': { 'surname':'Bruno', 'name':'Giovanni', 'sex':'M', 'birthdate':'26/02/1971', 'birthplace':'Torino' },
                'result':'BRNGNN71B26L219T',
            },
            {
                'input': { 'surname':'Caccamo', 'name':'Fabio', 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
                'result':'CCCFBA85D03L219P',
            },
            {
                'input': { 'surname':'Gomba', 'name':'Alessandro', 'sex':'M', 'birthdate':'05/01/1984', 'birthplace':'Pinerolo' },
                'result':'GMBLSN84A05G674H',
            },
            {
                'input': { 'surname':'Martini', 'name':'Maria', 'sex':'F', 'birthdate':'16/12/1983', 'birthplace':'Anagni' },
                'result':'MRTMRA83T56A269B',
            },
            {
                'input': { 'surname':'Panella', 'name':'Michele', 'sex':'M', 'birthdate':'27/10/1979', 'birthplace':'San Severo (FG)' },
                'result':'PNLMHL79R27I158P',
            },
            {
                'input': { 'surname':'Quatrini', 'name':'Dario', 'sex':'M', 'birthdate':'13/09/1971', 'birthplace':'Pavia' },
                'result':'QTRDRA71P13G388J',
            },
            {
                'input': { 'surname':'Takakura', 'name':'Yuuki', 'sex':'F', 'birthdate':'28/02/1987', 'birthplace':'Torino' },
                'result':'TKKYKU87B68L219F',
            },
        ]

        for obj in data:
            # with self.subTest(obj=obj):
            self.assertEqual(
                codicefiscale.encode(**obj['input']),
                obj['result'])

    def test_decode(self):

        data = [
            {
                'input':'THDSDA95P08Z330H',
                'result': { 'sex':'M', 'birthdate':'08/09/1995', 'birthplace':'Marocco' },
            },
            {
                'input':'BLSLGS84C22Z145O',
                'result': { 'sex':'M', 'birthdate':'22/03/1984', 'birthplace':'Lettonia' },
            },
            {
                'input':'BRNGNN71B26L219T',
                'result': { 'sex':'M', 'birthdate':'26/02/1971', 'birthplace':'Torino' },
            },
            {
                'input':'CCCFBA85D03L219P',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
            {
                'input':'GMBLSN84A05G674H',
                'result': { 'sex':'M', 'birthdate':'05/01/1984', 'birthplace':'Pinerolo' },
            },
            {
                'input':'MRTMRA83T56A269B',
                'result': { 'sex':'F', 'birthdate':'16/12/1983', 'birthplace':'Anagni' },
            },
            {
                'input':'PNLMHL79R27I158P',
                'result': { 'sex':'M', 'birthdate':'27/10/1979', 'birthplace':'San Severo' },
            },
            {
                'input':'QTRDRA71P13G388J',
                'result': { 'sex':'M', 'birthdate':'13/09/1971', 'birthplace':'Pavia' },
            },
            {
                'input':'TKKYKU87B68L219F',
                'result': { 'sex':'F', 'birthdate':'28/02/1987', 'birthplace':'Torino' },
            },
        ]

        for obj in data:
            # with self.subTest(obj=obj):

            obj_decoded = codicefiscale.decode(obj['input'])
            # print(obj_decoded)

            self.assertEqual(
                obj_decoded['sex'],
                obj['result']['sex'])

            self.assertEqual(
                obj_decoded['birthdate'],
                datetime.strptime(obj['result']['birthdate'], '%d/%m/%Y'))

            self.assertEqual(
                obj_decoded['birthplace']['name'].upper(),
                obj['result']['birthplace'].upper())

    def test_omocodia(self):

        data = [
            {
                'input':'CCCFBA85D03L219P',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
            {
                'input':'CCCFBA85D03L21VE',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
            {
                'input':'CCCFBA85D03L2MVP',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
            {
                'input':'CCCFBA85D03LNMVE',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
            {
                'input':'CCCFBA85D0PLNMVA',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
            {
                'input':'CCCFBA85DLPLNMVL',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
            {
                'input':'CCCFBA8RDLPLNMVX',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
            {
                'input':'CCCFBAURDLPLNMVU',
                'result': { 'sex':'M', 'birthdate':'03/04/1985', 'birthplace':'Torino' },
            },
        ]

        for obj in data:
            # with self.subTest(obj=obj):

            obj_decoded = codicefiscale.decode(obj['input'])
            # print(obj_decoded)

            self.assertEqual(
                obj_decoded['sex'],
                obj['result']['sex'])

            self.assertEqual(
                obj_decoded['birthdate'],
                datetime.strptime(obj['result']['birthdate'], '%d/%m/%Y'))

            self.assertEqual(
                obj_decoded['birthplace']['name'].upper(),
                obj['result']['birthplace'].upper())

    def test_is_valid(self):

        self.assertTrue(codicefiscale.is_valid('CCCFBA85D03L219P'))
        self.assertTrue(codicefiscale.is_valid('CCC FBA 85 D03 L219 P'))
        self.assertTrue(codicefiscale.is_valid('CCC-FBA-85-D03-L219-P'))

        self.assertFalse(codicefiscale.is_valid('CCCFBA85D03L219PP')) # too long
        self.assertFalse(codicefiscale.is_valid('CCCFBA85D03L219B')) # wrong CIN
        self.assertFalse(codicefiscale.is_valid('CCCFBA85D03L219')) # too short
        self.assertFalse(codicefiscale.is_valid('CCCFBA85D00L219')) # wrong birthdate day
        self.assertFalse(codicefiscale.is_valid('CCCFBA85D99L219')) # wrong birthdate day


if __name__ == '__main__':
    unittest.main()