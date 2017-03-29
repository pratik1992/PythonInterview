#!/usr/bin/env python


def apply_operation(left_operand, right_operand, operator):
    if left_operand and right_operand and operator is not None:
        return {
            '+': left_operand + right_operand,
            '-': left_operand - right_operand,
            '*': left_operand * right_operand,
            '/': left_operand / right_operand
        }[operator]




