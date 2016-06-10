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
public class CameraSrcConfigMemo extends AbstractVNodeConfigMemo  {
    
    public static final String CONFIG_NAME = "Camera";
    public static final String CONFIG_DESCRIPTION = "Return output from camera.";

    public CameraSrcConfigMemo() {
        super(CameraSrcConfigPanel.class, CONFIG_NAME, 0, 1);
    }

    @Override
    protected void writeFramesSource(int[] ins, StringBuilder builder, boolean asTcp) {
        builder.append(" -framesource CameraFrameGenerator ");
    }
    
    @Override
    protected String getRunCmdWithParams(StringBuilder builder) {
        builder.append("  -editor FrameEditorEmpty ");
        return builder.toString();
    }
    
}
