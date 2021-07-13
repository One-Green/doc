One-green project official documentation
----------------------------------------

.. image:: https://readthedocs.org/projects/one-green/badge/?version=latest
    :target: https://one-green.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Create dev environment
----------------------

.. code-block:: shell

    pipenv install


Live html
---------


.. code-block:: shell

    make livehtml


Build
-----

.. code-block:: shell

    make html


Build diagrams
--------------

.. code-block:: shell

    cd diagrams && \
    python helm_k8s_architecture.py
    python deploy_center.py
