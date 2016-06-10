.. java:import:: java.awt AWTEvent

.. java:import:: java.awt Point

.. java:import:: java.awt.event ActionEvent

.. java:import:: java.awt.event ActionListener

.. java:import:: java.awt.event FocusListener

.. java:import:: java.awt.event MouseAdapter

.. java:import:: java.awt.event MouseEvent

.. java:import:: java.io File

.. java:import:: java.lang.reflect Field

.. java:import:: java.util ArrayList

.. java:import:: java.util.logging Level

.. java:import:: java.util.logging Logger

.. java:import:: javax.swing JButton

.. java:import:: javax.swing JFileChooser

.. java:import:: javax.swing JOptionPane

.. java:import:: sem8.tirt.configsPanels InvertColorsConfigMemo

VideoFunDesigner
================

.. java:package:: sem8.tirt
   :noindex:

.. java:type:: public class VideoFunDesigner extends javax.swing.JFrame

   Main class to run. It's graphic user interface window.

   :author: Jacek Skoczylas

Fields
------
CONFIG_DEFAUTL_DESC
^^^^^^^^^^^^^^^^^^^

.. java:field:: public static final String CONFIG_DEFAUTL_DESC
   :outertype: VideoFunDesigner

INTERNAL_FRAME_OFFSET
^^^^^^^^^^^^^^^^^^^^^

.. java:field:: public static final int INTERNAL_FRAME_OFFSET
   :outertype: VideoFunDesigner

VNODES_CONFIGS
^^^^^^^^^^^^^^

.. java:field:: public static final Class<? extends AbstractVNodeConfigMemo>[] VNODES_CONFIGS
   :outertype: VideoFunDesigner

Constructors
------------
VideoFunDesigner
^^^^^^^^^^^^^^^^

.. java:constructor:: public VideoFunDesigner()
   :outertype: VideoFunDesigner

   Creates new form ViedoFunDesigner

Methods
-------
addVNode
^^^^^^^^

.. java:method:: protected void addVNode(Class<? extends AbstractVNodeConfigMemo> configMemoClass)
   :outertype: VideoFunDesigner

addVNode
^^^^^^^^

.. java:method:: protected void addVNode(Class<? extends AbstractVNodeConfigMemo> configMemoClass, int dx, int dy)
   :outertype: VideoFunDesigner

addVideoLink
^^^^^^^^^^^^

.. java:method:: public void addVideoLink(VideoLink link)
   :outertype: VideoFunDesigner

deleteAllLinksWithInLink
^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public void deleteAllLinksWithInLink(String inLink)
   :outertype: VideoFunDesigner

getConfigName
^^^^^^^^^^^^^

.. java:method:: static String getConfigName(Class c)
   :outertype: VideoFunDesigner

getVNodeFrame
^^^^^^^^^^^^^

.. java:method:: public VNodeFrame getVNodeFrame(int n)
   :outertype: VideoFunDesigner

getVideoLinks
^^^^^^^^^^^^^

.. java:method:: public ArrayList<VideoLink> getVideoLinks()
   :outertype: VideoFunDesigner

main
^^^^

.. java:method:: public static void main(String[] args)
   :outertype: VideoFunDesigner

   :param args: the command line arguments

putToWindowVNode
^^^^^^^^^^^^^^^^

.. java:method:: public void putToWindowVNode(VNodeFrame node)
   :outertype: VideoFunDesigner

setDescText
^^^^^^^^^^^

.. java:method:: public void setDescText(String desc)
   :outertype: VideoFunDesigner

