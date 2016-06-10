.. java:import:: java.awt Dimension

.. java:import:: java.awt Point

.. java:import:: java.io Serializable

VNodeMemo
=========

.. java:package:: sem8.tirt
   :noindex:

.. java:type:: public class VNodeMemo implements Serializable

   Stores serializable data using by \ ``VNodeFrame``\ .

   :author: Jacek Skoczylas

Constructors
------------
VNodeMemo
^^^^^^^^^

.. java:constructor:: public VNodeMemo()
   :outertype: VNodeMemo

VNodeMemo
^^^^^^^^^

.. java:constructor:: public VNodeMemo(int vnodeNumber, AbstractVNodeConfigMemo configMemo)
   :outertype: VNodeMemo

Methods
-------
copy
^^^^

.. java:method:: public VNodeMemo copy()
   :outertype: VNodeMemo

getConfigMemo
^^^^^^^^^^^^^

.. java:method:: public AbstractVNodeConfigMemo getConfigMemo()
   :outertype: VNodeMemo

getInputsNum
^^^^^^^^^^^^

.. java:method:: public int getInputsNum()
   :outertype: VNodeMemo

getLocation_orNull
^^^^^^^^^^^^^^^^^^

.. java:method:: public Point getLocation_orNull()
   :outertype: VNodeMemo

getOutputsNum
^^^^^^^^^^^^^

.. java:method:: public int getOutputsNum()
   :outertype: VNodeMemo

getSize_orNull
^^^^^^^^^^^^^^

.. java:method:: public Dimension getSize_orNull()
   :outertype: VNodeMemo

getVnodeNumber
^^^^^^^^^^^^^^

.. java:method:: public int getVnodeNumber()
   :outertype: VNodeMemo

setConfigMemo
^^^^^^^^^^^^^

.. java:method:: public void setConfigMemo(AbstractVNodeConfigMemo configMemo)
   :outertype: VNodeMemo

setInputsNum
^^^^^^^^^^^^

.. java:method:: public void setInputsNum(int inputsNum)
   :outertype: VNodeMemo

setLocation
^^^^^^^^^^^

.. java:method::  void setLocation(Point location)
   :outertype: VNodeMemo

setOutputsNum
^^^^^^^^^^^^^

.. java:method:: public void setOutputsNum(int outputsNum)
   :outertype: VNodeMemo

setSize
^^^^^^^

.. java:method::  void setSize(Dimension size)
   :outertype: VNodeMemo

setVnodeNumber
^^^^^^^^^^^^^^

.. java:method:: public void setVnodeNumber(int vnodeNumber)
   :outertype: VNodeMemo

