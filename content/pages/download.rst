Download
========

You can download the **latest release** `here
<https://github.com/vmo-score/vmo-score/releases>`__ or clone the
repository:

.. code-block:: fish

    git clone --recursive https://github.com/vmo-score/vmo-score.git


External Applications
---------------------

* PyOracle_: Max interface for the Audio Oracle.
* i-score_: A free and open-source inter-media sequencer. A fork with the automatic generation tool can be found `here <https://github.com/vmo-score/i-score/releases/latest>`__.


Manual Installation
-------------------

Dependencies
~~~~~~~~~~~~

* libsamplerate_: Sample Rate Converter for audio (*required by librosa*).

  .. code-block:: fish
    :linenos: inline

    curl -L http://www.mega-nerd.com/SRC/libsamplerate-0.1.8.tar.gz | tar xz
    cd libsamplerate-0.1.8
    ./configure
    make
    make install

* Graphviz_: Open source graph visualization software (*required by snakes*).

  .. code-block:: fish

      brew install graphviz

Build
~~~~~

.. code-block:: fish
  :linenos: inline

  cd vmo-score/
  python setup.py install
  vmo_generator

Usage
-----

1. Open :code:`vmo_generator`.

.. image:: {filename}/images/vmo-score-open.png
   :alt: summary
   :width: 70 %
   :align: center

2. Select the audio recording.

.. image:: {filename}/images/open-audio.png
   :alt: summary
   :width: 70 %
   :align: center

3. Generate the segmentation.

.. image:: {filename}/images/segmentation-gui.png
   :alt: summary
   :width: 70 %
   :align: center

4. Generate the Petri Net.

.. image:: {filename}/images/petri-net-gui.png
   :alt: summary
   :width: 70 %
   :align: center

5. Open the :code:`json` file with :code:`i-score`.

.. image:: {filename}/images/iscore-open.png
   :alt: summary
   :width: 70 %
   :align: center

|

.. image:: {filename}/images/iscore-json.png
   :alt: summary
   :width: 70 %
   :align: center

.. _Graphviz: http://www.graphviz.org/
.. _libsamplerate: http://www.mega-nerd.com/SRC/
.. _Qt5: http://doc.qt.io/qt-5/
.. _brew: http://brew.sh/
.. _PyQt5: http://pyqt.sourceforge.net/Docs/PyQt5/installation.html
.. _VMO: https://github.com/wangsix/vmo
.. _SNAKES: https://www.ibisc.univ-evry.fr/~fpommereau/SNAKES/
.. _PyOracle: https://github.com/vmo-score/PyOracle_I-score
.. _i-score: http://i-score.org/
