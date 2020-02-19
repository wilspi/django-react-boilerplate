# django-react-boilerplate
![Python application](https://github.com/wilspi/django-react-boilerplate/workflows/Python%20application/badge.svg?branch=master)     
`django-react-boilerplate` is a [Django](https://www.djangoproject.com/) and React boilerplate.  

### Quick start
Follow steps to quickly start development:  
1. Replace `django-react-boilerplate` with your application name


### Development
* #### Setup

  * Install `nix`  
    Follow steps [here](https://gist.github.com/wilspi/aad81f832d030d80fca91dfa264a1f8a), if not done already
  * Run
    ```
    nix-shell --pure shell.nix
    ```

* #### Update requirements
    ```
    pip install -r requirements.txt # python
    cd editor/frontend/ && npm install && cd - # node packages
    ```

* #### Run
  * Build js 
    ```
    cd editor/frontend/ && npm run build && cd -
    ```
  * Collect static files
    ```
    python manage.py collectstatic
    ```
  * Run application
    ```
    python manage.py runserver
    ```
  
