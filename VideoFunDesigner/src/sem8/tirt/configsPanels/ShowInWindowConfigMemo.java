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
public class ShowInWindowConfigMemo extends AbstractVNodeConfigMemo  {
    
    public static final String CONFIG_NAME = "Show";
    public static final String CONFIG_DESCRIPTION = "Creates windows where video from input are showing.";

    public ShowInWindowConfigMemo() {
        super(ShowInWindowConfigPanel.class, CONFIG_NAME, 2, 0);
    }

    @Override
    protected void writeFramesDestination(int[] outs, StringBuilder builder, boolean asTcp) {
        // do nothing
    }
    
    @Override
    protected String getRunCmdWithParams(StringBuilder builder) {
        builder.append("  -editor FrameEditorEmpty ");
        return builder.toString();
    }
    
}
