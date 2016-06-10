.. java:import:: java.awt BorderLayout

.. java:import:: java.awt Color

.. java:import:: java.awt Point

.. java:import:: java.awt PopupMenu

.. java:import:: java.awt.datatransfer DataFlavor

.. java:import:: java.awt.datatransfer StringSelection

.. java:import:: java.awt.datatransfer Transferable

.. java:import:: java.awt.dnd DnDConstants

.. java:import:: java.awt.dnd DropTarget

.. java:import:: java.awt.event ActionEvent

.. java:import:: java.awt.event ActionListener

.. java:import:: java.awt.event ComponentAdapter

.. java:import:: java.awt.event ComponentEvent

.. java:import:: java.awt.event MouseAdapter

.. java:import:: java.awt.event MouseEvent

.. java:import:: java.awt.event MouseListener

.. java:import:: java.util.logging Level

.. java:import:: java.util.logging Logger

.. java:import:: javax.swing DropMode

.. java:import:: javax.swing JButton

.. java:import:: javax.swing JComponent

.. java:import:: javax.swing JPanel

.. java:import:: javax.swing TransferHandler

.. java:import:: javax.swing UIManager

.. java:import:: javax.swing.event InternalFrameAdapter

.. java:import:: javax.swing.event InternalFrameEvent

VNodeFrame
==========

.. java:package:: sem8.tirt
   :noindex:

.. java:type:: public class VNodeFrame extends javax.swing.JInternalFrame implements MouseListener

   It's JInternalFrame representing single video block in gui.

   :author: Jacek Skoczylas

Constructors
------------
VNodeFrame
^^^^^^^^^^

.. java:constructor:: public VNodeFrame(VNodeMemo memo)
   :outertype: VNodeFrame

   Creates new form AbstractVNodeFrame

Methods
-------
createConfigPanel
^^^^^^^^^^^^^^^^^

.. java:method:: protected JPanel createConfigPanel()
   :outertype: VNodeFrame

getInputLocationOnScreen_orNull
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public Point getInputLocationOnScreen_orNull(int n)
   :outertype: VNodeFrame

getLocationOnScreenOfMiddleOfButton_orNull
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: protected Point getLocationOnScreenOfMiddleOfButton_orNull(JButton b)
   :outertype: VNodeFrame

getMemo
^^^^^^^

.. java:method:: public VNodeMemo getMemo()
   :outertype: VNodeFrame

getOutputLocationOnScreen_orNull
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public Point getOutputLocationOnScreen_orNull(int n)
   :outertype: VNodeFrame

mouseClicked
^^^^^^^^^^^^

.. java:method:: @Override public void mouseClicked(MouseEvent e)
   :outertype: VNodeFrame

mouseEntered
^^^^^^^^^^^^

.. java:method:: @Override public void mouseEntered(MouseEvent e)
   :outertype: VNodeFrame

mouseExited
^^^^^^^^^^^

.. java:method:: @Override public void mouseExited(MouseEvent e)
   :outertype: VNodeFrame

mousePressed
^^^^^^^^^^^^

.. java:method:: @Override public void mousePressed(MouseEvent e)
   :outertype: VNodeFrame

mouseReleased
^^^^^^^^^^^^^

.. java:method:: @Override public void mouseReleased(MouseEvent e)
   :outertype: VNodeFrame

setParent
^^^^^^^^^

.. java:method:: public void setParent(VideoFunDesigner parent)
   :outertype: VNodeFrame

