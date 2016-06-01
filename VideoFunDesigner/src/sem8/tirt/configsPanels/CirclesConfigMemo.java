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
public class CirclesConfigMemo extends AbstractVNodeConfigMemo {
    
    public static final String CONFIG_NAME = "Circles";
    public static final String CONFIG_DESCRIPTION = "Detects circles on image.";

    public CirclesConfigMemo() {
        super(CirclesConfigPanel.class, CONFIG_NAME);
    }

    @Override
    protected String getRunCmdWithParams(StringBuilder builder) {
        builder.append("  -editor FrameEditorCircles");
        return builder.toString();
    }
    
}
