.. java:import:: java.io Serializable

.. java:import:: java.util.regex Matcher

.. java:import:: java.util.regex Pattern

VideoLink
=========

.. java:package:: sem8.tirt
   :noindex:

.. java:type:: public class VideoLink implements Serializable

   :author: jskoczyl

Fields
------
VIDEO_LINK_PATTERN
^^^^^^^^^^^^^^^^^^

.. java:field:: public static final Pattern VIDEO_LINK_PATTERN
   :outertype: VideoLink

Constructors
------------
VideoLink
^^^^^^^^^

.. java:constructor:: public VideoLink(int srcVNode, int srcOutput, int dstVNode, int dstInput)
   :outertype: VideoLink

VideoLink
^^^^^^^^^

.. java:constructor:: public VideoLink(String dstUrl, String srcUrl)
   :outertype: VideoLink

Methods
-------
cotainsUrl
^^^^^^^^^^

.. java:method::  boolean cotainsUrl(String inLink)
   :outertype: VideoLink

getDstInput
^^^^^^^^^^^

.. java:method:: public int getDstInput()
   :outertype: VideoLink

getDstVNode
^^^^^^^^^^^

.. java:method:: public int getDstVNode()
   :outertype: VideoLink

getSrcOutput
^^^^^^^^^^^^

.. java:method:: public int getSrcOutput()
   :outertype: VideoLink

getSrcVNode
^^^^^^^^^^^

.. java:method:: public int getSrcVNode()
   :outertype: VideoLink

getTmpTcp
^^^^^^^^^

.. java:method:: public int getTmpTcp()
   :outertype: VideoLink

matchPattern
^^^^^^^^^^^^

.. java:method:: static boolean matchPattern(String data)
   :outertype: VideoLink

setDstInput
^^^^^^^^^^^

.. java:method:: public void setDstInput(int dstInput)
   :outertype: VideoLink

setDstVNode
^^^^^^^^^^^

.. java:method:: public void setDstVNode(int dstVNode)
   :outertype: VideoLink

setSrcOutput
^^^^^^^^^^^^

.. java:method:: public void setSrcOutput(int srcOutput)
   :outertype: VideoLink

setSrcVNode
^^^^^^^^^^^

.. java:method:: public void setSrcVNode(int srcVNode)
   :outertype: VideoLink

setTmpTcp
^^^^^^^^^

.. java:method:: public void setTmpTcp(int tmpTcp)
   :outertype: VideoLink

toInputLink
^^^^^^^^^^^

.. java:method:: public static String toInputLink(int dstVNode, int dstInput)
   :outertype: VideoLink

toOutputLink
^^^^^^^^^^^^

.. java:method:: public static String toOutputLink(int srcVNode, int srcOutput)
   :outertype: VideoLink

