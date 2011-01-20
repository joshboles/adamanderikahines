from fabric.api import *

env.disable_known_hosts = False # always fails for me without this
env.hosts = ['django1']
env.root = '/home/serveruser/'
env.proj_slug = 'myproject'
env.db_type = "postgresql"
env.ve_root = env.root + '.virtualenvs/' + env.proj_slug
env.proj_root = env.root + 'development-sites/' + env.proj_slug
env.pip_file_deploy = env.proj_root + '/requirements/deploy.txt'
env.pip_file_dev = env.proj_root + '/requirements/dev.txt'
env.supervisor_name = env.proj_slug

def update():
    """
    Update source, update pip requirements, syncdb, restart server
    """
    update_proj()
    update_reqs()
    build_static()
    migrate()
    syncdb()
    restart()

def update_local():
    local("git pull")
    update_reqs()
    migrate()
    syncdb()
    runserver()

def reset_local():
    local("git pull origin master")
    reset_db()
    hard_update_reqs()
    migrate()
    syncdb()
    runserver()

def start_local():
    local("mkvirtualenv %s" % env.proj_slug)
    reset_local()

def push():
    """
    Update source and restart

    This is similar to `update` but it does not update all the requirements
    and does not execute migrations. Perfect for minor changes.
    """
    local('git push') # TODO: use an explicit branch here?
    update()

def version():
    """
    Show last commit to repo on server
    """
    sshagent_run('cd %s; git log -1' % env.proj_root)

def restart():
    """Restart Apache process"""
    run('supervisorctl %s restart' % env.proj_slug)

def reset_db():
    """
    Empties the DB
    """
    if env.db_type is "postgresql":
        ve_run('dropdb %s; createdb %s;' % (env.proj_slug, env.proj_slug))
    else:
        ve_run("python manage.py sqlflush | python manage.py dbshell")

def update_reqs():
    """
    Update pip requirements
    """
    ve_run('yes w | pip install -E %s -r %s' % (env.root, env.pip_file))

def hard_update_reqs():
    ve_run('yes w | pip install -E %s -U -r %s' % (env.root, env.pip_file))

def update_proj():
    """
    Updates project source
    """
    sshagent_run('cd %s; git pull' % env.proj_root)

def syncdb():
    """
    Run syncdb
    """
    output = ve_run('python manage.py syncdb')
    if 'Not synced (use migrations):' in output:
         migrate()

def build_static():
    ve_run('python manage.py build_static --noinput')

def migrate():
    """Execute south migrations"""
    ve_run('python manage.py migrate')

def ve_run(cmd):
    """
    Helper function.
    Runs a command using the virtualenv environment
    """
    # require('root')
    # I do not require root for any of these functions
    return run('source %s/bin/activate; %s' % (env.ve_root, cmd))

def sshagent_run(cmd):
    """
    Helper function.
    Runs a command with SSH agent forwarding enabled.
    
    Note:: Fabric (and paramiko) can't forward your SSH agent. 
    This helper uses your system's ssh to do so.
    """

    for h in env.hosts:
        try:
            host, port = h.split(':')
            local('ssh -p %s -A %s "%s"' % (port, host, cmd))
        except ValueError:
            local('ssh -A %s "%s"' % (h, cmd))