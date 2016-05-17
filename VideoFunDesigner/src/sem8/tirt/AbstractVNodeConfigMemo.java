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

    public AbstractVNodeConfigMemo(Class panelClass, String configName) {
        this.panelClass = panelClass;
        this.configName = configName;
        inputsNum = 1;
        outputsNum = 1;
        nodeType = getClass().getSimpleName();
    }

    public AbstractVNodeConfigMemo(Class panelClass, String configName, int inputsNum, int outputsNum) {
        this.panelClass = panelClass;
        this.configName = configName;
        this.inputsNum = inputsNum;
        this.outputsNum = outputsNum;
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
            Constructor constructor = panelClass.getConstructor(getClass());
            return (JPanel) constructor.newInstance(this);
        } catch (Exception e) {
            throw new CannotCreateConfigPanelException("Can't create config panel: " + configName, e);
        }
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
    
}
