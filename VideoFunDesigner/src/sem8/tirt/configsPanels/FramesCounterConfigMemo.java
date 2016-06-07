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
public class FramesCounterConfigMemo extends SimpleFilterConfigMemo {
    
    public static final String CONFIG_NAME = "Frames Counter";
    public static final String CONFIG_DESCRIPTION = "Writes text with numer of frames on image corner.";

    public FramesCounterConfigMemo() {
        super(CONFIG_NAME, "FrameEditorFramesCounter");
    }
    
}
