/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sem8.tirt.configsPanels;

import java.util.Locale;
import sem8.tirt.AbstractVNodeConfigMemo;

/**
 *
 * @author Jacek Skoczylas
 */
public class ResizeConfigMemo extends AbstractVNodeConfigMemo  {
    
    public static final String CONFIG_NAME = "Resize";
    public static final String CONFIG_DESCRIPTION = "Resizes the image.";
    
    private double sizeX;
    private double sizeY;

    public ResizeConfigMemo() {
        super(ResizeConfigPanel.class, CONFIG_NAME);
        sizeX = 0.7;
        sizeY = 0.7;
    }

    @Override
    protected String getRunCmdWithParams(StringBuilder builder) {
        builder.append("  -editor FrameEditorResize");
        builder.append("  -editorparams ");
        builder.append(getParameters());
        return builder.toString();
    }

    @Override
    public String getParameters() {
        return String.format(Locale.US, "%.4f,%.4f", sizeX, sizeY);
    }

    public double getSizeX() {
        return sizeX;
    }

    public void setSizeX(double sizeX) {
        this.sizeX = sizeX;
    }

    public double getSizeY() {
        return sizeY;
    }

    public void setSizeY(double sizeY) {
        this.sizeY = sizeY;
    }
    
    
}
