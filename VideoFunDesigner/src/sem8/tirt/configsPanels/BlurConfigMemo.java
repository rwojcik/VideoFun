/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt.configsPanels;

import sem8.tirt.AbstractVNodeConfigMemo;

/**
 *
 * @author Jacek Skoczylas
 */
public class BlurConfigMemo extends AbstractVNodeConfigMemo  {
    
    public static final String CONFIG_NAME = "Blur";
    public static final String CONFIG_DESCRIPTION = "Blures the image.";
    
    private int blurType;
    private int blurSizeX;
    private int blurSizeY;

    public BlurConfigMemo() {
        super(BlurConfigPanel.class, CONFIG_NAME);
        blurType = 0;
        blurSizeX = 11;
        blurSizeY = 11;
    }

    @Override
    protected String getRunCmdWithParams(StringBuilder builder) {
        builder.append("  -editor FrameEditorSmoothing");
        builder.append("  -editorparams ");
        builder.append(getParameters());
        return builder.toString();
    }

    @Override
    public String getParameters() {
        return blurSizeX + "," + blurSizeY + "," +blurType;
    }

    public int getBlurType() {
        return blurType;
    }

    public void setBlurType(int blurType) {
        this.blurType = blurType;
    }

    public int getBlurSizeX() {
        return blurSizeX;
    }

    public void setBlurSizeX(int blurSizeX) {
        this.blurSizeX = blurSizeX;
    }

    public int getBlurSizeY() {
        return blurSizeY;
    }

    public void setBlurSizeY(int blurSizeY) {
        this.blurSizeY = blurSizeY;
    }
    
    
    
}
