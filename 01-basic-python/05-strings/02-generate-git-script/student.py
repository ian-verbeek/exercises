<<<<<<< HEAD
from textwrap import dedent

def generate_git_script(id):
    string = f'''
    if [ ! -d {id} ]; then
        git clone https://github.com/{id}/project {id}
    else
        (cd {id}; git pull)
    fi
    '''
    return dedent(string).strip()
    
=======
# gemaakt op pc
>>>>>>> 6b67f39ea963ddbbb6bfabf70e9c3fbc0dd42244
