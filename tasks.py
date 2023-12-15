"""tasks.py"""
# pylint: disable-all

import sys
from invoke.tasks import task

@task
def run(ctx):
    if sys.platform.startswith("win"):
        ctx.run("python suber/main.py")
    else:
        ctx.run("python3 suber/main.py")

@task
def unittest(ctx):
    ctx.run("pytest ./tests/unit")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest ./tests/unit")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html -d ./docs/coverage")

@task
def lint(ctx):
    ctx.run("pylint suber", warn = True)

@task
def typecheck(ctx):
    ctx.run("mypy suber --html-report ./docs/mypy")

@task
def report(ctx):
    ctx.run("pylint suber", warn = True)
    ctx.run("mypy suber --html-report ./docs/mypy")
    ctx.run("coverage run --branch -m pytest ./tests/unit")
    ctx.run("coverage html -d ./docs/coverage")