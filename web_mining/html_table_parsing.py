#!/usr/bin/env python
from collections import defaultdict
import lxml
from lxml import html


def table_to_2d_dict(table):
    result = defaultdict(lambda: defaultdict(unicode))
    for row_i, row in enumerate(table.xpath('./tr')):
        for col_i, col in enumerate(row.xpath('./td|./th')):
            colspan = int(col.get('colspan', 1))
            rowspan = int(col.get('rowspan', 1))
            col_data = unicode(col.text_content())
            while row_i in result and col_i in result[row_i]:
                col_i += 1
            for i in range(row_i, row_i + rowspan):
                for j in range(col_i, col_i + colspan):
                    result[i][j] = col_data
    return result


def parse_simple_table(table_string, has_headers=False):
    table = lxml.html.fromstring(table_string)

    handled_headers = False

    parsed_rows = []
    for row_i, row in enumerate(table.xpath('./tr')):
        if not handled_headers:
            if has_headers:
                headers = [unicode(col.text_content()) for col in row]
                handled_headers = True
                continue
            else:
                headers = range(0, len(row))
                handled_headers = True

        values = [unicode(col.text_content()) for col in row]
        parsed_rows.append(dict(zip(headers, values)))

    return parsed_rows


def parse_simple_table2(table_string, has_headers=False):
    from lxml import etree

    table = etree.XML(table_string)
    rows = iter(table)
    if has_headers:
        headers = [col.text for col in next(rows)]
    else:
        headers = range(0, len(next(rows)))
        rows = iter(table)

    parsed_rows = []

    for row in rows:
        values = [col.text for col in row]
        parsed_rows.append(dict(zip(headers, values)))
    return parsed_rows

def parse_horizonal_table(table_string):
    table = lxml.html.fromstring(table_string)

    parsed_rows = []
    for row_i, row in enumerate(table.xpath('./tr')):
        headers = [unicode(col.text_content()) for col in row]


        values = [unicode(col.text_content()) for col in row]
        parsed_rows.append(dict(zip(headers, values)))

    return parsed_rows
    pass



def iter_2d_dict(dct):
    for i, row in sorted(dct.items()):
        cols = []
        for j, col in sorted(row.items()):
            cols.append(col)
        yield cols

