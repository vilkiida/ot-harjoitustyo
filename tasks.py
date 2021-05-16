from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/minesweeper.py")

@task
def initialize(ctx):
	ctx.run("python3 src/initialize_database.py")
@task
def test(ctx):
	ctx.run("pytest src")

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html")

@task
def lint(ctx):
	ctx.run("pylint src")
