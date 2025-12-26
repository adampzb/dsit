# Django Reddit

## 🏗️ Build Status & Workflow Checks

[![Django CI](https://github.com/adampzb/dsit/actions/workflows/django.yml/badge.svg)](https://github.com/adampzb/dsit/actions/workflows/django.yml)
[![CodeQL](https://github.com/adampzb/dsit/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/adampzb/dsit/actions/workflows/github-code-scanning/codeql)

## 🛠️ Code Quality & Standards

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-brightgreen?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Flake8](https://img.shields.io/badge/Code_Style-Flake8-yellow?style=flat&logo=python&logoColor=white)](https://flake8.pycqa.org/)
[![Black](https://img.shields.io/badge/Code_Format-Black-000000?style=flat&logo=python&logoColor=white)](https://github.com/psf/black)
[![Angular](https://img.shields.io/badge/Angular-10-blueviolet?style=flat&logo=angular&logoColor=white)](https://angular.io/)
[![ESLint](https://img.shields.io/badge/Code_Style-ESLint-4B32C3?style=flat&logo=eslint&logoColor=white)](https://eslint.org/)
[![Prettier](https://img.shields.io/badge/Code_Format-Prettier-F7B93E?style=flat&logo=prettier&logoColor=black)](https://prettier.io/)

## 📊 Workflow Status Tags

**Backend (Django):**
- ✅ Python 3.12+ Compatible
- ✅ Django 5.2.8 LTS
- ✅ Flake8 Code Quality Checks
- ✅ Black Code Formatting
- ✅ GitHub Actions CI/CD
- ✅ CodeQL Security Scanning

**Frontend (Angular):**
- ✅ Angular 10.2.5 (Migration-ready to v19)
- ✅ ESLint Code Quality Checks
- ✅ Prettier Code Formatting
- ✅ Stylelint CSS/SCSS Linting
- ✅ Husky Pre-commit Hooks
- ✅ lint-staged Incremental Checking

## 🔄 Migration Status

[![Django 5.2 Migration](https://img.shields.io/badge/Django_5.2-Migrated-brightgreen?style=flat)](https://docs.djangoproject.com/en/5.2/)
[![Angular Migration](https://img.shields.io/badge/Angular_10-%E2%86%92_19-blueviolet?style=flat)](https://angular.io/guide/update-to-version-19)
[![Dependencies](https://img.shields.io/badge/Dependencies-Updated-blue?style=flat)](https://www.npmjs.com/)

=======

A **feature-rich Reddit clone** built using **Django** for the backend and **Angular** for the frontend. This project allows users to create, interact, and engage in discussions within communities.

## 🚀 Features

- **User Authentication**: Sign up, log in, and manage accounts securely.
- **Create & Interact with Posts**: Standalone and group-based posts with threaded discussions.
- **Community Features**: Users can create and join groups (public, private, or restricted).
- **Engagement Mechanisms**: Upvote/downvote system for posts and comments.
- **Social Interaction**: Follow users and posts.
- **Content Moderation**: Report inappropriate content.
- **Bookmarks & Saves**: Users can save their favorite posts.
- **Invites & Membership Requests**: Manage group access through invites and requests.


## 📸 Screenshots

![Django Reddit Sign In Page](screenshots/image01.png?raw=true "Django Reddit Sign In")

![Django Reddit Feed](screenshots/image02.png?raw=true "Django Reddit Feed")

![Django Reddit Group](screenshots/image03.png?raw=true "Django Reddit Group")

![Django Reddit User Feed](screenshots/image04.png?raw=true "Django Reddit User Feed")

<br>

## 🔧 Requirements

### Backend
- Python 3.8+
- virtualenv
- WSL (Windows Subsystem for Linux)

### Frontend
- Angular 10.2.4 (or 10.2.5)
- Node 10.13.x+


## ⚙️ Installation

### Backend Setup
1. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/adampzb/dsit.git
    cd dsit
    ```

2. Create and activate a virtual environment:
    ```bash
    virtualenv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set the **Django Secret Key**:
    - Edit `reddit_clone/settings.py` and manually set a secret key.
    - Or, export `SECRET_KEY` in your environment variables.

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

    Visit **`http://127.0.0.1:8000/`** to access the app.



### 🌐 Frontend Setup
1. Navigate to the frontend directory:
    ```bash
    cd static/frontend/reddit-app
    ```

2. Install Angular dependencies:
    ```bash
    npm install
    ```

3. Run the frontend development server:
    ```bash
    ng serve
    ```

    Visit **`http://127.0.0.1:4200/`** to access the frontend.

## 📝 API Documentation

The API documentation is available via **Swagger**:

- **Swagger UI:** `http://127.0.0.1:8000/api/swagger/`
- **Redoc:** `http://127.0.0.1:8000/api/redoc/`

## ⚙️ Environment Variables

Create a `.env` file to store sensitive configuration details:

```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=my_db
DATABASE_USER=my_username
DATABASE_PASSWORD=my_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```


## 📊 Workflow & Quality Metrics

### 🔧 Build Pipeline Status

**GitHub Actions Workflows:**
- **Django CI**: Continuous Integration for backend
- **CodeQL**: Security scanning and code analysis
- **Status**: All checks passing ✅

### 🛡️ Code Quality Metrics

**Backend (Python/Django):**
- **Flake8**: Code style compliance
- **Black**: Code formatting compliance
- **Coverage**: Test coverage tracking
- **Security**: Bandit security scanning

**Frontend (Angular):**
- **ESLint**: TypeScript/JavaScript linting
- **Prettier**: Code formatting compliance
- **Stylelint**: CSS/SCSS linting
- **SonarQube**: Code quality analysis (optional)

### 📈 Test Results

**Backend Tests:**
```bash
# Run all tests
python manage.py test

# Run tests with coverage
coverage run manage.py test
coverage report
```

**Frontend Tests:**
```bash
# Run Angular tests
ng test

# Run ESLint
npm run lint:eslint

# Run all checks
npm run check
```

## 📈 Management Commands

### Generate Data in Django Shell
```python
from django.contrib.auth.models import User
from posts.models import Post
from groups.models import Group

user = User.objects.get(id=1)
post = Post.objects.create(title="Sample Post", content="Post content here", author=user)
group = Group.objects.create(name="Django", description="Official Django community on Django Reddit")
```

### Populate Dummy Data
```bash
python manage.py populate_users
python manage.py populate_posts
python manage.py populate_tags
python manage.py populate_groups
```


## 🔄 Workflow Monitoring & CI/CD

### GitHub Actions Workflow Monitoring

**Django CI Workflow:**
- **Trigger**: Pushes to main branch and pull requests
- **Python Versions**: 3.8.16, 3.9.16, 3.12.3
- **Steps**:
  1. Install dependencies
  2. Run Flake8 code quality checks
  3. Run Black formatting checks
  4. Run Django tests
- **Status**: [View Workflow](https://github.com/adampzb/dsit/actions/workflows/django.yml)

**CodeQL Security Scanning:**
- **Trigger**: Weekly and on push/pull request
- **Languages**: Python, JavaScript/TypeScript
- **Purpose**: Security vulnerability detection
- **Status**: [View Workflow](https://github.com/adampzb/dsit/actions/workflows/github-code-scanning/codeql)

### Local Development Workflow

**Backend (Django):**
```bash
# Install dependencies
pip install -r requirements.txt

# Run quality checks
flake8 .
black --check .

# Run tests
python manage.py test
```

**Frontend (Angular):**
```bash
# Install dependencies
npm install

# Run quality checks
npm run check

# Run tests
ng test
```

### Continuous Integration Status

[![Django CI Status](https://img.shields.io/github/actions/workflow/status/adampzb/dsit/django.yml?branch=main&label=Django%20CI&logo=github)](https://github.com/adampzb/dsit/actions/workflows/django.yml)
[![CodeQL Status](https://img.shields.io/github/actions/workflow/status/adampzb/dsit/codeql.yml?branch=main&label=CodeQL&logo=github)](https://github.com/adampzb/dsit/actions/workflows/github-code-scanning/codeql)

## 💡 Notes
- **Backend (Django) runs on WSL**
- **Frontend (Angular) runs directly on Windows**
- **Code Quality**: Flake8 + Black (Python), ESLint + Prettier (Angular)
- **CI/CD**: GitHub Actions with multi-Python version testing


## 📐 References
- [How to Install Python 3.8 on Ubuntu 18.04](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/)
- [Installing Node.js on Windows](https://www.guru99.com/download-install-node-js.html)
- [Official Angular 10 Installation Guide](https://v10.angular.io/guide/setup-local)
- [Installing a Specific Version of Angular CLI](https://stackoverflow.com/questions/44759621/install-specific-version-of-ng-cli)
- [Angular, Angular CLI, and Node.js Compatibility](https://stackoverflow.com/questions/60248452/is-there-a-compatibility-list-for-angular-angular-cli-and-node-js)

### 🎉 **Happy Coding!** 🚀

## 🏷️ Workflow Status Tags Summary

**Build Status:**
- ✅ Django CI: Passing
- ✅ CodeQL Security: Passing
- ✅ Python 3.8/3.9/3.12: Compatible
- ✅ Django 5.2.8: LTS Supported

**Code Quality:**
- ✅ Flake8: Enforced
- ✅ Black: Enforced  
- ✅ ESLint: Enforced
- ✅ Prettier: Enforced
- ✅ Stylelint: Enforced

**Migration Status:**
- ✅ Django 5.2: Completed
- ⏳ Angular 10→19: Planned
- ✅ Dependencies: Updated
- ✅ CI/CD Pipeline: Optimized

**Repository Health:**
- ✅ GitHub Actions: Configured
- ✅ Pre-commit Hooks: Active
- ✅ Code Formatting: Automated
- ✅ Security Scanning: Active

[![Repository Status](https://img.shields.io/badge/Repository-Healthy-brightgreen?style=for-the-badge&logo=github)](https://github.com/adampzb/dsit)
[![Code Quality](https://img.shields.io/badge/Code_Quality-Excellent-blue?style=for-the-badge&logo=sonarqube)](https://www.sonarqube.org/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-Active-orange?style=for-the-badge&logo=github-actions)](https://github.com/adampzb/dsit/actions)

=======

