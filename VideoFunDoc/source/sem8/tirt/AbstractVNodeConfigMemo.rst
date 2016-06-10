.. java:import:: java.io Serializable

.. java:import:: java.lang.reflect Constructor

.. java:import:: javax.swing JPanel

AbstractVNodeConfigMemo
=======================

.. java:package:: sem8.tirt
   :noindex:

.. java:type:: public class AbstractVNodeConfigMemo implements Serializable

   :author: jskoczyl

Fields
------
CONFIG_DESCRIPTION_FIELD_NAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:field:: public static final String CONFIG_DESCRIPTION_FIELD_NAME
   :outertype: AbstractVNodeConfigMemo

CONFIG_NAME_FIELD_NAME
^^^^^^^^^^^^^^^^^^^^^^

.. java:field:: public static final String CONFIG_NAME_FIELD_NAME
   :outertype: AbstractVNodeConfigMemo

cmdBlockName
^^^^^^^^^^^^

.. java:field:: protected String cmdBlockName
   :outertype: AbstractVNodeConfigMemo

Constructors
------------
AbstractVNodeConfigMemo
^^^^^^^^^^^^^^^^^^^^^^^

.. java:constructor:: public AbstractVNodeConfigMemo(Class panelClass, String configName)
   :outertype: AbstractVNodeConfigMemo

AbstractVNodeConfigMemo
^^^^^^^^^^^^^^^^^^^^^^^

.. java:constructor:: public AbstractVNodeConfigMemo(Class panelClass, String configName, int inputsNum, int outputsNum)
   :outertype: AbstractVNodeConfigMemo

Methods
-------
copy
^^^^

.. java:method:: public AbstractVNodeConfigMemo copy()
   :outertype: AbstractVNodeConfigMemo

createJPanel
^^^^^^^^^^^^

.. java:method:: public JPanel createJPanel() throws CannotCreateConfigPanelException
   :outertype: AbstractVNodeConfigMemo

getConfigName
^^^^^^^^^^^^^

.. java:method:: public String getConfigName()
   :outertype: AbstractVNodeConfigMemo

getInputsNum
^^^^^^^^^^^^

.. java:method:: public int getInputsNum()
   :outertype: AbstractVNodeConfigMemo

getMergeParams
^^^^^^^^^^^^^^

.. java:method:: public String getMergeParams()
   :outertype: AbstractVNodeConfigMemo

getMergeType
^^^^^^^^^^^^

.. java:method:: public int getMergeType()
   :outertype: AbstractVNodeConfigMemo

getNodeType
^^^^^^^^^^^

.. java:method:: public String getNodeType()
   :outertype: AbstractVNodeConfigMemo

getOutputsNum
^^^^^^^^^^^^^

.. java:method:: public int getOutputsNum()
   :outertype: AbstractVNodeConfigMemo

getPanelClass
^^^^^^^^^^^^^

.. java:method:: public Class getPanelClass()
   :outertype: AbstractVNodeConfigMemo

getParameters
^^^^^^^^^^^^^

.. java:method:: public String getParameters()
   :outertype: AbstractVNodeConfigMemo

getRunCmd
^^^^^^^^^

.. java:method:: public String getRunCmd(int[] ins, int[] outs)
   :outertype: AbstractVNodeConfigMemo

getRunCmdWithParams
^^^^^^^^^^^^^^^^^^^

.. java:method:: protected String getRunCmdWithParams(StringBuilder builder)
   :outertype: AbstractVNodeConfigMemo

setConfigName
^^^^^^^^^^^^^

.. java:method:: public void setConfigName(String configName)
   :outertype: AbstractVNodeConfigMemo

setInputsNum
^^^^^^^^^^^^

.. java:method:: public void setInputsNum(int inputsNum)
   :outertype: AbstractVNodeConfigMemo

setMergeParams
^^^^^^^^^^^^^^

.. java:method:: public void setMergeParams(String mergeParams)
   :outertype: AbstractVNodeConfigMemo

setMergeType
^^^^^^^^^^^^

.. java:method:: public void setMergeType(int mergeType)
   :outertype: AbstractVNodeConfigMemo

setNodeType
^^^^^^^^^^^

.. java:method:: public void setNodeType(String nodeType)
   :outertype: AbstractVNodeConfigMemo

setOutputsNum
^^^^^^^^^^^^^

.. java:method:: public void setOutputsNum(int outputsNum)
   :outertype: AbstractVNodeConfigMemo

setPanelClass
^^^^^^^^^^^^^

.. java:method:: public void setPanelClass(Class panelClass)
   :outertype: AbstractVNodeConfigMemo

setParameters
^^^^^^^^^^^^^

.. java:method:: public void setParameters(String s)
   :outertype: AbstractVNodeConfigMemo

writeFramesDestination
^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: protected void writeFramesDestination(int[] outs, StringBuilder builder)
   :outertype: AbstractVNodeConfigMemo

writeFramesSource
^^^^^^^^^^^^^^^^^

.. java:method:: protected void writeFramesSource(int[] ins, StringBuilder builder)
   :outertype: AbstractVNodeConfigMemo

