About
=====

:url:
:save_as: index.html

VMO-Score_ [@@Arias:2016] is a tool to generate an interactive score to control
the improvisation according to larger structures found in an audio recording.

Intuitively, VMO-Score_ takes an audio file as an input and uses the tool VMO_
[@@Wang:2015] to generate an Audio Oracle [@@Dubnov:2011] for improvisation. In
addition, VMO is also used to do a segmentation analysis of the input
[@@Wang2016]. Once the tool has identified possible *natural* transitions
between sections with similar musical content, it translates the music
structure into a Petri net [@@Murata:1989] model in order to provide a higher,
more intuitive and formal representation of this structure. Therefore, the
artist can modify the structure of the Petri net in order to control the
improvisation by adding temporal and logical constraints.

VMO-Score_ also generates an interactive score based on the Petri net structure
for the inter-media sequencer i-score_ [@@delaHogue:2016]. This tool provides
a complete graphical interface for structuring and performing in real-time the
improvisation. Such improvisation is carried out by the Max interface of the
Audio Oracle called PyOracle_ [@@Surges:2013] which is controlled by i-score_
using OSC [#]_ messages.



.. image:: {filename}/images/summary.png
   :alt: summary
   :width: 50 %
   :align: center

.. [#] *Open Sound Control* (OSC_) is a protocol for communication among multimedia devices.

.. _VMO-Score: {filename}/pages/about.rst
.. _VMO: https://github.com/wangsix/vmo
.. _i-score: http://i-score.org/
.. _PyOracle: https://gitlab.com/himito/PyOracle_I-score
.. _OSC: http://opensoundcontrol.org/
