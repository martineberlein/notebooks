# Jupyter Notebooks for Avicenna

## Getting started

- Download >= [Python 3.10](https://www.python.org/downloads/)
   
  Some variation of
  ```shell
  $ sudo apt-get install python3.12
  ```

- Make a virtual environment (recommended)
- 
  ```shell
  $ python3 -m venv avicenna_venv
  $ . avicenna_venv/bin/activate
  ```
- Install [Jupyter](https://jupyter.org/).
  ```shell
  $ python3 -m pip install jupyter
  ```

- Install the repositories:
  ```shell
  $ python3 -m pip install git+https://github.com/martineberlein/avicenna.git
  $ python3 -m pip install git+https://github.com/martineberlein/evogfuzzplusplus.git
  ```

- Start the Jupyter server in the repository directory
  ```shell
  $ jupyter lab .
  ```
This opens a browser window at http://localhost:8888/tree

