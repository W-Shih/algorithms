<!--===============================================================================================
                                 All Rights Reserved.
===================================================================================================
File description:
        README.md to introduce and explain this project

===================================================================================================
   Date      Name                    Description of Change
14-Nov-2021  Wayne Shih              Initial create and add badges
14-Nov-2021  Wayne Shih              Add codacy badges
01-Sep-2022  Wayne Shih              Add doc on how to run on local machine
$HISTORY$
================================================================================================-->

# algorithms

[![Build Status](https://app.travis-ci.com/W-Shih/algorithms.svg?branch=main)](https://app.travis-ci.com/W-Shih/algorithms)
[![codecov](https://codecov.io/gh/W-Shih/algorithms/branch/main/graph/badge.svg?token=bybEpCVcGG)](https://codecov.io/gh/W-Shih/algorithms)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9b31e49fa7344bcf93e6bc688da93fe2)](https://www.codacy.com/gh/W-Shih/algorithms/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=W-Shih/algorithms&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/9b31e49fa7344bcf93e6bc688da93fe2)](https://www.codacy.com/gh/W-Shih/algorithms/dashboard?utm_source=github.com&utm_medium=referral&utm_content=W-Shih/algorithms&utm_campaign=Badge_Coverage)
[![pylint Score](https://mperlet.github.io/pybadge/badges/10.svg)](https://app.travis-ci.com/W-Shih/algorithms) <!-- https://mperlet.github.io/pybadge/ -->

## Contents

- [algorithms](#algorithms)
  - [Contents](#contents)
  - [Run on Your Machine](#run-on-your-machine)
    - [Pre-install](#pre-install)
    - [Prepare Environment](#prepare-environment)
    - [Ready to Go](#ready-to-go)

## Run on Your Machine

### Pre-install

- [Oracle VM VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)

### Prepare Environment

- Clone this Repo

  ```bash
  host$ git clone git@github.com:W-Shih/algorithms.git
  ```

- Prepare `Vagrantfile`
  
  The simplest way is to use `Vagrantfile-bak` as the template.

  ```bash
  host$ cp Vagrantfile-bak Vagrantfile
  ```

- Initial VM

  ```bash
  host$ vagrant up
  ```

- VM settings (optional)
  - Virtual Box
    - Use 4 CPUs at least
    - Use 2048 MBs for memory at least
  - Modify `.bashrc`
  
    ```bash
    host$ vagrant ssh
    vm$ sudo vi ~/.bashrc
    ```

    - add `cd /vagrant` on the top
    - `force_color_prompt=yes`

### Ready to Go

Now you are all set. You should be able to run this service on your machine.

- Run tests
  
  ```bash
  vm$ coverage run -m unittest discover && coverage report -m && coverage html && coverage xml
  ```

- Run pylint

  ```bash
  vm$ touch __init__.py; pylint $(pwd); rm __init__.py
  ```
