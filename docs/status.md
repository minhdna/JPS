---
layout: default
title: Status
---

### Project Summary

The goal of JPS remains the same and it is to be able to continue solving <br />
progressingly intricate jumping puzzles. Our base line project, which we <br />
have already achieved, is to solve a small 2D maze (5x4) that is only solveable <br />
through jumping. That is, the AI may choose to walk through the maze <br />
(if it leads to the optimal reward) but it can never reach the destination <br />
block if it does not utilize jumping. Our next milestone is to be able to solve <br />
a small maze with 2 floors (5x4x2). From there on, we will continue to increase <br />
the size of the maze and add more floors. Our moonshot case is for our agent to <br />
be able to solve a large maze with 3 floors (10x10x3). 

### Approach

### Evaluation

### Remaining Goals and Challenges

Currently, our agent is very limited in that it is only able to solve a very small, <br />
single-dimension maze that we generated ourselves. We hope to expand our agent so that <br />
it is able to solve multi-floor mazes. The bare-minimum in which we consider our agent <br />
a success is if it is able to solve a maze of 2 floors. Once it is able to solve a 2-level <br />
maze, we are confident it can learn to solve 3 or 4-level maze. <br />

The biggest challenge is for our agent to observe that the maze has 2 floors and make smart <br />
decisions base off of that. We're currently using one Q-table to represent the reward states <br />
of a single-level maze. One solution we're thinking about is using multiple Q-tables to <br />
represent multiple floors. That is a difficult task in itself so our backup plan is to <br />
ignore the Y-value completely.
