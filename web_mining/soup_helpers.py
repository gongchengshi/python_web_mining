from bs4 import BeautifulSoup, NavigableString
from collections import deque
import lxml.html


def breadth_first_search(element, criteria, accessor):
    q = deque()
    q.append(element)
    while len(q):
        e = q.popleft()
        if criteria(e):
            return accessor(e)
        for child in e.findAll(recursive=False):
            q.append(child)


def get_closest_subordinate_text(element):
    e = element.next_element
    while e:
        text = e.string and e.string.strip()
        if text:
            return text
        e = e.next_element
    return None


def find_direct_text(soup, name, text):
    found = [tag for tag in soup.find_all(name, text=text) if isinstance(tag.contents[0], NavigableString)]
    return found[0] if found else None


def soup_between(start_element, end_element, tag=None, include_start=False):
    siblings = []

    current = start_element if include_start else start_element.find_next_sibling(tag)

    while current != end_element:
        siblings.append(current)
        current = current.find_next_sibling(tag)

    return siblings


def html_between(start_element, end_element, tag=None, include_start=False):
    return "".join([str(s) for s in soup_between(start_element, end_element, tag, include_start)])
