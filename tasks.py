from invoke import task


@task
def wsl(c):
    """install config file link for windows/wsl environment"""
    win_user_dir = c.run('wslpath "$(wslvar USERPROFILE)"').stdout.rstrip()
    working_dir = c.run("pwd").stdout.rstrip()
    c.run(f"rm -f {win_user_dir}/AppData/Roaming/qutebrowser/config/config.py")
    c.run("cp blank.html /mnt/c/opt/qutebrowser")
    c.run(
        f"cp {working_dir}/config-win.py "
        f"{win_user_dir}/AppData/Roaming/qutebrowser/config/config.py"
    )


@task
def ubuntu(c):
    """install config file link for ubuntu environment"""
    working_dir = c.run("pwd").stdout.rstrip()
    c.run(f"ln -s {working_dir}/config-ubuntu.py " f"~/.config/qutebrowser/config.py")
