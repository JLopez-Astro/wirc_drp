from setuptools import setup, find_packages


#We should flesh this out

setup(
	name='wirc_drp',
	version='0.1', 
	packages=find_packages(),
	license="TBD",
	install_requires=['photutils','opencv-python','scikit-image'],
	long_description=open('README.md').read()
	)


