.. java:import:: java.awt Component

.. java:import:: java.io BufferedWriter

.. java:import:: java.io File

.. java:import:: java.io FileInputStream

.. java:import:: java.io FileOutputStream

.. java:import:: java.io IOException

.. java:import:: java.io ObjectInputStream

.. java:import:: java.io ObjectOutputStream

.. java:import:: java.io OutputStreamWriter

.. java:import:: java.io PrintStream

.. java:import:: java.io PrintWriter

.. java:import:: java.net DatagramSocket

.. java:import:: java.net ServerSocket

.. java:import:: java.util ArrayList

.. java:import:: java.util.logging Level

.. java:import:: java.util.logging Logger

.. java:import:: javax.swing JFileChooser

.. java:import:: javax.swing JOptionPane

.. java:import:: javax.xml.bind JAXBContext

.. java:import:: javax.xml.bind Marshaller

.. java:import:: javax.xml.bind.annotation XmlRootElement

OpenSaveManager
===============

.. java:package:: sem8.tirt
   :noindex:

.. java:type:: public class OpenSaveManager

   :author: jskoczyl

Constructors
------------
OpenSaveManager
^^^^^^^^^^^^^^^

.. java:constructor:: public OpenSaveManager(Component parentComponent, JFileChooser chooser)
   :outertype: OpenSaveManager

Methods
-------
available
^^^^^^^^^

.. java:method:: public static boolean available(int port)
   :outertype: OpenSaveManager

exportCmd
^^^^^^^^^

.. java:method::  File exportCmd(ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks)
   :outertype: OpenSaveManager

exportCmdAndRun
^^^^^^^^^^^^^^^

.. java:method::  void exportCmdAndRun(ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks)
   :outertype: OpenSaveManager

exportXml
^^^^^^^^^

.. java:method::  void exportXml(ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks)
   :outertype: OpenSaveManager

gui_openInto_orNull
^^^^^^^^^^^^^^^^^^^

.. java:method:: public ArrayList<VNodeMemo> gui_openInto_orNull(ArrayList<VideoLink> videoLinks)
   :outertype: OpenSaveManager

gui_save
^^^^^^^^

.. java:method:: public void gui_save(boolean saveAs, ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks)
   :outertype: OpenSaveManager

readInto
^^^^^^^^

.. java:method:: public ArrayList<VNodeMemo> readInto(File file, ArrayList<VideoLink> videoLinks) throws IOException, ClassNotFoundException
   :outertype: OpenSaveManager

save
^^^^

.. java:method:: public void save(File file, ArrayList<VNodeFrame> vNodeFrames, ArrayList<VideoLink> videoLinks) throws IOException
   :outertype: OpenSaveManager

