"""
This module defines Dependency resolver functionality
"""

import json


def create_dict_from_json() -> dict:
    """
    Function to read JSON data and returns it
    :return prepared_json_data: JSON data as dictionary
    """
    with open ("package.JSOn", mode="r", encoding="utf-8") as json_file:
        raw_data = json.load(json_file)

    prepared_json_data = {}
    for pkg in raw_data["packages"]:
        prepared_json_data[pkg["name"]] = pkg["requires"]
    return prepared_json_data


def topo_sort(data: dict, start_node: str, visited: list, result: list) -> None:
    """
    Topological sort using the Depth First Search algorithm
    :param data: dictionary with dependancy information
    :param starting_node: starting point (package) for the sort
    :param visited: empty list to track visited nodes
    :param result: empty list to fill dependencies
    """
    if start_node in visited:
        return

    visited.append(start_node)

    for dep in data.get(start_node, []):
        topo_sort(data, dep, visited, result)

    result.append(start_node)


def dependency_resolver(package_name: str) -> list:
    """
    Function receives package_name, then calls topo_sort on that package.
    :param package_name: package name input as str
    :return dependency_list: list of all dependencies of the input package
    """
    json_data_as_dict = create_dict_from_json()

    dependency_list = []
    visited = []

    topo_sort(json_data_as_dict, package_name, visited, dependency_list )

    return dependency_list
