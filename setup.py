import setuptools

with open('./requirements.txt') as h:
    deps = list(filter(lambda s: len(s) and s[0] != '#',
                map(lambda s: s.strip(),
                    h)))
    # assert all(map(lambda s: s.startswith('http'), deps))

setuptools.setup(
    name='lojban_xbar',
    version="0.1.0",
    author="Oleg Parashchenko",
    author_email="olpa@uucode.com",
    description="Lojban mapping to X-Bar trees",
    url="https://github.com/olpa/lojban-xbar",
    classifiers=[
        "Topic :: Text Processing :: Linguistic",
    ],
    package_dir={'lojban_xbar': './src/lojban_xbar'},
    packages=['lojban_xbar'],
    scripts=['scripts/camxes_to_xbar.py', 'scripts/xbar_to_dot.py'],
    python_requires=">=3.6",
    install_requires=deps,
)
