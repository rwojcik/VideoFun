/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt.configsPanels;

import sem8.tirt.AbstractVNodeConfigMemo;

/**
 *
 * @author jskoczyl
 */
public class BlurConfigMemo extends AbstractVNodeConfigMemo  {
    
    public static final String CONFIG_NAME = "Blur";
    public static final String CONFIG_DESCRIPTION = "Blures the image.";
    
    private String blurName;
    private int blurSize;

    public BlurConfigMemo() {
        super(BlurConfigPanel.class, CONFIG_NAME);
        blurName = "Gaussian";
        blurSize = 10;
    }

    @Override
    public String getParameters() {
        return blurSize + "," + blurName;
    }

    public String getBlurName() {
        return blurName;
    }

    public void setBlurName(String blurName) {
        this.blurName = blurName;
    }

    public int getBlurSize() {
        return blurSize;
    }

    public void setBlurSize(int blurSize) {
        this.blurSize = blurSize;
    }    
    
}
