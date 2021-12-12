"""
Advent of code, day 12 - Passage Pathing

https://adventofcode.com/2021/day/12
"""
import fileinput
import collections


if __name__ == "__main__":
    graph = collections.defaultdict(list)
    for line in fileinput.input():
        c_from, c_to = line.strip().split("-")
        if c_to != "start":
            graph[c_from].append(c_to)
        if c_from != "start":
            graph[c_to].append(c_from)
    graph.pop("end")

    def dfs(node, visited, one_off):
        if node == "end":
            return 1
        if node.islower():
            visited.add(node)

        total = sum(dfs(n, visited, one_off) for n in graph[node] if not n in visited)

        if one_off == " ":
            total += sum(
                dfs(n, visited, n) for n in graph[node] if n in visited and n != "start"
            )

        if node != one_off:
            visited.discard(node)
        return total

    p1 = dfs("start", set(), "")
    p2 = dfs("start", set(), " ")
    print(f"{p1=}, {p2=}")
