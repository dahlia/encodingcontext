from __future__ import with_statement

from distutils.core import setup
import re


def readme():
    try:
        with open('README.rst') as f:
            readme = f.read()
    except IOError:
        return
    return re.sub(
        r'''
        (?P<colon> : \n{2,})?
        \.\. [ ] code-block:: \s+ [^\n]+ \n
        [^ \t]* \n
        (?P<block>
            (?: (?: (?: \t | [ ]{3}) [^\n]* | [ \t]* ) \n)+
        )
        ''',
        lambda m: (':' + m.group('colon') if m.group('colon') else '') +
                  '\n'.join(' ' + l for l in m.group('block').splitlines()) +
                  '\n\n',
        readme, 0, re.VERBOSE
    )


setup(
    name='encodingcontext',
    version='0.9.0',
    description='A bad idea about the default encoding',
    long_description=readme(),
    py_modules=['encodingcontext'],
    author='Hong Minhee',
    author_email='minhee' '@' 'dahlia.kr',
    url='https://github.com/dahlia/encodingcontext',
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Text Processing'
    ]
)
