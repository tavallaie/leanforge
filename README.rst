===============================
Lean Forge Project
===============================

This project implements a Lean Canvas Model using Django and HTMX for smooth UI interactions without full page reloads.

What is Lean Canvas?
--------------------

Lean Canvas is a 1-page business plan template invented by Ash Maurya that helps you deconstruct your idea into its key assumptions. It replaces elaborate business plans with a single page business model.

Getting Started
----------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
-------------

You will need Python 3.7+ installed on your local machine. To check if you have Python 3 installed, you can run:

.. code-block:: bash

   $ python3 --version

You also need to have Poetry installed on your system. To install Poetry, you can run:

.. code-block:: bash

   $ curl -sSL https://install.python-poetry.org | python3 -

Installing
----------

1. Clone the repository:

   .. code-block:: bash

      $ git clone https://github.com/tavallaie/leanforge.git

2. Change into the `leanforge` directory:

   .. code-block:: bash

      $ cd leanforge

3. Install the required packages:

   .. code-block:: bash

      $ poetry install

4. Run the migrations:

   .. code-block:: bash

      $ poetry run python manage.py migrate

5. Start the server:

   .. code-block:: bash

      $ poetry run python manage.py runserver

Using the Application
---------------------

You should now be able to open a web browser and visit the application at http://localhost:8000.

Contributing
------------

.. Please read CONTRIBUTING.rst for details on our code of conduct, and the process for submitting pull requests.

License
-------

This project is licensed under the MIT License - see the LICENSE.rst file for details.
