# AITA

Online learning platform with face features detection and concentration grading.

## TODO

- [ ] improve post request while uploading courses
- [ ] refactoring the code to make it more readable (make it RESTful?)
- [ ] refactoring front-end code with Vuex
- [x] finish testing

## RUN

  1. Run MongoDB on your computer on default port
  2. cd /path/to/AITA
  3. pip3 install -r requirements.txt
  4. python3 run.py

## DEVELOPE

  1. You will find the flask project in `aita` folder
  2. You will find the vue-cli project in `client` folder
  3. When you run `npm run build`, the static files will be generated into `aita/static` and `aita/templates` due to `client/vue.config.js`
  4. While developing, if you use `npm run serve` as your client, the browser can't find staic files like `*.mp4` properly (`*.css` and `*.js` work fine). You need to build vue project, and `python3 run.py`

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

