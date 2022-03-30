---
deeptendies
---

[![image](https://img.shields.io/pypi/v/deeptendies.svg)](https://pypi.python.org/pypi/deeptendies)
[![image](https://img.shields.io/travis/stancsz/deeptendies.svg)](https://travis-ci.com/stancsz/deeptendies)
[![Documentation Status](https://readthedocs.org/projects/deeptendies/badge/?version=latest)](https://deeptendies.readthedocs.io/en/latest/?version=latest)

Bringing quantitative trading to the masses!

# Features
The most difficult part of quantitative analysis is getting started. This project has you covered ;) It is a one-stop shop for obtaining historical data, engineering features, and fitting the data through a pipeline.

## Ease of installation
```
!pip install git+https://github.com/stancsz/deeptendies && pip install -r https://raw.githubusercontent.com/stancsz/deeptendies/main/requirements.txt
```

## Look and feel of pandas dataframe
indeed you're getting a pd.dataframe, instead of some proprietary file formats
```python
import deeptendies as dt
df = dt.DataFrame.from_yf('GME')
```

## Feature engineering
Easy to use feature engineering methods
```python
df = dt.Feature.get_x_low(df, x=52, interval='week')
df = get_x_ma(df, x=50, interval='day')
```

## Builtin Pipeline class
for mass processing features
```python
pipeline = dt.Pipeline(
    [
        dt.Feature.get_x_high,
        dt.Feature.get_x_low,
        dt.Feature.get_x_ma,
        dt.Feature.get_diff
    ]
)
df = pipeline.run(df=df, x=50, interval='day')
df = pipeline.run(df=df, x=100, interval='day')
df = pipeline.run(df=df, x=200, interval='day')
df = pipeline.run(df=df, x=50, interval='week')
df = pipeline.run(df=df, x=100, interval='week')
df = pipeline.run(df=df, x=200, interval='week')
```
![img.png](docs/img.png)
## Jupyter
[or use it in a notebook](https://github.com/deeptendies/deeptendies/blob/master/tests/jupyter/01_getting_stock_data_and_engineer_feature.ipynb)

# Development guide
```
git clone https://github.com/deeptendies/deeptendies.git
pip install -e deeptendies
```

# Credits
- This package is redesigned from the [legacy deeptendies package](https://github.com/deeptendies/legacy-deeptendies-library), credits to original authors.
  - @mklasby @bgulseren @KBehairy @hasnil @Karenzhang7717
- This package was created with Cookiecutter and the audreyr/cookiecutter-pypackage project template.

# License
- Free software: MIT license
- Documentation: <https://deeptendies.readthedocs.io>.
