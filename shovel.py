from shovel import task

import re
import datetime


def touch(base, title):
    '''Touch an empty post in the provided base'''
    now = datetime.datetime.now()
    sanitized = re.sub(r'\W+', '-', title).strip('-').lower()
    path = '%s/%s-%s.md' % (base, now.strftime('%Y-%m-%d'), sanitized)
    with open(path, 'w+') as fout:
        fout.write('\n'.join([
            '---',
            'layout: post',
            'title:  "%s"' % title,
            'date:   %s' % now.strftime('%Y-%m-%d %H:%M:%S'),
            'categories:',
            '---'
        ]))
    return path


@task
def post(title):
    '''Create a new post with the provided title'''
    print touch('_posts/', title)


@task
def draft(title):
    '''Create a new draft with the provided title'''
    print touch('_drafts', title)
