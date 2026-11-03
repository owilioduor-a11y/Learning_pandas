# Learning Pandas

A hands-on learning repository for data analysis and manipulation using the **pandas** library in Python. This project contains notebooks, scripts, and datasets to help you go from beginner to advanced pandas techniques.

## 📑 Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 📖 About

This repository is dedicated to learning and practicing **pandas**, the powerful open-source data analysis and manipulation library for Python. Whether you are just getting started with data science or looking to sharpen your data-wrangling skills, you'll find practical examples, notebooks, and reference scripts here.

## ✨ Features

- 🐼 Core pandas fundamentals (Series, DataFrames, indexing)
- 🧹 Data cleaning and preprocessing techniques
- 📊 Data aggregation, grouping, and pivoting
- 🔗 Merging, joining, and concatenating datasets
- 📈 Time series analysis with pandas
- 📂 Working with CSV, Excel, JSON, and SQL data sources
- 📓 Jupyter notebooks for interactive exploration

## 📁 Project Structure

```text
Learning_pandas/
├── .github/
│   └── workflows/
│       └── python.yml              # CI workflow
├── data/                           # Sample datasets 
│   ├── raw/
│   └── processed/
├── notebooks/                      # Jupyter notebooks
│   ├── 01-introduction.ipynb
│   └── 02-data-cleaning.ipynb
├── src/                            # Source code
│   └── learning_pandas/
│       ├── __init__.py
│       └── utils.py
├── tests/                          # Unit tests
│   └── test_utils.py
├── .gitignore                      # Git ignore rules
├── .gitattributes                  # Git attributes
├── LICENSE                         # Project license
├── README.md                       # This file
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup file
└── pyproject.toml                  # Modern Python project config
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/) or [conda](https://docs.conda.io/)

### Clone the Repository

```bash
git clone https://github.com/owilioduor-a11y/Learning_pandas.git
cd Learning_pandas
```

### Set Up a Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Optional: Install in Development Mode

```bash
pip install -e .
```

## 💻 Usage

### Running a Notebook

```bash
jupyter notebook notebooks/01-introduction.ipynb
```

### Running a Python Script

```bash
python src/learning_pandas/utils.py
```

### Running Tests

```bash
pytest
```

## 📝 Examples

Here is a quick taste of what you can do with pandas:

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'London', 'Tokyo']
})

# Display basic info
print(df.head())
print(df.describe())

# Filter and group
adults = df[df['age'] >= 30]
print(adults)
```

See the `notebooks/` folder for more detailed, step-by-step examples.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Commit your changes**: `git commit -m 'Add some feature'`
4. **Push to the branch**: `git push origin feature/your-feature-name`
5. **Open a Pull Request**

Please make sure to follow the existing code style and include tests for new features.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

- **Author:** Peter Owili
- **GitHub:** [@owilioduor-a11y](https://github.com/owilioduor-a11y)
- **Email:** owilioduor@gmail.com

---

⭐ If you find this project helpful, please consider giving it a star!