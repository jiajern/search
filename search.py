# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
#    print problem.getSuccessors(problem.getStartState())
    begin = problem.getStartState()
    mystack = util.Stack()
    visited = []
    mystack.push((begin, []))
#    parent[problem.getStartState()] = None
#    move[problem.getStartState()] = None
    while not mystack.isEmpty():
        state = mystack.pop()
        #print state
        if state not in visited:
            visited.append(state[0])
            if problem.isGoalState(state[0]):
                return state[1]
            else:
                for suc in problem.getSuccessors(state[0]):
                    if suc[0] not in visited:
                        mystack.push((suc[0], state[1]+[suc[1]]))
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    my_q = util.Queue()
    begin = problem.getStartState()
    my_q.push((begin,[],0))
    visited = []
    #i = 0
    while not my_q.isEmpty():
        state = my_q.pop()
        #print state
        #if i == 100:
        #    break
        #i += 1
        if state[0] in visited:
            continue
        visited.append(state[0])
        #mysolution.append(state[1])
        if problem.isGoalState(state[0]):
        #    print state[0]
            return state[1]
        else:
            for s in problem.getSuccessors(state[0]):
                if s[0] not in visited:
                    my_q.push((s[0], state[1]+[s[1]], s[2]))
    return []
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # this is basically a dijkstra algorithm
    # which we expand the node with lowest cost
    # need a priority Q to keep the node
    PQ = util.PriorityQueue()
    # instead of keeping the parent we keep track of the route that we traveled
    PQ.push((problem.getStartState(), [], 0), 0)
    # also need a list to keep visited node
    visited = []
    while not PQ.isEmpty():
        node = PQ.pop()
        if node[0] not in visited:
            visited.append(node[0])
            if problem.isGoalState(node[0]):
                return node[1]
            else:  # have to expand the node
                for succ in problem.getSuccessors(node[0]):
                    if succ[0] not in visited:
                        PQ.push((succ[0], node[1]+[succ[1]], succ[2] + node[2]), succ[2] + node[2])
#    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # this is just dijkstra but with heuristic value
    PQ = util.PriorityQueue()
    PQ.push((problem.getStartState(), [], 0), 0)
    visited = []
    while not PQ.isEmpty():
        node = PQ.pop()
        #print()
        if node[0] not in visited:
            visited.append(node[0])
            if problem.isGoalState(node[0]):
                return node[1]
            else:
                for succ in problem.getSuccessors(node[0]):
                    if succ[0] not in visited:
                        h = heuristic(succ[0], problem)
                        PQ.push((succ[0], node[1]+[succ[1]], succ[2]+node[2]), succ[2]+node[2]+h)
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
