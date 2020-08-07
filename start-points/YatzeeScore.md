Yatzee Score
============

This excercise is about fixing a bug and adding a feature to already existing code.

You will refactor and modify a command line program that computes the different possible scores of a given Yatzee dice roll. Here is an example execution for the Python version of the utility:

```
$ python yatzee.py 1 1 1 1 1
1s: 5
2s: 0
3s: 0
4s: 0
5s: 0
6s: 0
---
3 of a kind: 3
4 of a kind: 4
Full House: 5
Small Straight: 0
Large Straight: 0
Chance: 5
```

Notice two things with this report:

  1. It does not contain a line for "YATZEE" score even though the user got it (5 of a kind is YATZEE, and it is always scored 50)
  2. The Full House score is incorrect; 5 dices of the same value is not a full house in Yatzee, so the score should be 0

(1) is a feature that is not implemented yet.
(2) is a bug.

In this excercise, use approval testing to confidently fix (1) and (2).
