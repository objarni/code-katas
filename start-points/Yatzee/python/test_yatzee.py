#!/usr/bin/env python3
from approvaltests.approvals import verify


from yatzee import YatzeeScore


def dice_scores(*dice):
    return YatzeeScore(dice)


def printer(scoring):
    return scoring.score_report()


def test_all_ones_scores():
    scoring = dice_scores(1, 1, 1, 1, 1)
    verify(printer(scoring))


