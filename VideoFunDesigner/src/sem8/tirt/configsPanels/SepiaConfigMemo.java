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
public class SepiaConfigMemo extends SimpleFilterConfigMemo {
    
    public static final String CONFIG_NAME = "Sepia";
    public static final String CONFIG_DESCRIPTION = "Applies Sepia filter to image.";

    public SepiaConfigMemo() {
        super(CONFIG_NAME, "FrameEditorSepia");
    }
    
}
