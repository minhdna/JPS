---
layout: default
title: Proposal
---

## PROPOSAL FOR CS175 AI PROJECT
#### Met with professor on May 1, 2017


### Summary for Project

For our project, we chose our agent to solve a Jumping game. The Jumping game has a start and destination. The agent must get from the start to the destination. However, unlike regular mazes, mazes in the Jumping game have missing blocks that the agent fall through. The agent must avoid these gaps the sucessfully reach the destination block. Our input semantics will be the generated maze mission. The agent will not know of its envirnment and only has information about the current state. The output of each mission will be the path the agent found and a cost of the path the agent found from the optimal path. 
    
### AI/ML Algorithms

We plan on using Monte Claro policy evaluation to find the optimal path of a puzzle. We then hope to use reinforcement learning to train our agent on the optimal path to be able to sovle Jumping puzzles.
    
### Evaluation Plans

Based on the optimal path and the path given by our agent at the end of the mission, we calculate the cost of the generated path. The reinforcement learning will optimize the cost and converge to an optimal value. To verify that our algorithm works, we will measure the error at each iteration and see wether it decreases monotonically and wither it converges to a final value.

To verify if our agent is properly trained, we will run the agent of a maze it has never seen before and ask it to traverse it. We will consider the project a success if the cost generated is within a threshold from the optimal path. As a sanity case, we will use a simple maze. It will likely have a small number of blocks and few missing blocks. Our moonshot case is solving a large puzzle with sparse blocks that have large gaps inbetween blocks. It would not have to find the optimal path but only be able to solve the puzzle. 
