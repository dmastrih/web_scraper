import requests

from bs4 import BeautifulSoup as bs_four


def create_parser(site_url: str) -> list:
    """
    This function takes a link to the site and sends a request to the specified url
    and returns a list with found "a" tags.

    :param site_url: string
    :return: list
    """

    res = requests.get(site_url).text
    soup = bs_four(res, "html.parser")

    return soup.find_all("a")


def check_url(tags_a_list: list) -> set:
    """
    The function gets the value from 'href', checks for the occurrence of "http" in the link
    and then truncates the link to the main page of the site.
    The function returns a set of links.

    :param tags_a_list: list
    :return: set
    """

    set_url = set()

    for tag_a in tags_a_list:
        url = tag_a.get("href")

        if "http" in url:
            ind = url.find("/", 8)

            if ind > 0:
                url = url[:ind + 1]
                set_url.add(url)

    return set_url


def check_link_from_2_site(set_url: set):
    """
    The function receives a link to a site from the set and creates a parser for it after this checks by condition
    and adds the result to the list. Otherwise, an error message is displayed.
    At the end of the function a list is returned.

    :param set_url: set
    :return: list
    """

    list_url_2_site = []

    for url in set_url:

        try:
            a_list = create_parser(url)
            res = check_url(a_list)
            list_url_2_site.append(res)
        except:
            print(f"There was an error when we connected to the a site from the base site list")

    return list_url_2_site


if __name__ == "__main__":
    URL = "https://bigwood.ru/"

    answer = input("Сonsole or File? :")

    base_url = create_parser(URL)
    set_for_first_url = check_url(base_url)
    list_of_sets = check_link_from_2_site(set_for_first_url)

    if answer == 'Console':

        for first_url in set_for_first_url:
            print(first_url)

        for list_of_set in list_of_sets:
            for link in list_of_set:
                print(link)

    elif answer == 'File':

        with open("file.txt", "w") as our_file:

            for first_url in set_for_first_url:
                our_file.write(first_url + "\n")

            for list_of_set in list_of_sets:
                for link in list_of_set:
                    our_file.write(link + "\n")
    else:
        print("Your value is not correct")
