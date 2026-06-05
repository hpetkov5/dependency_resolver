# dependency_resolver

This project implements a simple dependency resolver using Topological Sorting.
It reads package definitions from a JSON file, resolves all dependencies for a given package, and returns the correct installation order.

## Installation

### Requirements
- Python 3.11 or higher

### Install locally

Clone the repository and install the package.

## Usage

How the program works

### Load JSON data
```python
prepare_data()
```
Read the JSON file and convert the data into dictionary.
```python
{
  "A": ["B", "D", "E"],
  "B": ["F"],
  ...
}
```
### Topological sort
```python
topo_sort(data, start_node, visited, result)
```
Performs a Depth-First Search which visits all dependencies before adding the package itself.
### Dependency Resolution
```python
dependency_resolver(package_name)
```
Entry point of the program which calls topo_sort and returns ordered list of dependencies.

## Example Usage

### Call
```python
dependency_resolver("B")
```
### Output
```python
["F", "B"]
```