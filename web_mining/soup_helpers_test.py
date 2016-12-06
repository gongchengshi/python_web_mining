# -*- coding: utf-8 -*-

from pprint import pprint
from bs4 import BeautifulSoup
import lxml
from html_table_parsing import table_to_list
from soup_helpers import *


def get_closest_subordinate_text_test():
    test1 = """
      <div>
        <span id="first span">
          <span>
            <span>this is the text</span>
            <span>this is not the text</span>
          </span>
        </span>
      </div>
    """

    test2 = """
      <div>
        <span id="first span">
          <span>
            <span>   &nbsp;</span>
            <span>this is the text</span>
            <span>this is not the text</span>
          </span>
        </span>
      </div>
    """

    test3 = """
      <div>
        <span id="first span">
          <span>
            this is the text
            <span>this is not the text</span>
          </span>
        </span>
      </div>
    """

    test10 = """
              <tr>
                <td align="right" bgcolor="#EEEEEE" colspan="2" nowrap valign="center">
                  <font class="text" id="key">Location</font>
                </td>
                <td align="left" bgcolor="#EEEEEE" nowrap valign="center">
                  <font class="text">Off County Road 320</font>
                </td>
                <td align="right" bgcolor="#EEEEEE" nowrap valign="center">
                  <font class="text">Phone</font>
                </td>
                <td align="left" bgcolor="#EEEEEE" colspan="3" nowrap valign="center">
                  <font class="text">(713) 425-6520</font>
                </td>
              </tr>
    """

    test11 = """
              <tr>
                <td align="right" bgcolor="#EEEEEE" colspan="2" nowrap valign="center">
                  <font class="text"><b id="key">Status</b></font>
                </td>
                <td align="right" bgcolor="#EEEEEE" colspan="3" nowrap valign="center">
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="left" bgcolor="#EEEEEE" nowrap valign="center">
                        <font class="text" color="#CC0000">Active</font>
                      </td>
                      <td align="right" bgcolor="#EEEEEE" nowrap valign="center">
                        <font class="text"><b id="key2">Last Update</b>
                                <font class="text" color="#CC0000">2013-08-27</font>
                              </font>
                      </td>
                      <td align="right" bgcolor="#EEEEEE" nowrap valign="center">
                        <font class="text"><b>Initial Release</b> <font class=
                        "text">2004-08-27</font></font>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
    """


    soup = BeautifulSoup(test1)
    element = soup.find(id="first span")
    closest_text = get_closest_subordinate_text(element)
    print closest_text
    assert closest_text == "this is the text"

    soup = BeautifulSoup(test2)
    element = soup.find(id="first span")
    closest_text = get_closest_subordinate_text(element)
    print closest_text
    assert closest_text == "this is the text"

    soup = BeautifulSoup(test3)
    element = soup.find(id="first span")
    closest_text = get_closest_subordinate_text(element)
    print closest_text
    assert closest_text == "this is the text"

    soup = BeautifulSoup(test10)
    element = soup.find(id="key")
    closest_text = get_closest_subordinate_text(element.next_element)
    print closest_text
    assert closest_text == "Off County Road 320"

    soup = BeautifulSoup(test11)
    element = soup.find(id="key")
    closest_text = get_closest_subordinate_text(element.next_element)
    print closest_text
    assert closest_text == "Active"

    soup = BeautifulSoup(test11)
    element = soup.find(id="key2")
    closest_text = get_closest_subordinate_text(element.next_element)
    print closest_text
    assert closest_text == "2013-08-27"


def parse_table_test():
    simplest = """
        <table>
            <tr>
                <td>Row 1 Col 1</td>
                <td colspan="2">Row 1 Col 2</td>
            </tr>
            <tr>
                <td>Row 2 Col 1</td>
                <td>Row 2 Col 2</td>
                <td>Row 2 Col 3</td>
            </tr>
        </table>
    """

    test1 = """
        <tr>
            <td align="right" bgcolor="#EEEEEE" colspan="2" rowspan="4" valign=
            "top">
              <font class="text" color="black"><b>Project Manager</b></font>
            </td>
            <td align="left" bgcolor="#EEEEEE" colspan="2" nowrap valign=
            "center">
              <font class="text" color="black">Medicine Bow Fuel &amp; Power
              LLC</font>
            </td>
            <td align="left" bgcolor="#EEEEEE" colspan="4" nowrap valign=
            "center">
              <font class="text" color="black">Jude Rolfes</font>
            </td>
          </tr>
          <tr>
            <td align="left" bgcolor="#EEEEEE" colspan="2" nowrap valign=
            "center">
              <font class="text" color="black">2 Riverway Suite 1780</font>
            </td>
            <td align="left" bgcolor="#EEEEEE" colspan="6" nowrap valign=
            "center">
              <font class="text" color="black">Vice President Of
              Engineering</font>
            </td>
          </tr>
          <tr>
            <td align="left" bgcolor="#EEEEEE" colspan="2" nowrap valign=
            "center">
              <font class="text" color="black">Houston, Texas 770561918</font>
            </td>
            <td align="left" bgcolor="#EEEEEE" colspan="6" nowrap valign=
            "center">
              <font class="text" color="black">[Tel.] (713) 425-6520</font>
            </td>
          </tr>
          <tr>
            <td align="left" bgcolor="#EEEEEE" colspan="2" nowrap valign=
            "center">
              <font class="text" color="black">U.S.A.</font>
            </td>
            <td align="left" bgcolor="#EEEEEE" colspan="6" nowrap valign=
            "center">
              <a href='mailto:jrolfes@dkrwaf.com' style='color: #000000' title=
              'This e-mail address is valid, but might have filters in place to block bulk e-mail'>
              <font class='text' color=
              'black'>jrolfes@dkrwaf.com</font></a>  <img src=
              '/images/icons/e-mails.gif' border='0' width='12' height='12'
              alt='(!)' title=
              'This e-mail address is valid, but might have filters in place to block bulk e-mail'>
            </td>
          </tr>
    """

    import lxml.html

    html = "<table>" + test1 + "</table>"

    # doc = lxml.html.fromstring(simplest)
    # doc = lxml.html.fromstring(html)

    #table = table_to_list(doc)
    #pprint(table)

    print get_cell_text(html, 0, 0).strip()

    print get_cell_text(html, 0, 2).strip()
    print get_cell_text(html, 0, 4).strip()

    print get_cell_text(html, 1, 2).strip()
    print get_cell_text(html, 1, 4).strip()

    print get_cell_text(html, 2, 2).strip()
    print get_cell_text(html, 2, 4).strip()

    print get_cell_text(html, 3, 2).strip()
    print get_cell_text(html, 3, 4).strip()

parse_table_test()
