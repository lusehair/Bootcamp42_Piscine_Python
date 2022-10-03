import setuptools 


# https://stackoverflow.com/questions/36014334/how-to-install-python-packages-from-the-tar-gz-file-without-using-pip-install
# https://docs.python.org/3/distutils/setupscript.html

setuptools.setup(
    name="my_minipack",
    version="0.0.1",
    author="lusehair", 
    description="logger and progressbar package for python pool 02 ex04", 
    packages=["my_minipack"],
    author_email="lusehair@student.fr",
    url="https://profile.intra.42.fr/users/lusehair",
    license="MIT",
    installer="pip",
     classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Students',
          'Topic :: Education',
          'Topic :: HowTo',
          'Topic :: Package',
          'License :: : OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3 :: Only',
          ],

    




)