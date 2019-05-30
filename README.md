# AITA

Online learning platform with face features detection and concentration grading.

## TODO

- [ ] improve post request while uploading courses
- [ ] refactoring the code to make it more readable (make it RESTful?)
- [ ] refactoring front-end code with Vuex
- [x] finish testing

## RUN OR DEVELOP

The `test` branch isn't a fully functional branch, it's for SoftwareTesting project. To run or develop, see [master branch](https://github.com/ludanxer/AITA/).

## TESTING

### WHAT AND HOW

  1. Black Box Testing [1]: `aita/auth.py`, methods: Boundary Value Analysis
  2. Black Box Testing [2]: `aita/api/focus.py`, methods: Equivalence Class Partitioning
  3. White Box Testing: `aita/api/usr.py`

### RESULT

#### pytest output

![pytest-m](https://github.com/ludanxer/AITA/raw/test/images/pytest-v.png)

#### coverage report of tested modules

![coverage-p](https://github.com/ludanxer/AITA/raw/test/images/coverage.png)

#### coverage report full content

![coverage-a](https://github.com/ludanxer/AITA/raw/test/images/coverage-a.png)

