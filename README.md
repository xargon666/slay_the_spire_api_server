# Slay the Spire API

> WIP

## Contents
  * [Description](#description)
  * [Usage](#usage)
    + [Access Deployment](#access-deployment)
    + [Run Local Dev](#run-local-dev)
    + [Endpoints](#endpoints)
    + [Features](#features)
  * [Bugs](#bugs)
  * [Updates to Come](#updates-to-come)

---

## Description
A Python Flask API deployed to Heroku with a Postgres DB using an MVC pattern

## Usage
### Access Deployment
Currently deployed [here](https://slay-the-spire-api-server.herokuapp.com/) on heroku

### Run Local Dev
1. Clone repo
2. pipenv shell
3. pipenv install
4. pipenv run dev

### Endpoints
- /
  -home
- /relics
  - entire database
- /relics/ **int**
  -a single entry
### Features
- Route redirect to index.html
- CRUD
- Favicon
- Absolutely zero tests or frontend

## Bugs
- Radio buttons returns "on" instead of the value
- Form needs 'required' for name
## Updates to Come
- Add tables for more game data *e.g. cards*
- UI needs a button to create a table for all relics
- UI needs button for get relic by id / search for relic
- Base.html needs a header
- Add UI to request data
- Add User Login
- Add Deck Builder for Users
- Show stats for deck *e.g. draw probability*
