#!/usr/bin/env python

#Author: nhny at hcmut.edu.vn
#Course: AI 2016
#Lab 3
from sys import argv
from time import time
from node import *

class Searcher(object):
    """Searcher that manuplate searching process."""

    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def print_path(self, state):
        path = []
        while state:
            path.append(state)
            state = state.prev
        path.reverse()
        print("\n-->\n".join([str(state) for state in path]))

    def dfs(self, depth = 100):
        stack = [self.start]
        visited = set()
        found = False

        while stack:
            state = stack.pop()

            if state == self.goal:
                found = state
                break

            if state in visited or state.step > depth:
                continue

            visited.add(state)

            for s in state.next():
                stack.append(s)

        if found:
            self.print_path(found)
            print "Find solution"
        else:
            print("No solution found")

    def bfs(self, depth = 50):
        """Run Breadth-first search."""
        #TODO: Implement breadth first search
        queue = [self.start]
        visited = set()
        found = False

        while queue:
            state = queue.pop()

            if state == self.goal:
                found = state
                break

            if state in visited or state.step > depth:
                continue

            visited.add(state)

            for s in state.next():
                queue.insert(0, s)

        if found:
            self.print_path(found)
            print "Find solution"
        else:
            print("No solution found")

    def steepest_ascent_hill_climbing(self):
        """Run hill climbing search."""
        #TODO Implement hill climbing.
        stack = [self.start]

        while stack:
            state = stack.pop()
            if state == self.goal:
                self.print_path(state)
                print "Find solution"
                break

            h_val = state.manhattan_distance() + state.hamming_distance()
            next_state = False
            for s in state.next():
                h_val_next = s.manhattan_distance() + s.hamming_distance()
                if h_val_next < h_val:
                    next_state = s
                    h_val = h_val_next

            if next_state: 
                stack.append(next_state)
            else:
                self.print_path(state)
                print "Cannot find solution"


    # I don't know this function
    def hill_climbing(self, depth = 100):
        """Run steepest ascent hill climbing search."""
        #TODO Implement hill climbing.
        stack = [self.start]
        visited = set()

        while stack:
            state = stack.pop()
            if state == self.goal:
                self.print_path(state)
                print "Find solution"
                break

            if state in visited or state.step > depth:
                self.print_path(state)
                print "Cannot find solution"
                continue

            visited.add(state)

            h_val = 50
            next_state = False
            for s in state.next():
                h_val_next = s.manhattan_distance() + s.hamming_distance()
                if h_val_next < h_val:
                    next_state = s
                    h_val = h_val_next

            stack.append(next_state)
            
    def astar(self, depth = 75):
        """Run A* search."""
        #TODO: Implement a star search.
        priotity_queue = PriorityQueue()
        h_val = self.start.manhattan_distance() + self.start.hamming_distance()
        # g_val always is start.step
        f_val = h_val + self.start.step
        priotity_queue.push(self.start, f_val)
        visited = set()
        found = False

        while not priotity_queue.isEmpty():
            state = priotity_queue.pop()

            if state == self.goal:
                found = state
                break

            if state in visited or state.step > depth:
                continue

            visited.add(state)

            for s in state.next():
                h_val_s = s.manhattan_distance() + s.hamming_distance()
                f_val_s = h_val_s + s.step
                priotity_queue.push(s, f_val_s)

        if found:
            self.print_path(found)
            print "Find solution"
        else:
            print("No solution found")


if __name__ == "__main__":
    script, strategy = argv

    #Unit test
    print("Search for solution\n")
    start = Node([2,0,1,4,5,3,8,7,6])
    goal = Node([1,2,3,4,5,6,7,8,0])

    #print start.hamming_distance()
    #print start.manhattan_distance()

    search = Searcher(start, goal)

    start_time = time()
    if strategy == "dfs":
        search.dfs()
    elif strategy == "bfs":
        search.bfs()
    elif strategy == "hc":
        search.hill_climbing()
    elif strategy == "sahc":
        search.steepest_ascent_hill_climbing()
    elif strategy == "astar":
        search.astar()
    else:
        print "Wrong strategy"
    end_time = time()
    elapsed = end_time - start_time
    print "Search time: %s" % elapsed
    print "Number of initialized node: %d" % Node.n
