---
layout: default
title: Final Report
---

## Video

## Project Summary

The concept of a jumping puzzle has been around for decades. Think of a regular maze, where you have a start point and must reach the end point through a series of up, down, left, right actions. Now add holes in this maze along with a jumping action to the action space and you have a jumping puzzle. 

<img src="http://s3.vidimg.popscreen.com/original/2/ZHZuS0tvOEIxLWsx_o_funny-minecraft-jump.jpg" height="260" width="380">

The ability for a character to jump is a key mechanism in many successful games. Jumping puzzles
takes this mechanism to a whole new level in which the player’s knowledge of where to jump and
when to jump can decide whether they pass the level or not. Games like Guild Wars and Assassin’s
creed implement this feature to some extent while games like Super Mario are a giant jumping puzzle in itself.
A jumping puzzle AI would allow game developers to test whether a jumping puzzle
is able to be completed/whether it is too easy or hard. The field of robotics is fairly new but that
doesn’t stop researchers from having visions of robots saving people from catastrophes or fighting
in wars in place of humans. Like Minecraft, the real world is not just flat lands. If a robot is
going to perform those functions, it will need to be able to, not only walk, but to learn to climb
and maybe even jump!

In our project, we give our agent, JPS, progressingly intricate jumping puzzles to solve. What separates a jumping puzzle from a regular maze is that it is only solveable by jumping. That is, JPS may choose to walk through the maze (if it leads to the optimal reward) but it can never reach the destination block if it does not utilize jumping.

<img src="http://i61.servimg.com/u/f61/15/81/88/32/jump_210.png" height="260" width="380">

Sounds simple enough right? Wrong. There are many complex attributes to a jumping puzzle. Jumping across a single-block hole is easy but what happens when the hole is 2-blocks large? Increasing the size of the maze is trivial (we deal with x and z coordinates) but how does the complexity scale when we add multiple layers to the maze (now we're dealing with x, z, AND y). How would the agent even know to jump to the floor above it? Stay tuned and JPS will help unearth the answers to some of these questions!

<img src="https://s-media-cache-ak0.pinimg.com/736x/75/b9/49/75b949bc25f4c19a3fbb19dc699b57b4.jpg" height="260" width="380">


## Approaches

## Evaluation

## References
