/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt;

import java.io.Serializable;
import java.lang.reflect.Constructor;
import javax.swing.JPanel;

/**
 * Stores serializable data about type and parameters of video block.
 * 
 * @author jskoczyl
 */
public class AbstractVNodeConfigMemo implements Serializable {

    public static final String CONFIG_NAME_FIELD_NAME = "CONFIG_NAME";
    public static final String CONFIG_DESCRIPTION_FIELD_NAME = "CONFIG_DESCRIPTION";

    private Class panelClass;
    private String configName;
    private int inputsNum;
    private int outputsNum;
    private String nodeType;
    protected String cmdBlockName = "block.py";
    private int mergeType = 0;
    private String mergeParams;

    public AbstractVNodeConfigMemo(Class panelClass, String configName) {
        this.panelClass = panelClass;
        this.configName = configName;
        inputsNum = 2;
        outputsNum = 1;
        nodeType = getClass().getSimpleName();
    }

    public AbstractVNodeConfigMemo(Class panelClass, String configName, int inputsNum, int outputsNum) {
        this.panelClass = panelClass;
        this.configName = configName;
        this.inputsNum = inputsNum;
        this.outputsNum = outputsNum;
    }

    public String getRunCmd(int[] ins, int[] outs, boolean asTcp) {
        StringBuilder builder = new StringBuilder();
        builder.append("start python ");
        builder.append(cmdBlockName);
        writeFramesSource(ins, builder, asTcp);
        writeFramesDestination(outs, builder, asTcp);
        if (getMergeType() != 0) {
            builder.append(" -merge ");
            builder.append(MergeConfigDialog.MERGERS_NAME[getMergeType()]);
            if (getMergeParams() != null && getMergeParams().trim().length() > 0) {
                builder.append(" -mergerparams ");
                builder.append(getMergeParams());
                builder.append(" ");
            }
        }
        return getRunCmdWithParams(builder);
    }

    protected void writeFramesDestination(int[] outs, StringBuilder builder, boolean asTcp) {
        if(asTcp) {
            listIntsOnCmd(" -framedestination TransmissionControlSinkServer  ", outs, builder);
        } else {
            listIntsOnCmd(" -framedestination DatagramSinkServer  ", outs, builder);
        }
    }

    protected void writeFramesSource(int[] ins, StringBuilder builder, boolean asTcp) {
        if(asTcp) {
            listIntsOnCmd(" -framesource TransmissionControlFrameGenerator  ", ins, builder);
        } else {
            listIntsOnCmd(" -framesource DatagramFrameGenerator  ", ins, builder);
        }
    }

    public String getParameters() {
        return "";
    }

    public void setParameters(String s) {
    }

    public AbstractVNodeConfigMemo copy() {
        return new AbstractVNodeConfigMemo(panelClass, configName);
    }

    public JPanel createJPanel() throws CannotCreateConfigPanelException {
        try {
            for(Constructor con : panelClass.getConstructors()) {
                Class[] types = con.getParameterTypes();
                if(types.length == 1 && types[0].isAssignableFrom(getClass())) {
                    return (JPanel) con.newInstance(this);
                }
            }
        } catch (Exception e) {
            throw new CannotCreateConfigPanelException("Can't create config panel: " + configName, e);
        }
        throw new CannotCreateConfigPanelException("Can't create config panel, no construnctor found: " + configName);
    }

    public Class getPanelClass() {
        return panelClass;
    }

    public void setPanelClass(Class panelClass) {
        this.panelClass = panelClass;
    }

    public String getConfigName() {
        return configName;
    }

    public void setConfigName(String configName) {
        this.configName = configName;
    }

    public int getInputsNum() {
        return inputsNum;
    }

    public void setInputsNum(int inputsNum) {
        this.inputsNum = inputsNum;
    }

    public int getOutputsNum() {
        return outputsNum;
    }

    public void setOutputsNum(int outputsNum) {
        this.outputsNum = outputsNum;
    }

    public String getNodeType() {
        return nodeType;
    }

    public void setNodeType(String nodeType) {
        this.nodeType = nodeType;
    }

    private void listIntsOnCmd(String prefix, int[] ins, StringBuilder builder) {
        boolean first = true;
        for (Integer i : ins) {
            if (i == -1) {
                continue;
            }
            if (first) {
                builder.append(prefix);
            } else {
                builder.append(",");
            }
            builder.append("localhost:");
            builder.append(i);
            first = false;
        }
    }

    public int getMergeType() {
        return mergeType;
    }

    public void setMergeType(int mergeType) {
        this.mergeType = mergeType;
    }

    public String getMergeParams() {
        return mergeParams;
    }

    public void setMergeParams(String mergeParams) {
        this.mergeParams = mergeParams;
    }

    protected String getRunCmdWithParams(StringBuilder builder) {
        throw new UnsupportedOperationException();
    }

}
