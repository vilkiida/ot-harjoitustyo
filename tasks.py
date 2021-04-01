from invoke import task

@task
def start(ctx):
	ctx.rum("python3 src/index.py")
