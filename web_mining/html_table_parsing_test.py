from pprint import pprint
from html_table_parsing import *

s = """<table>
  <tr><th>Event</th><th>Start Date</th><th>End Date</th></tr>
  <tr><td>a</td><td>b</td><td>c</td></tr>
  <tr><td>d</td><td>e</td><td>f</td></tr>
  <tr><td>g</td><td>h</td><td>i</td></tr>
</table>
"""

s1 = """
    <table border="0" cellpadding="3" cellspacing="1" width="100%">
    <tr>
        <td align="right" bgcolor="CCCCCC" nowrap="" valign="middle" width="15%"><font class="text"><b>Title</b></font></td>
        <td align="left" bgcolor="CCCCCC" nowrap="" valign="middle" width="25%"><font class="text"><b>Contact</b></font></td>
        <td align="left" bgcolor="CCCCCC" nowrap="" valign="middle" width="10%"><font class="text"><b>QC Date</b></font></td>
        <td align="left" bgcolor="CCCCCC" nowrap="" valign="middle" width="15%"><font class="text"><b>Telephone</b></font></td>
        <td align="left" bgcolor="CCCCCC" nowrap="" valign="middle" width="10%"><font class="text"><b>On-Site</b></font></td>
        <td align="left" bgcolor="CCCCCC" colspan="2" nowrap="" valign="middle" width="25%"><font class="text"><b>E-Mail</b></font></td>
    </tr>
    <tr>
        <td align="right" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Plant Manager</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Wade Cline</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Mar-2013</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">(713) 425-6520 </font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Yes</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width="25%"><font class='text'><a href='mailto:wcline@drkwf.com'>wcline@drkwf.com</a></font></td>
    </tr>
    <tr>
        <td align="right" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Maintenance Manager</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Jon Doyle</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Dec-2012</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">() 425-6520 </font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Yes</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width="25%"></td>
    </tr>
    <tr>
        <td align="right" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Utilities Manager</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Robert Kelly</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">Dec-2012</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">(713) 425-6520 103</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width=""><font class="text">No</font></td>
        <td align="left" bgcolor="EEEEEE" nowrap="" valign="middle" width="25%"><font class='text'><a href='mailto:rkelly@dkrwf.com'>rkelly@dkrwf.com</a></font></td>
    </tr>
    </table>
    """

def test_parse_simple_table_s1():
    result = parse_simple_table(s1, has_headers=True)
    pprint(result)

    result = parse_simple_table(s1, has_headers=False)
    pprint(result)

def test_parse_simple_table():
    result = parse_simple_table(s, has_headers=True)
    pprint(result)

    result = parse_simple_table(s, has_headers=False)
    pprint(result)


def test_table_to_2d_dict():
    import lxml.html
    from pprint import pprint

    doc = lxml.html.parse('tables.html')
    for table_el in doc.xpath('//table'):
        dct = table_to_2d_dict(table_el)
        table = list(iter_2d_dict(dct))
        pprint(table)


test_parse_simple_table_s1()
