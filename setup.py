from setuptools import setup, find_packages

setup(
    name="sentiment_analysis_app",
    version="1.0.0",
    description="A Flask-based Sentiment Analysis Web Application",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==2.3.2",
        "textblob==0.17.1"
    ],
    entry_points={
        "console_scripts": [
            "run-sentiment-app=app.server:app.run"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)