/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt;

import java.awt.Dimension;
import java.awt.Point;
import java.io.Serializable;

/**
 * Stores serializable data using by <code>VNodeFrame</code>.
 * 
 * @author Jacek Skoczylas
 */
public class VNodeMemo implements Serializable {
    
    private static final long serialVersionUID = -662238991505571100L;
    
    private int vnodeNumber;
    private AbstractVNodeConfigMemo configMemo;
    private Dimension size;
    private Point location;

    public VNodeMemo() {
    }

    public VNodeMemo(int vnodeNumber, AbstractVNodeConfigMemo configMemo) {
        this.vnodeNumber = vnodeNumber;
        this.configMemo = configMemo;
    }
    
    public VNodeMemo copy() {
        return new VNodeMemo(vnodeNumber, configMemo.copy());
    }

    public int getVnodeNumber() {
        return vnodeNumber;
    }

    public void setVnodeNumber(int vnodeNumber) {
        this.vnodeNumber = vnodeNumber;
    }

    public AbstractVNodeConfigMemo getConfigMemo() {
        return configMemo;
    }

    public void setConfigMemo(AbstractVNodeConfigMemo configMemo) {
        this.configMemo = configMemo;
    }

    public int getInputsNum() {
        return configMemo.getInputsNum();
    }

    public void setInputsNum(int inputsNum) {
        configMemo.setInputsNum(inputsNum);
    }

    public int getOutputsNum() {
        return configMemo.getOutputsNum();
    }

    public void setOutputsNum(int outputsNum) {
        configMemo.setOutputsNum(outputsNum);
    }

    void setLocation(Point location) {
        this.location = location;
    }

    void setSize(Dimension size) {
        this.size = size;
    }

    public Point getLocation_orNull() {
        return location;
    }

    public Dimension getSize_orNull() {
        return size;
    }
    
}
