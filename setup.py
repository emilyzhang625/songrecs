from setuptools import setup, find_packages

setup(
    name='songrecs',
    packages=find_packages(include=['frontend', 'frontend.*']),
    install_requires=[
        'pandas>=2.2.2',
        'scikit-learn>=1.5.1',
        'numpy>=2.0.1',
        'streamlit>=1.37.0',
        'requests>=2.32.3',
        'python-dotenv>=1.0.1',
    ],
)
